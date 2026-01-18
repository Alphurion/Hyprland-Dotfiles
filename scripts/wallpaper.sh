#!/bin/bash

cd Hyprland-dotfiles || exit 1

if [!(d "/.config/hypr")]; then
mkdir -p ~/.config/hypr

mkdir ~/Wallpapers

cp -r Hyprland-dotfiles/* ~/.config/hypr/
