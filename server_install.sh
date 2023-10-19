#! /bin/bash

echo 'Starting fantastic server install script'
echo '================================================'
echo 'Updating repos and upgrading installed packages'
echo '================================================'
sudo apt update
sudo apt upgrade
echo 'Installing applications for server'
echo '================================================'
sudo apt install neofetch net-tools ranger neovim htop btop tree
echo 'neofetch' >> .bashrc
echo 'Installing and configuring Network Manager'
echo '================================================'
sudo apt install network-manager
sudo rm /etc/NetworkManager/NetworkManager.conf
sudo cp /config/NetworkManager.conf /etc/NetworkManager/
sudo systemctl enable NetworkManager --now
echo '================================================'
echo '.......done!!!'
