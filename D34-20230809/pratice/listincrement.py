#adding  the numbers in the list
digits=[4,9,9,9]
num=""
empty=[]
for i in digits:
    num=num+str(i)
a=int(num)+1
b=str(a)
for j in b:
    empty.append(int(j))
print(empty)

