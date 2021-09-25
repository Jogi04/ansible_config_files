#!/bin/bash


useradd -m -s /bin/bash ansible
passwd ansible
touch /etc/sudoers.d/ansible
echo 'ansible ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/ansible

apt install ansible
apt install git
git clone https://github.com/Jogi123/ansible_config_files.git  /home/ansible/ansible_config_files
