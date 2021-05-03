# Ansible
personal Ansible configurations and playbooks

# Usage:
1. Make sure ansible is setup properly: Ansible is installed locally, the user "ansible" is present on remote server, "ansible" has sudo privileges and ssh public key is present on remote host for "ansible".
2. Add remote host to inventory file and create <remote_ip>.yml file in host_vars and set the variables for this host.
3. Run "ansible-playbook main.yml --tags base" to install base configs.
4. Run "ansible-playbook main.yml --tags server" to install server configs if remote host is intended to be a server.
5. Run "ansible-playbook main.yml --tags workstation" to install workstation configs if remote host is intended to be a workstation.
