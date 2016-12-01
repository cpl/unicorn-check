# Unicorn Check
###### Quick script that will tell you if you have any unicorns in your code. 🦄
![ulogo](https://img.shields.io/badge/unicorns-0-ff69b4.svg)

### How it works
Using ```python```, the program goes trough the file line by line, encoding each line in ```UTF-8``` and adding the escape char. After that the program performs a ```regex``` search on the entire line, gets the number of matches back and adds it to a total count that is then printed for you at the end.

```
$ python ucheck.py test.txt
You have 4 unicorn/s in your file.
```
