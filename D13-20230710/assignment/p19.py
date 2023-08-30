import random
def hilo():
    num=random.randint(1,100)
    guess=0
    while guess<7:
        guess=guess+1
        qn=int(input("Guess the number : "))
        if qn<num:
            print("sorry you are too low")
        elif qn>num:
            print("sorry you are too high")
        else:
            print("you guessed it correct")
            exit()
    print("you did'nt guess it in 7 tries. You lose.")
    print("the correct number is",num )
hilo()