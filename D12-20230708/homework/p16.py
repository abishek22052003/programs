gender=input("what is your gender(M/F)? ")
def information(gender):
    fname=input("first name : ")
    lname=input("last name : ")
    age=int(input("age : "))
    if gender=="M":
        if age>=20:
            work=input("are you working uncle: ")
            if work==work:
                print("then i shall call you Mr.",fname,lname)
        else:
                print("then i shall call you ",fname,lname)
    if gender=="F":
        if age>=20:
            work=input("are you married(y/n): ")
            if work=="y":
                print("then i shall call you Mrs.",fname,lname)
            elif work=="n":
                 print("then i shall call you Ms.",fname,lname)
        else:
                print("then i shall call you ",fname,lname)
result=information(gender)