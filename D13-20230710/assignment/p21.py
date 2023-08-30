weight=float(input("Your weight in kg : "))
height=float(input("your height in m : "))
bmi=weight/(height**2)
print("Your BMI is",bmi)
if bmi<18.5:
    print("underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("normal weight")
elif bmi>=25.0 and bmi<=29.9:
    print("overweight")
elif bmi>=30.0:
    print("obese")
