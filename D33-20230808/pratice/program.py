# lists=[100,180,260,310,40,535,695]
# num=0
# for i in range(len(lists)):
#     for j in range(i+1,len(lists)):
#         total=lists[i]-lists[j]
#         value=abs(total)
#         if value>num:
#             num=value
#             a,b=i,j
# print(num,a,b)


# lists=[100,180,260,310,40,535,695]
n=int(input("enter the number of days : "))
num=0
lists=[]
new=0
while num<n:
    days=int(input("enter the amount : "))
    lists+=[days]
    num+=1
    for i in range(len(lists)):
        for j in range(i+1,len(lists)):
            total=lists[j]-lists[i]
            if total>new:
                new=total
                a,b=i,j
print(new,a,b)

  