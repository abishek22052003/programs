"""Expected-input:
Enter your name : Jhon
Enter your age : 23
Enter your DOB : 18-02-2000
Enter your location : United Kingdom
Enter your college name : cambridge university


Expected-output:"
Hello, my name is Jhon. I am 23 years old and was born on 18-02-2000.
Currently, I am located in United Kingdom and i completed my degree at cambridge university"
"""
name=str(input("enter your name :"))
age=int(input("enter your age :"))
dob=input("enter your dob :")
location=input("enter your location :")
college=input("enter your college name :")
print("hello,my name is ",name,".i am",age,"years old and was born on",dob,".currently, I am located in ",location,"and i completed my degree at",college)
