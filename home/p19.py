import random
def correct():
    num=random.randint(1,100)
    guess=0
    while guess<7:
        guess=guess+1
        qn=int(input("guess the num : "))
        if qn<num:
            print("you are too low")
        if qn>num:
            print("you are too high")
        if qn==num:
            print("correct")
            break
    print("correct num",num)
    print("you ran out of guesses")
correct()
