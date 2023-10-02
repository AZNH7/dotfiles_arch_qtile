#!/bin/zsh

# xrandr | grep -i " connected" | cut -d" " -f1 

displayNUmber=$(xrandr | awk '/ connected/{print $1}' | dmenu)

echo $displayNUmber

# displayOrientation=$(xrandr | grep -i $displayNUmber | cut -d" " -f4 | dmenu -i -p -c -l 5 "Select orientation")

displayOrientation=$(echo -e "--below \n--left-of \n--right-of \n--above" | dmenu)
echo $displayOrientation

xrandr --output $displayNUmber $displayOrientation eDP-1