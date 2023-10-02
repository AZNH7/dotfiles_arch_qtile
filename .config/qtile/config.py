
import os
import subprocess
from libqtile import hook
from libqtile import qtile
from typing import List  
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.dgroups import simple_key_binder
import colors
from qtile_extras.widget.decorations import RectDecoration



#Variables
mod = "mod4"
mod1 = "mod1"
browser = 'firefox -P'
terminal = 'kitty'
text_editor = terminal + ' nano'
file_manager1 = 'thunar'
file_manager2 = terminal + ' ranger'
file_launcher1 = "dmenu_run -c -l 20 -p 'Run: '"
file_launcher2 = 'rofi -show drun' # -theme ~/.config/rofi/launcher.rasi'
email_cliant = 'thunderbird'
process_viewer = terminal + ' btop'
config_menu = '.local/bin/config_menu'
websites_menu = '.local/bin/websites_menu'
colorscheme_menu = '.local/bin/colorscheme_menu'
power_menu = '.local/bin/power_menu'

mbfs = colors.mbfs()
doomOne = colors.doomOne()
dracula = colors.dracula()
everforest = colors.everforest()
nord = colors.nord()
gruvbox = colors.gruvbox()
OneDark = colors.OneDark()
blackboard = colors.blackboard()
TomorrowNight = colors.TomorrowNight()
TokyoNight = colors.TokyoNight()
darkcutom = colors.DarkCustom()
afternooncoffee = colors.afternooncoffee()
darenowardrobe = colors.darenowardrobe()

#Choose colorscheme
colorscheme = darenowardrobe

#Colorschme funcstion
colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo = colorscheme 

# functions 
# Call Calendar Notification
# def calendar_notification(qtile):{
#     subprocess.call(os.path.expanduser('~/.local/bin/calendar'))
# }
# def calendar_notification_prev(qtile):{
#     subprocess.call(os.path.expanduser('~/.local/bin/calendar', 'prev'))
# }

#KEYBINDINGS

