input_num=[3,2,2,3]
new=[]
for i in input_num:
    if i!=3:
        new=new+[i]
    if i==3:
        new=new+["*"]
print(new)