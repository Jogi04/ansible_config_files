## Setup

### Control Host Setup
Run the following command to set up the Ansible Control Host:
```bash
sudo ./ansible_control_host_setup.sh
```

### Server Setup
Run the following commands on the server to set up prerequisites on the server which is intended to be configured:
```bash
sftp jogi@10.0.0.100:/home/jogi/ansible_config_files/ansible_server_setup.sh ~
sudo ./home/jogi/ansible_server_setup.sh
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
ansible-playbook main.yml --tags arch_install
```
