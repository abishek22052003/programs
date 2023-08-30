name=input("what's your name ? ")
age=int(input("ok"f"{name}, how old are you ? "))
if age<16 :
    print("you cant drive" f"{name}")
elif age<18:
    print("you cant vote", name)
elif age<25:
    print("you cant rent a car", name)
else:
    print("you cant do anything thats legal")
