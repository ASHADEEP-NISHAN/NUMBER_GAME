import random as r
n=r.randint(1,100)
g=0
while True:
    gs=input("enter a number between 1 to 100")
    g += 1
    try:
        gs=int(gs)
    except:
        print("enter a valid number")
        continue
    if gs==n:
        print(f"congratulation! you guess the nember in {g} guesses")
        break
    elif gs <n :
        print("your guess is short")
    else:
        print("your guess is high")

