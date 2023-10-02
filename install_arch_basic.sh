#!/bin/bash

set -e  # Exit immediately if any command fails

# Define variables
BOOT_PARTITION="/dev/vda1"
ROOT_PARTITION="/dev/vda2"
HOME_PARTITION="/dev/vda3"
TIMEZONE="Europe/Berlin"
read -p "what is your hostname? " HOSTNAME
read -p "Your username? " USERNAME

# Partition and format the disk (Assuming /dev/vda for simplicity)
echo "Partitioning and formatting the disk..."
(
  echo o; echo n; echo p; echo 1; echo ""; echo +512M;  # EFI partition
  echo n; echo p; echo 2; echo ""; echo +20G;          # Root partition
  echo n; echo p; echo 3; echo ""; echo "";            # Home partition
  echo t; echo 1; echo 1;                               # Set type for EFI
  echo w
) | fdisk /dev/vda

# Create file systems
mkfs.fat -F32 $BOOT_PARTITION
mkfs.ext4 $ROOT_PARTITION
mkfs.ext4 $HOME_PARTITION

# Mount partitions
mount $ROOT_PARTITION /mnt
mkdir -p /mnt/boot/efi
mount $BOOT_PARTITION /mnt/boot/efi
mkdir -p /mnt/home
mount $HOME_PARTITION /mnt/home

# Install Arch Linux base system
echo "Installing Arch Linux base system..."
pacstrap /mnt base base-devel linux linux-firmware

# Generate fstab
genfstab -U /mnt >> /mnt/etc/fstab

# Change root into the new system
arch-chroot /mnt <<EOF
# Set the timezone
ln -sf /usr/share/zoneinfo/$TIMEZONE /etc/localtime
hwclock --systohc

# Uncomment the desired locale(s) in /etc/locale.gen
# Generate the locales
locale-gen

# Set the hostname
echo "$HOSTNAME" > /etc/hostname

# Edit /etc/hosts
# Add the following lines:
# 127.0.0.1  localhost
# ::1        localhost
# 127.0.1.1  $HOSTNAME.localdomain  $HOSTNAME

# Set the root password
passwd

# Create a new user
useradd -m -G wheel $USERNAME
passwd $USERNAME

# Allow wheel group to execute sudo
echo "%wheel ALL=(ALL) ALL" >> /etc/sudoers
EOF

# Install and configure bootloader (Grub in this example)
pacman -S grub efibootmgr
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=arch
grub-mkconfig -o /boot/grub/grub.cfg

# Install and configure Qtile window manager and Xorg
pacman -S xorg qtile picom qtile-extras

# Install paru AUR helper
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si

# Install Firefox, Zoom, Steam, and Slack (you can add more packages)
paru -S firefox zoom steam slack-desktop rofi kitty 

# Enable services (e.g., for NetworkManager)
systemctl enable NetworkManager

# move configs folders to the config local folder
cp -R .config/* /home/$USERNAME/.config/ 

# Exit the chroot environment
exit

# Unmount partitions and reboot
umount -R /mnt
reboot