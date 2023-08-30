quiz=input("are you ready for the quiz ? (Y/N) ")
if quiz=="Y":
    print("okay here it is comes\n")
elif quiz=="N":
    exit()
sum=0
qn=int(input("Q!) what is the capital of alaska? \n\t1)Melbourne\n\t2)Anchorage\n\t3)Juneau\n> " ))
if qn==3:
    print("thats right")
    sum=sum+1
else:
    print("wrong")
qn1=int(input(("can you store the value cat in a variable of type int? \n\t1)yes\n\t 2)no\n> ")))
if qn1==1:
    print("sorry" "cat" "is a string.ints can only store number")
if qn1==2:
    print("no")
    sum=sum+1  
qn2=int(input("what is the result of 9+6/3?\n\t1)5\n\t2)11\n\t3)15/3\n> "))
if qn2==2:
    print("thats correct")
    sum=sum+1 
else:
    print("wrong")
print(f"overall you got {sum} out of 3 correct.\nthanks for playing")



