import subprocess

#----- Variables -----#

tips = False
saveConfig = True

# Text
title = """ 
▄▖▜   ▌ ▌    ▖▖      ▜      ▌  ▄   ▗   
▌▌▐ ▛▌▛▌ ▛▘  ▙▌▌▌▛▌▛▘▐ ▀▌▛▌▛▌  ▌▌▛▌▜▘▛▘
▛▌▐▖▙▌▌▌ ▄▌  ▌▌▙▌▙▌▌ ▐▖█▌▌▌▙▌  ▙▘▙▌▐▖▄▌
    ▌          ▄▌▌                     
"""
# Program

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
    "noto-fonts",
    "noto-fonts-cjk",
    "noto-fonts-emoji"
]


#----- Begin program -----#


print(title, "\n Have you installed these dotfiles before? [Y,n]")
user_input = input()

if [user_input != "n"]:
    user_input = "Y"

if [user_input == "Y"]:
    tips = True

#Installing basic hyprland
for program in installs:
    Install_Program(program)

#----- Functions -----#
def Install_Program(program):
    subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', program])

def Save_Configuration(program, saveConfig):
    print(program, "appears to have configurations, do you wish to save them?[Y, n]")
    user_input = input()
