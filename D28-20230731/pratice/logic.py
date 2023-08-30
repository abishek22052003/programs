l=[1,5,3,7,9,13]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==10:
            print([i,j])
    break