#Window keybindings
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc = "Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc = "Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc = "Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc = "Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc = "Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc = "Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc = "Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc = "Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows
    Key([mod, mod1], "h", 
        lazy.layout.grow(), 
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)' ),
    Key([mod, mod1], "l",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)' 
        ),
    Key([mod], "n", lazy.layout.normalize(), desc = "Reset all window sizes"), # not working, need to fix it
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc = "Toggle fullscreen"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "space", lazy.layout.toggle_split(),
        desc = "Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc = "Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc = "Toggle between layouts"),
    
    # Close windows
    Key([mod, "shift"], "c", lazy.window.kill(), desc = "Kill focused window"),
    
    # Close, logout and reset Qtile
    Key([mod, "shift"], "r", lazy.restart(), desc = "Restart Qtile"),
    Key([mod, "shift"], "q", lazy.spawn("shutdown now"), desc = "Shutdown"),
    Key([mod, "control"], "r", lazy.spawn("reboot"), desc = "Reboot"),
    # Key([mod, "control"], "l", lazy.spawn("betterlockscreen -l"), desc= "Screen Lock"),
    Key([mod, "control"], "l", lazy.spawn("xscreensaver-command -lock"), desc= "Screen Lock"),

    # move between monitors
    Key([mod], "period", lazy.next_screen(), desc = "Move focus to next monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc = "Move focus to prev monitor"),

    # Applications

    # rofi
    Key([mod], "w", lazy.spawn(file_launcher2 + ' -show'), desc = "Launch rofi"),
    Key([mod], "d", lazy.spawn(file_launcher2 + ' -show drun'), desc = "Launch rofi drun"),
    
    # Open Terminal    
    Key([mod], "Return", lazy.spawn(terminal), desc = "Launch terminal"),
    
    #Browser
    Key([mod, "shift"], "b", lazy.spawn(browser), desc = "Launch browser"),

    #Text editor
    Key([mod, "shift"], "n", lazy.spawn(text_editor), desc = "Launch nano"),

    #Email cliant
    # Key([mod], "e", lazy.spawn(email_cliant), desc = "Launch thunderbird"),
    
    # Webcam configuration
    Key([mod, "control"], "c", lazy.spawn(terminal + " qv4l2"), desc = "open the webcam setting"),

    #File manager
    Key([mod, "shift"], "f", lazy.spawn(file_manager1), desc = "Lauch primary file manager"),

    #dmenu
    Key([mod, "shift"], "Return", lazy.spawn(file_launcher1), desc = "Launch primary launcher"),

    # screenshot with scrot
    Key([], "Print", lazy.spawn("scrot '%Y-%m-%d_$wx$h.png' -e 'mv $f ~/screenshots/'"), desc = "Take a screenshot"),
    Key([mod], "Print", lazy.spawn("scrot -s '%Y-%m-%d_$wx$h.png' -e 'mv $f ~/screenshots/'"), desc = "Take a screenshot of a selected area"),
    Key([mod, "shift"], "Print", lazy.spawn("scrot -u '%Y-%m-%d_$wx$h.png' -e 'mv $f ~/screenshots/'"), desc = "Take a screenshot of a focused window"),

    #Rofi Bash scripts
    Key([mod], "d", lazy.spawn(file_launcher2), desc = "Launch secondary launcher"),
    # Key([mod, "control"], "c", lazy.spawn(config_menu), desc = "Launch rofi configuration menu"),
    # Key([mod, "control"], "b", lazy.spawn(websites_menu), desc = "Launch rofi website menu"),
    # Key([mod, "control"], "t", lazy.spawn(colorscheme_menu), desc = "Launch rofi colorscheme menu"),
    # Key([mod, "control"], "p", lazy.spawn(power_menu), desc = "Launch rofi power menu"),

    #Backup run launcher
    Key([mod], "r", lazy.spawncmd(), desc = "Spawn a command using a prompt widget"),

    #drive anlyzer
    Key([mod, "shift"], "d", lazy.spawn(terminal + " gdu"), desc = "Open GDU for disk anlyzer"),
    
# Hardware/system control
    #Sound
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),

    #Brightness for laptop
    # Key([], "XF86MonBrightnessUp", lazy.spawn("lux -a 10%")),
    # Key([], "XF86MonBrightnessDown", lazy.spawn("lux -s 10%")),
]

groups = [Group("1", layout='RatioTile', matches=[Match(wm_class=["firefox"])]), 
          Group("2", layout='RatioTile'),
          Group("3", layout='Tile', matches=[Match(wm_class=["kitty"])]),
          Group("4", layout='RatioTile'),
          Group("5", layout='RatioTile', matches=[Match(wm_class=["slack"])]),
          Group("6", layout='RatioTile', matches=[Match(wm_class=["zoom"])]),
          Group("7", layout='RatioTile'),
          Group("8", layout='RatioTile'),
          Group("9", layout='RatioTile'),
          Group("0", layout='RatioTile', matches=[Match(wm_class=["steam"])]),
]

dgroups_key_binder = simple_key_binder(mod)

def window_to_previous_screen(qtile, switch_group=False, switch_screen=True):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=True):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)
                                    
keys.extend([
    # MOVE WINDOW TO NEXT SCREEN
    Key([mod,"shift"], "Left", lazy.function(window_to_next_screen)),
    Key([mod,"shift"], "Right", lazy.function(window_to_previous_screen)),
])
# groups = []
# groups_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# groups_labels = ["", "󰇮", "", "", "󰈙", "", "", "", "", ""]
# groups_labels = ["", "󰇮", "", "", "󰈙", "", "", "", "", ""]
# groups_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('terminal', terminal, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.7),
    DropDown('slack', 'slack', width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('file_manager2', file_manager2, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('process_viewer', process_viewer, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
]))

