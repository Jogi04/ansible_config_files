#!/bin/bash

useradd -m ansible
passwd ansible
touch /etc/sudoers.d/ansible
echo 'ansible ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/ansible

apt install openssh-server -y
systemctl start sshd
systemctl enable sshd

mkdir /home/ansible/.ssh
ssh jogi@10.0.0.100 "cat /home/jogi/.ssh/ansible.pub" > /home/ansible/.ssh/authorized_keys
chmod 744 -R /home/ansible/.ssh/
chown -R ansible:ansible /home/ansible/.ssh/
