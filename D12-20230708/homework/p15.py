def things(question1):
    if question1=="outside":
        question2=input("QUESTION 2)Is it a living thing? ")
        if question2=="yes":
            print("then  what else could you be thinking of besides a python?!?")
        else:
            print("not alive")
    elif question1=="inside":
        print("is it houseplant")
    elif question1=="both":
        print("is it a dog")
print("TWO MORE QUESTIONS BABY\n")
print("Think of something and I'll try it!\n")
question1=input("QUESTION 1) Does it stay inside or outside or both? ")
check=things(question1)