#!/bin/bash

echo "Welcome to Alph's Dotfiles!"
echo "Have you installed Dotfiles before? (Y/n)"

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


