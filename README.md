# Scripts.  
*image-show.py* - show image on terminal using ueberzug lib.


# command-line gems.  
---

## General

*"!!" grabs the last run command.*  
for example  
```sh
sudo !! # Run the last command as root
```

*Extract tarball from internet without local saving*  
```sh
# 1st opt:
wget -qO - "http://www.tarball.com/tarball.gz"  | tar zxvf -
# 2nd opt:
curl http://tarball.com/tarball.gz | tar xz
```

*Serve current directory tree at http port 8000*  
```sh
python -m http.server 8000
```

*Show $PATH sorted with unique count*  
```sh
echo $PATH | sed 's/:/\n/g' | sort | uniq -c
```
*Random cooooolooooored cowsay smart stuff*  

```sh
bullshit | cowsay -f $(ls /usr/share/cows/|shuf -n 1) | lolcat
```
*note:* Requires cowsay lolcat bullshit.  

*Pip update my stuff (user stuff)*
```sh
pip freeze --user | cut -d= -f1 | xargs pip install --user -U
```

*Calculate days on which Friday the 13th occurs*  
```sh
for i in {2021..2025}-{01..12}-13; do [[ $(date --date $i +"%u" | grep 5) != 5 ]] || echo "$i Friday the 13th"; done
```
---
## yay / pacman
*Remove unrequired deps:*  
```sh
pacman -Rsn $(pacman -Qdtq)
# also work for yay
yay -Rsn $(yay -Qdtq)
```
explanation:   
* -Q -> query.  
-d -> deps.  
-t -> unrequired.  
-q -> quiet.  
* -R -> Remove.  
-s -> recursive.  
-n -> nosave.  


*Print 20 last installed/updated packages:*  
```sh
expac --timefmt='%Y-%m-%d %T' '%l\t%n' | sort | tail -n 20
```
*note:* Requires expac.  

