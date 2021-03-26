#!/bin/python


import os
import sys
import subprocess
import re
from termcolor import cprint


class AnsibleSetup:
    def __init__(self, username, server_ips, initial_setup=False):
        self.username = username
        self.server_ips = server_ips
        self.initial_setup = initial_setup

    def setup(self):
        """
        main function; if initial_setup == False, only a key will be copied; otherwise it will install ansible and ssh,
        start and enable ssh, generate ssh keys, install sshpass to automate the initial login and remove sshpass at the
        end
        """
        system_package_manager = self.check_underlying_package_manager()
        if self.initial_setup:
            self.install_ansible(system_package_manager)
            self.install_openssh_client(system_package_manager)
            self.start_and_enable_sshd()
            self.generate_ssh_keys()

        key_location = str(input("Enter the location of the public ssh key [~/.ssh/<key-name>.pub]: "))
        password_servers = str(input("Enter the ssh password for the servers you want to copy the key to: "))
        self.install_sshpass(system_package_manager)

        # get list of IPs from inventory file and copy defined public key to each defined server
        with open(self.server_ips, 'r') as f:
            for line in f:
                ip = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
                if ip:
                    self.copy_public_key_to_server(ip.group(), key_location, password_servers)

        self.uninstall_sshpass(system_package_manager)

    def check_underlying_package_manager(self):
        """
        checks the underlying package manager to install required software later on
        :return: package manager if found
        """
        check_package_manager = subprocess.call(['which', 'apt'])
        if check_package_manager == 0:
            package_manager = 'apt'
            cprint('Found apt as the underlying package manager!', 'green')
            return package_manager

        check_package_manager = subprocess.call(['which', 'pacman'])
        if check_package_manager == 0:
            package_manager = 'pacman'
            cprint('Found pacman as the underlying package manager!', 'green')
            return package_manager

        check_package_manager = subprocess.call(['which', 'yum'])
        if check_package_manager == 0:
            package_manager = 'yum'
            cprint('Found yum as the underlying package manager!', 'green')
            return package_manager

        cprint('***Error: Neither apt nor pacman nor yum was found! Install a supported package manager!***', 'red')
        print('Exiting...')
        sys.exit(1)

    def install_ansible(self, package_manager):
        """
        install ansible from the official repositories
        :param package_manager: which underlying package manager to use
        """
        if package_manager == 'apt':
            os.system('sudo -S apt install ansible')
        elif package_manager == 'pacman':
            os.system('sudo -S pacman -S ansible')
        elif package_manager == 'yum':
            os.system('sudo -S yum install ansible')

    def install_openssh_client(self, package_manager):
        """
        install openssh client from the official repositories
        :param package_manager: which underlying package manager to use
        """
        if package_manager == 'apt':
            os.system('sudo -S apt install openssh-client')
        elif package_manager == 'pacman':
            os.system('sudo -S pacman -S openssh')
        elif package_manager == 'yum':
            os.system('sudo -S yum install openssh-clients')

    def start_and_enable_sshd(self):
        """
        start and enable ssh service via systemd
        """
        os.system('sudo systemctl enable --now sshd')

    def install_sshpass(self, package_manager):
        """
        install sshpass from the official repositories
        :param package_manager: which underlying package manager to use
        """
        if package_manager == 'apt':
            os.system('sudo -S apt install sshpass')
        elif package_manager == 'pacman':
            os.system('sudo -S pacman -S sshpass')
        elif package_manager == 'yum':
            os.system('sudo -S yum install sshpass')

    def uninstall_sshpass(self, package_manager):
        """
        unistall sshpass
        :param package_manager: which underlying package manager to use
        """
        if package_manager == 'apt':
            os.system('sudo -S apt remove sshpass')
            os.system('sudo -S apt autoremove')
        elif package_manager == 'pacman':
            os.system('sudo -S pacman -Rns sshpass')
        elif package_manager == 'yum':
            os.system('sudo -S yum autoremove sshpass')

    def generate_ssh_keys(self):
        """
        generate ssh keys which ansible requires
        """
        os.system('ssh-keygen')

    def copy_public_key_to_server(self, server_ip, key_loc, server_password):
        """
        copy an existing ssh public key to a server
        :param server_ip: ip of the server the keys are supposed to be copied onto
        :param key_loc: location of the public ssh key
        :param server_password: password of the server(s) you want to copy the public key to
        """
        os.system(f'sshpass - p "{server_password}" ssh-copy-id -i {key_loc} {self.username}@{server_ip}')


if __name__ == '__main__':
    setup = AnsibleSetup('jogi', 'inventory', False)
    setup.setup()

