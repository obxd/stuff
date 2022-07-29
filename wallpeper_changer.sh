#/bin/sh
while true
do
  /bin/ls -d -1 '/home/obxd/Pictures/dark_wallpepers'/* \
    | shuf -n 1 \
    | xargs -I % xwallpaper --maximize '%';
  sleep 10m;
done
