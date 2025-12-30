#!/bin/bash

echo "Welcome to Alph's Dotfiles!"
echo "Have you installed Dotfiles before? (Y/n)"

if [[ "$ans" =~ ^[Nn]$ ]]; then
    exit 1
fi


sudo pacman -S --needed \
  dolphin dunst grim hyprland kitty polkit-kde-agent \
  qt5-wayland qt6-wayland slurp uwsm wofi \
  xdg-desktop-portal-hyprland hyprpaper hyprctl


	#Keybind Config

cd Hyprland-dotfiles || exit 1
rm ~/.config/hypr/hyprland.conf
mkdir -p ~/.config/hypr
mkdir ~/Wallpapers
cp -r Hyprland-dotfiles/* ~/.config/hypr/


	#Waybar Config

fc-list | grep -i nerd
sudo pacman -S ttf-jetbrains-mono-nerd

	#Keybind Config
	

	#Hyprpaper Config
sudo pacman -S hyprpaper

	#Audio Config

sudo pacman -S blueman bluez bluez-utils
echo "Do you wan to reboot (Y/n)"
read ans
if [[ "$ans" =~ ^[Nn]$ ]]; then
    exit 0
else
    reboot
fi


