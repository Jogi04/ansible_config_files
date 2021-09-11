#!/bin/bash

useradd -m ansible
passwd ansible
touch /etc/sudoers.d/ansible
echo 'ansible ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/ansible

apt install openssh-server -y
systemctl start sshd
systemctl enable sshd
mkdir /home/ansible/.ssh
sftp jogi@10.0.0.100:/home/jogi/.ssh/ansible.pub /home/ansible/.ssh/ansible.pub
chmod 644 /home/ansible/.ssh/ansible.pub
chown ansible:ansible /home/ansible/.ssh/ansible.pub
