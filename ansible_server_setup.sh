#!/bin/bash


useradd -m -s /bin/bash ansible
passwd ansible
touch /etc/sudoers.d/ansible
echo 'ansible ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/ansible

apt install openssh-server -y
systemctl start sshd
systemctl enable sshd

mkdir /home/ansible/.ssh
cat << EOF >> /home/ansible/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCpGmT8qDe8h2how2LQ3hRiqXRVQVgsyhkfFRuL6EOW0kMQmVBdP0erbom01hls21VKWwQquqUAiZqve+BYT/ov1k070A7gaGKQdDG8avZzSC1az0SQZOmpA7jl3hceO8kFQJSA2M54c91lb+DkUsNFpUokp6w1wEAUW1Gh28b1xxWbRpvv9Dd66nwI8bv8uNMGGSgJy+mUJpnNHEP5efDLIeJnz2OeTUbnrJmDQb3jUG+dfT2KVq8MTfuf4AzX8W8Fkx0Q8AJsLEF/Cwgv5I1px2kTpbdJrANMcSxK3dLIzri6f5IS8/VCaLpMzFZL/PtvkPotoyKZbdlKUyDDpdRNRpRVpjiexFRkD2sLS0nHUwSM9fQln2v9PLcj7XhdtXDf7WH327LXoCp6atX06/OiUj5NabgX7Xww6BwvRm1lFqvxYoSRW8uJEonWDYyWjJfv5oU5FtX0cAAxEp3mqsDsR2/+MbhGpzqfkLPV8XdptW89sax4rMrtMW01Rg2+OB8= ansible@ansible
EOF
chmod 744 -R /home/ansible/.ssh/
chown -R ansible:ansible /home/ansible/.ssh/
