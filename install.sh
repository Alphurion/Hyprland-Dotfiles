#!/bin/bash

echo "Welcome to Alph's Dotfiles!"


	#Keybind Config

cd Hyprland-dotfiles
rm ~/.config/hypr/hyprland.conf
cp Hyprland-dotfiles ~/hypr/

	#Waybar Config

fc-list | grep -i nerd
sudo pacman -S ttf-jetbrains-mono-nerd

	#Keybind Config



	#Hyprpaper Config

sudo pacman -S hyprpaper

	#Audio Config

sudo pacman -S blueman bluez bluez-utils

exit 0
