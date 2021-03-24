# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

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

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

alias ls='ls --color=auto'
alias ll='ls -l'
alias la='ls -a'
alias lla='ls -la'
alias pi='ssh ubuntu@192.168.178.48'
alias rsync_backup='cd /home/jogi/programming/python/fun_projects/; python arch_backup_rsync.py'
alias usb_backup='cd /home/jogi/programming/python/fun_projects/; python arch_backup_usb.py; cd ~'
alias sync_arch_install='bash /home/jogi/programming/bash/git_sync/sync_arch_install.sh'
alias sync_debian_install='bash /home/jogi/programming/bash/git_sync/sync_debian_install.sh'
alias sync_python_repo='bash /home/jogi/programming/bash/git_sync/sync_python.sh'
alias maintenance='bash /home/jogi/programming/git/arch_install/maintenance/maintenance.sh'