# extend keys list with keybinding for scratchpad
keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('terminal')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('slack')),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('file_manager2')),
    Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('process_viewer')),
])  

layouts = [
    layout.Bsp(border_focus = colors[9], border_normal = colors[0], border_width = 3, margin = 0),
    # layout.MonadTall(border_focus = colors[9], border_normal = colors[0], border_width = 3, margin = 8),
    # layout.MonadWide(border_focus = colors[9], border_normal = colors[0], border_width = 3, margin = 8),
    # layout.Floating(border_focus = colors[9], border_normal = colors[0], border_width = 3, margin = 8),
    layout.RatioTile(border_focus = colors[9], border_normal = colors[0], border_width = 3, margin = 0),
    layout.Tile(border_focus = colors[9], border_normal = colors[0], border_width = 3, margin = 0),
    # layout.Max(border_focus = colors[9], border_normal = colors[0], border_width = 3, margin = 8),
    # layout.TreeTab(border_focus = colors[9], border_normal = colors[0], border_width = 3, margin = 8),
    #layout.Stack(num_stacks=2),
    # layout.Matrix(border_focus = colors[9], border_normal = colors[0], border_width = 3, margin = 8),
    #layout.TreeTab(border_focus = colors[9], border_normal = colors[0], border_width = 3, margin = 8),
    # layout.VerticalTile(border_focus = colors[9], border_normal = colors[0], border_width = 3, margin = 8),
    # layout.Zoomy(border_focus = colors[9], border_normal = colors[0], border_width = 3, margin = 8),
]

widget_defaults = dict(
    font = 'Hack Nerd Font Bold',
    fontsize = 16, # default font size for text widgets
    padding = 2, # default padding for all widgets
    background = colors[0] # default background color for all widgets = colors[0]
)
extension_defaults = widget_defaults.copy()

