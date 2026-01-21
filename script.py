import subprocess
import shlex
import os

#----- Variables -----#

tips = False
saveConfig = True
mainPath = " "
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
    "noto-fonts-emoji",
    "ttf-jetbrains-mono-nerd"
]


#----- Begin program -----#


print(title, "\n Have you installed these dotfiles before? [Y,n]")
user_input = input()

if [user_input != "n"]:
    user_input = "Y"

if [user_input == "Y"]:
    tips = True

user_input = " "
#Installing basic hyprland
for program in installs:
    Install_Program(program)

# Wallpaper
bash("chmod +x /scripts/wallpaper.sh")
bash("./wallpaper.sh")

# Audio setup
if not bash("command -v pipewire") and not bash("command -v pulseaudio"):
    print("It appears you do not have any audio software installed, would you like to use (1) Pipewire or (2) Pulseaudio")
    user_input = input("> ")

subprocess.run(['echo', 'Installing Bluetooth...'])
bash("sudo pacman -S blueman bluez bluez-utils")

    
#----- Functions -----#

def Install_Program(program):
    subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', program])

def Save_Configuration(program, saveConfig):
    print(program, "appears to have configurations, do you wish to save them?[Y, n]")
    user_input = input()

def bash(command):
    args = shlex.split(command)
    subprocess.run(args)
