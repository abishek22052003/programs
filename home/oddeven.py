# # Expected-input: Enter the Number:18
# # Expected-output: 18 is an Even number

# # Expected-input: Enter the Number:5
# # Expected-output: 5 is an Odd number
# num=int(input("enter the number : "))
# if num%2:
#     print("the number is odd")
# else:
#     print("the number is even")
def numbers(num):
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")
num=int(input("enter a number : "))
check=numbers(num)
