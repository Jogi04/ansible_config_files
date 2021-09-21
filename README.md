## Setup

### Control Host Setup
Clone the github repository:
```bash
git clone https://github.com/Jogi123/ansible_config_files.git
```
Navigate into the root of the repository and run the following command to set up the Ansible Control Host:
```bash
sudo ./ansible_control_host_setup.sh
```

### Server Setup
Download setup script, make it executable and run it as root to set up prerequisites on the server which is intended to be configured:
```bash
wget https://raw.githubusercontent.com/Jogi123/ansible_config_files/master/ansible_server_setup.sh
chmod +x ansible_server_setup.sh
sudo ./ansible_server_setup.sh
```
---

## Usage

### Requirements
Add host ip to inventory file and create <host_ip>.yml file in host_vars and set the variables for the host.

### Base Role
```bash
ansible-playbook main.yml --tags base
```

### Server Role
```bash
ansible-playbook main.yml --tags server
```

### Workstation Role
```bash
ansible-playbook main.yml --tags workstation
```

### Arch Installation Role
```bash
ansible-playbook main.yml --tags arch_linux_install
```
