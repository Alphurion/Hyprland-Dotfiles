#!/bin/bash

echo "Welcome to Alph's Dotfiles!\n Have you installed Dotfiles before? (Y/n)"
sleep 10
sudo pacman -S dolphin
sudo pacman -S dunst
sudo pacman -S grim
sudo pacman -S hyprland
sudo pacman -S kitty
sudo pacman -S polkit-kde-agent
sudo pacman -S qt5-wayland
sudo pacman -S qt6-wayland
sudo pacman -S slurp
sudo pacman -S uwsm
sudo pacman -S wofi
sudo pacman -S xdg-desktop-portal-hyprland

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
