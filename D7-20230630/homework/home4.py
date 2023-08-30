item1=int(input("enter the amount of item1 :"))
item2=int(input("enter the amount of item2 :"))
item3=int(input("enter the amount of item3 :"))
item4=int(input("enter the amount of item4 :"))
add=item1+item2+item3+item4 
if (add>=500 and add<=1000):
    print("you have owned a silver token")
if(add>1000):
    print("you have owned a golden token")
if(add<500):
    print("you have owned no token")