logo=""" ██████  ██    ██ ███████ ███████ ███████     ████████ ██   ██ ███████     ███    ██ ██    ██ ███    ███ ██████  ███████ ██████  
██       ██    ██ ██      ██      ██             ██    ██   ██ ██          ████   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██ 
██   ███ ██    ██ █████   ███████ ███████        ██    ███████ █████       ██ ██  ██ ██    ██ ██ ████ ██ ██████  █████   ██████  
██    ██ ██    ██ ██           ██      ██        ██    ██   ██ ██          ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██ 
 ██████   ██████  ███████ ███████ ███████        ██    ██   ██ ███████     ██   ████  ██████  ██      ██ ██████  ███████ ██   ██ 
"""
print(logo)
import random as r
n=r.randint(1,100)
level=input("Choose A Level EASY/HARD\n").lower()
g=0
if level=='hard':
    g=5
else:
    g=10
ng=0
print("I AM THINKING A NUMBER BETWEEN 1 TO 100\nHOPE YOU ARE ABLE TO GUESS IT")
while g>0:
    print(f"you have {g} number of attempt to guess the number")
    gs=int(input("MAKE A GUESS:"))
    g -= 1
    ng+=1
    if gs==n:
        print(f"congratulation! you guess the number in {ng} guesses")
        exit()
    elif gs <n :
        print("your guess is short")
    else:
        print("your guess is high")
print("YOU LOST")