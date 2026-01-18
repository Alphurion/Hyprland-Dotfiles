#!/bin/bash

echo "Welcome to Alph's Dotfiles!"
echo "This script requires python to work, do you wish to install python? [Y/n]"

if [[ "$ans" =~ ^[Nn]$ ]]; then
    exit 1
fi

workingDir = $pwd
sudo pacman -S python
python3 script.py


echo "Do you wan to reboot (Y/n)"
read ans
if [[ "$ans" =~ ^[Nn]$ ]]; then
    exit 0
else
    reboot
fi


