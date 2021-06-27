# Scripts.  
*image-show.py* - show image on terminal using ueberzug lib.


# command-line gems.  
---

## General
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

