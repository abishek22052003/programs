"""Expected-output:"Hello, my name is Jhon. I am 23 years old and was born on 18-02-2000. 
Currently, I am located in United Kingdom and i completed my degree at cambridge university"""
name=input("enter your name : ")
age=int(input("enter your age : "))
dob=input("enter your data birth : ")
location=input("your current locatiom ? ")
college=input("where you completed your degree ? ")
print(f"hello my name is{name}. I am {age} years old and was born on {dob}. Currently, I am located in {location} and i completed my degree at {college}.")