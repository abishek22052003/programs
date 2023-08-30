weight=float(input("enter your current earth weight : "))
print("I have information for the following planet:\n\t1.venus  2.mars  3,jupiter\n\t4.saturn  5.uranus  6.neptune")
planet=int(input("which planet you are visiting ? "))
if planet==1:
    calc=weight*0.78 
elif planet==2:
    calc=weight*0.39
elif planet==3:
    calc=weight*2.65
elif planet==4:
    calc=weight*1.17
elif planet==5:
    calc=weight*1.05
elif planet==6:
    calc=weight*1.23li

print("your weight would be",calc,"pounds on the planet")




