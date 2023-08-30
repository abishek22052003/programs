def planets(visiting):
    if visiting==1:
        calc=weight*0.78
    elif visiting==2:
        calc=weight*0.39
    elif visiting==3:
        calc=weight*2.65
    elif visiting==4:
        calc=weight*1.17
    elif visiting==5:
        calc=weight*1.05
    elif visiting==6:
        calc=weight*1.23
    return calc
weight=int(input("please enter your current earth weight : "))
print("I have information for the following planets:\n\t1)venus  2)mars  3)jupiter\n\t4)saturn  5)uranus  6)neptune")
visiting=int(input("which planet you are visiting ? "))
check=planets(visiting)
print(f"your wieght should be {check} on the planet ")
