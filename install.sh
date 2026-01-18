#!/bin/bash

echo "Welcome to Alph's Dotfiles!"
echo "This script requires python to work, do you wish to install python? [Y/n]"

if [[ "$ans" =~ ^[Nn]$ ]]; then
    exit 1
fi

Working_Dir = $pwd
sudo pacman -S python
python3 script.py Working_Dir


echo "Do you wan to reboot (Y/n)"
read ans
if [[ "$ans" =~ ^[Nn]$ ]]; then
    exit 0
else
    reboot
fi


