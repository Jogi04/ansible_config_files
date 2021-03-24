# Lines configured by zsh-newuser-install

# manually installed zsh plugins
source ~/.zsh-plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/.zsh-plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.zsh-plugins/zsh-completions/zsh-completions.plugin.zsh

# manually installed themes
source ~/.zsh-themes/gnzh/gnzh.zsh-theme

HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/jogi/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
#
# Prompt ZSH
autoload -Uz promptinit
promptinit

alias ls='ls --color=auto'
alias ll='ls -l'
alias la='ls -a'
alias lla='ls -la'
alias pi='ssh ubuntu@192.168.178.48'
alias rsync_backup='cd /home/jogi/programming/python/fun_projects/; python arch_backup_rsync.py'
alias usb_backup='cd /home/jogi/programming/python/fun_projects/; python arch_backup_usb.py; cd ~'
alias maintenance='bash /home/jogi/programming/github/arch_install/maintenance/maintenance.sh'
