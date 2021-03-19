import os
import sys
import subprocess
from termcolor import cprint


class AnsibleSetup:
    def __init__(self, username, server_ip):
        self.username = username
        self.server_ip = server_ip
        self.package_manager = self.check_underlying_package_manager()
        self.install_ansible()
        self.install_openssh_client()
        self.start_and_enable_sshd()
       	self.generate_ssh_keys()
        self.copy_public_key_to_server()

    def check_underlying_package_manager(self):
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

    def install_ansible(self):
        if self.package_manager == 'apt':
            os.system('sudo -S apt install ansible')
        elif self.package_manager == 'pacman':
            os.system('sudo -S pacman -S ansible')
        elif self.package_manager == 'yum':
            os.system('sudo -S yum install ansible')

    def install_openssh_client(self):
        if self.package_manager == 'apt':
            os.system('sudo -S apt install openssh-client')
        elif self.package_manager == 'pacman':
            os.system('sudo -S pacman -S openssh')
        elif self.package_manager == 'yum':
            os.system('sudo -S yum install openssh-clients')

    def start_and_enable_sshd(self):
        os.system('sudo systemctl enable --now sshd')

    def generate_ssh_keys(self):
        os.system('ssh-keygen')

    def copy_public_key_to_server(self):
        key_location = str(input('Enter the location of the newly created ssh key [~/.ssh/<key_name>.pub]: '))
        os.system(f'ssh-copy-id -i {key_location} {self.username}@{self.server_ip}')


if __name__ == '__main__':
    test = AnsibleSetup('<username>', '<server_ip>')
