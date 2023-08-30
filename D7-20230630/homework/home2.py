"""output:
Expected-input: Enter your Age:18
Expected-output: You are eligible to vote

Expected-input: Enter your Age:15
Expected-output: You are not eligible to vote

3.Get a number as an  input from the user and check if the number is odd or even.
"""
age=int(input("enter you age :"))
if(age>=18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")