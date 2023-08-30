days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
new=[]
total_days=range(1,31)
for day in days:
    for i in total_days:
        if day=="monday":
            new=new+[i]
print(new)


