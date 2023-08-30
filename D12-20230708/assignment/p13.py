def answer(qn1):
    if qn1=="animal":
        qn2=input("Question 2) Is it bigger than a breadbox ?\n>")
        if qn2=="no":
            print("my guess is that you are thinking of a mouse.\n I would ask you if i'm right.but i dont actually care")
        else:
            print("wrong")
    elif qn1=="mineral":
        qn2=input("Question 2) Is it bigger than a breadbox ?\n>")
        if qn2=="yes":
            print("my guess is that you are thinking of a truck.\n I would ask you if i'm right.but i dont actually care")
        else:
            print("wrong")
    elif qn1=="vegetable":
        print("wrong answer")
qn1=input("Question 1) Is it animal,vegetable or mineral ?\n>")
check=answer(qn1)



    
        