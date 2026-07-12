#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
alias reload='source ~/.bashrc'   # or ~/.zshrc if you use zsh

PS1='[\u@\h \W]\$ '

ex () {
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1     ;;
      *.tar.gz)    tar xzf $1     ;;
      *.bz2)       bunzip2 $1     ;;
      *.rar)       unrar x $1     ;;
      *.gz)        gunzip $1      ;;
      *.tar)       tar xf $1      ;;
      *.tbz2)      tar xjf $1     ;;
      *.tgz)       tar xzf $1     ;;
      *.zip)       unzip $1       ;;
      *.Z)         uncompress $1  ;;
      *.7z)        7z x $1        ;;
      *.deb)       ar x $1        ;;
      *.tar.xz)    tar xf $1      ;;
      *.tar.zst)   unzstd $1      ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

note() {
  echo "$(date): $*" >> ~/"note_$(date +%Y-%m-%d).txt"
}

up() {
  local d=""
  for ((i=1; i<=${1:-1}; i++)); do
    d="../$d"
  done
  cd "$d"
}

# navigation
alias ..=   'cd ..'
alias ...=  'cd ../..'
alias ....= 'cd ../../..'

alias la='ls -A --color=auto'
# ecosystem
alias siddown='sudo pacman -Syu && shutdown -h now'

# grep
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

#git
alias addup='git add -u'
alias addall='git add .'
alias branch='git branch'
alias checkout='git checkout'
alias commit='git commit -m'
alias fetch='git fetch'
alias pull='git pull origin'
alias push='git push origin'
alias status='git status'
alias tag='git tag'
alias newtag='git tag -a'

# adding flags
alias rm='rm -i'                                  # confirm before deleting
alias mv='mv -i'                                  # confirm before overwriting
alias cp="cp -i"                                  # confirm before overwriting something
alias df='df -h'                                  # human-readable sizes
alias free='free -m'                              # show sizes in MB
alias lynx='lynx -cfg=~/.lynx/lynx.cfg -lss=~/.lynx/lynx.lss -vikeys'

# info
alias h='history'
alias ports='netstat -tulanp'
alias path='echo -e ${PATH//:/\\n}'               # print your PATH one entry per line
alias myip='curl ifconfig.me'                     # show your public IP