# def for the widgets list
def init_widgets_list():
    widgets_list = [
            widget.Image(
                filename = '~/arch_color.png',
                scale = True,
                margin_x = 5,
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(file_launcher2)}
                ),
            widget.GroupBox(
                active = colors[7],
                inactive = colors[0],
                highlight_color = colors[8],  
                highlight_method = 'line', # 'block', 'text' or 'line'
                other_current_screen_border = colors[8],
                other_screen_border = colors[2],
                this_current_screen_border = colors[8],
                this_screen_border = colors[2],
                urgent_border = colors[6],
                urgent_text = colors[6],
                ),
            widget.CurrentLayout(
                scale = 0.7,
                foreground = colors[4],
                
                ),
            widget.WindowName(
                foreground = colors[9],
                font='Hack Nerd Font Bold',
                for_current_screen = False,
                format = '{state} {name}',
                max_chars = 80,
                markup = True,
                ),
            widget.Chord(
                chords_colors = {
                    'launch': (foregroundColor, foregroundColor),
                },
                name_transform=lambda name: name.upper(),
                ),

                
            # widget.TextBox(
            #     text='\u25e2',
            #     padding = 0,
            #     fontsize = 50,
            #     background = backgroundColor,
            #     foreground = foregroundColorTwo
            #     ),
            # widget.TextBox(
            #     text='\u25e2',
            #     padding = 0,
            #     fontsize = 14,
            #     background = foregroundColorTwo,
            #     foreground = foregroundColorTwo
            #     ),
            
            widget.Net(
                interface = "eno2",
                format = ' {down} ↓↑ {up}',
                prefix = 'M',
                foreground = colors[4],
                mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn(terminal + ' -e nmtui')},
                ),
            # widget.Bluetooth(
            #     format = ' {percent:2.0%}',
            #     foreground = colors[4],
            #     padding = 8,
            #     mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn(terminal + ' -e blueman-manager')},
            #     ),
            widget.CPU(
                format = ' {load_percent}%',
                foreground = colors[4],
                mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn(terminal + ' -e btop')},
                ),
            widget.Memory(
                format = '{MemUsed: .0f}{mm}',
                measure_mem = 'G',
                foreground = colors[4],
                mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn(terminal + ' -e btop')},
                ),
            widget.OpenWeather(
                decorations=[RectDecoration(colour=colors[0], radius=7, filled=True)],
                foreground = colors[4],
                app_key = '3b4f646548de75b00e10a0d853e6cdc6',
                cityid = '2950159',
                weather_symbols = {
                "Unknown": "",
                "01d": "",
                "01n": "🌕",
                "02d": "",
                "02n": "",
                "03d": "",
                "03n": "",
                "04d": "",
                "04n": "",
                "09d": "⛆",
                "09n": "⛆",
                "10d": "",
                "10n": "",
                "11d": "🌩",
                "11n": "🌩",
                "13d": "❄",
                "13n": "❄",
                "50d": "🌫",
                "50n": "🌫",
                },
                format = '{icon} {main_temp}°{units_temperature}',
                metric = True,
                update_interval = 600,
            ),
            widget.CheckUpdates(
                update_interval = 3600,
                distro = "Arch",
                display_format = "Updates: {updates} ",
                no_update_string = " No Updates",
                colour_have_updates = colors[7],
                colour_no_updates = colors[4],
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e pacman -Syu')},
                # background = foregroundColorTwo
                ),
            widget.PulseVolume(
                foreground = colors[4],
                # theme_path = "/home/$USER/.config/qtile/icons/volume_icons",
                emoji = True, 
                emoji_list = {
                    'mute': '',
                    'low': '',
                    'medium': '',
                    'high': '',
                    'max':  '',
                },
                mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn(terminal + ' -e pavucontrol')},
                volume_app = 'pavucontrol',
                volume_up_command = 'pactl set-sink-volume @DEFAULT_SINK@ +5%',
                volume_down_command = 'pactl set-sink-volume @DEFAULT_SINK@ -5%',
                ),
            widget.Systray(
                ),
            # widget.TextBox(
            #     text='\u25e2',
            #     padding = 0,
            #     fontsize = 50,
            #     background = foregroundColorTwo,
            #     foreground = backgroundColor
            #     ),
            # widget.Systray(
            #     icon_size = 15,
            #     padding = 5,
            #     ),
            widget.Clock(format=' %a, %d. %m. %Y.%Z',
                foreground = colors[4],
                ),
            
            widget.Clock(format=' %I:%M %p',
                foreground = colors[4],
                ),
    ]
    return widgets_list        


# function to display widgets on two monitors

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    # del widgets_screen1[0]               # Slicing removes unwanted widgets (systray) on Monitors 1
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    # del widgets_screen2[1:9]                # Slicing removes unwanted widgets (systray) on Monitor 2
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=30)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=30)),
            # Screen(top=bar.Bar(widgets=init_widgets_screen3(), opacity=1.0, size=20))
            ]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start = lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start = lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(border_focus = colors[4], float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class = 'ssh-askpass'),  # ssh-askpass
    Match(title = 'branchdialog'),  # gitk
    Match(title = 'pinentry'),  # GPG key password entry
    Match (title='zoom*'), # Zoom
    Match (title='Steam*'), # Steam
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='archlinux-logout'),
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
])

auto_fullscreen = True
focus_on_window_activation = "smart"  # or focus
reconfigure_screens = True

#Programms to start on log in
@hook.subscribe.startup_once
def autostart ():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

# hook to change monitors based on xrandr output changes
# @hook.subscribe.screen_change
# def restart_on_randr(qtile, ev):
#     qtile.cmd_restart()
    
# # reconfigure output on screen changes
# @hook.subscribe.screens_reconfigured
# def screens_reconfigured(qtile, ev):
#     for i in qtile.screens:
#         if i.x == 0:
#             qtile.screens.remove(i)
#             qtile.screens.insert(0, i)
#     qtile.cmd_restart()


floating_types = ["notification", "toolbar", "splash", "dialog"]

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
