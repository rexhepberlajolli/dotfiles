xrandr --setprovideroutputsource modesetting NVIDIA-0
xrandr --auto
[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources
export TERMINAL=rxvt-unicode
exec i3 > ~/.i3.log 2>&1
