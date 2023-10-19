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
echo 'Installing minimal neovim config'
echo '================================================'
mkdir ~/.config/nvim
cp /config/init.vim ~/.config/nvim/
echo 'Installing and configuring Network Manager'
echo '================================================'
sudo apt install network-manager
sudo rm /etc/NetworkManager/NetworkManager.conf
sudo cp /config/NetworkManager.conf
sudo systemctl enable NetworkManager --now
echo '.......done!!!'
