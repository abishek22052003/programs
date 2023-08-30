# output:
# Expected-input: Enter your Age:18
# Expected-output: You are eligible to vote

# Expected-input: Enter your Age:15
# Expected-output: You are not eligible to vote
age=int(input('enter your age : '))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")