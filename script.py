#
# sudo pacman -S --needed \
#   dolphin dunst grim hyprland kitty polkit-kde-agent \
#   qt5-wayland qt6-wayland slurp uwsm wofi \
#   xdg-desktop-portal-hyprland hyprctl \

import subprocess

Tips = False

installs = [
    "dolphin",
    "dunst",
    "grim",
    "hyprland",
    "kitty",
    "polkit-kde-agent",
    "qt5-wayland",
    "qt6-wayland",
    "slurp",
    "uwsm",
    "wofi",
    "xdg-desktop-portal-hyprland",
    "hyprctl",
]


title = """ 
▄▖▜   ▌ ▌    ▖▖      ▜      ▌  ▄   ▗   
▌▌▐ ▛▌▛▌ ▛▘  ▙▌▌▌▛▌▛▘▐ ▀▌▛▌▛▌  ▌▌▛▌▜▘▛▘
▛▌▐▖▙▌▌▌ ▄▌  ▌▌▙▌▙▌▌ ▐▖█▌▌▌▙▌  ▙▘▙▌▐▖▄▌
    ▌          ▄▌▌                     
"""
print(title, "\n Have you installed these dotfiles before? [Y,n]")
user_input = input()
if [user_input != "n"]:
    user_input = "Y"

if [user_input == "Y"]:
    Tips = True

for program in installs:
    subprocess.run(['sudo', 'pacman', '-S', 'noconfirm' program])
    
