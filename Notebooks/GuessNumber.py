import sys
from random import randint


def play(first,last):
    fix_num = randint(first,last)
    
    guess_num = int(input("Guess the number :"))
    
    guessed_right = True
    while guess_num!=fix_num :
        if guess_num > fix_num :
            print("oh try lower")
        elif guess_num < fix_num :
            print("oh try higher")
    
        inp = input("Enter number to continue :) ")
        if not inp:
            guessed_right = False
            break
        else:
            guess_num = int(inp)
    
    if guessed_right:
        print(f"Great yes it is {fix_num}")
    else:
        print(f"Thanks for playing, ans is : {fix_num}")

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        first = 1
        last = 100
    elif len(sys.argv) == 2:
        num = int(sys.argv[1])
        first = min(1,num)
        last = max(num,100)
    else:
        first = int(sys.argv[1])
        last = int(sys.argv[2])
    play(first,last)


    




    