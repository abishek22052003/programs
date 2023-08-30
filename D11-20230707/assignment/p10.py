name=input("hey! what's your name? (sorry in keep forgetting. )")
age=int(input(f"ok {name} how old are you "))
if age<16:
    print("you cant drive")
elif age>=16 and age<=17:
    print("you can drive but you cant vote")
elif age>=18 and age<=24:
    print("you can vote but you cant rent a car")
elif age>=25:
    print("you can do anything else")