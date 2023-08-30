num=0
while True:
    number=int(input("Number : "))
    num=num+number
    if number==0:
        exit()
    print(f"the total so far is {num}")