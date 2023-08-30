list=[1,0,3,0,2,0,3]
n=[]
for i in list:
    n=n+[i]
    if i==0:
        n=n+[0]
print(n[0:7])