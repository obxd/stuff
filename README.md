# Scripts.  
*image-show.py* - show image on terminal using ueberzug lib.

*bouncing_char* - bouncing char using curses.

# command-line gems.  
---

## General

### "!!" grabs the last run command.
for example  
```sh
sudo !! # Run the last command as root
```

### Extract tarball from internet without local saving
```sh
wget -qO - "http://www.tarball.com/tarball.gz"  | tar zxvf -
```

### Serve current directory tree at http port 8000
```sh
python -m http.server 8000
```

### Show $PATH sorted with unique coun
```sh
echo $PATH | sed 's/:/\n/g' | sort | uniq -c
```
### Random cooooolooooored cowsay smart stuf

```sh
bullshit | cowsay -f $(ls /usr/share/cows/|shuf -n 1) | lolcat
```
*note:* Requires cowsay lolcat bullshit.

### Pip update my stuff (user stuf
```sh
pip freeze --user | cut -d= -f1 | xargs pip install --user -U
```

### Calculate days on which Friday the 13th occurs
```sh
for i in {2021..2025}-{01..12}-13; do [[ $(date --date $i +"%u" | grep 5) != 5 ]] || echo "$i Friday the 13th"; done
```

### Compare two directorys
```sh
diff <(cd dir1 && find | sort) <(cd dir2 && find | sort)
```
 
### Make dir and cd into i
```sh
mkdir foo && cd $_
```
---
## yay / pacman
### Remove unrequired deps
```sh
pacman -Rsn $(pacman -Qdtq)
```
```sh
yay -Rsn $(yay -Qdtq)
```

### Print 20 last installed/updated packages
```sh
expac --timefmt='%Y-%m-%d %T' '%l\t%n' | sort | tail -n 20
```
*note:* Requires expac.  

