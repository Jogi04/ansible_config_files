# Ansible
This repository consists of personal Ansible playbooks for configuring servers and workstations.

# Requirements
- Ansible package is installed locally
- User "ansible" is present on the remote host(s)
- Remote user "ansible" has root privileges without entering a password
- Public key is present on the remote host(s)

# Usage
1. Add remote host(s) to inventory file and create <remote_ip>.yml file in host_vars and set the variables for the host(s).
3. Run "ansible-playbook main.yml --tags base" to install base configs.
4. Run "ansible-playbook main.yml --tags server" to install server configs if remote host is intended to run as a server.
5. Run "ansible-playbook main.yml --tags workstation" to install workstation configs if remote host is intended to run as a workstation.
