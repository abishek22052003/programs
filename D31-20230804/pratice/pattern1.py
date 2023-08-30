# num=int(input("enter the num : "))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")
# for k in range(num-1,0,-1):
#     for h in range(k,0,-1):
#         print("*",end="")
#     print("")

# num=int(input("enter the num : "))
# for i in range(1,num+1):
#     print(i*"*",end="")
#     print("")
# for j in range(num-1,0,-1):
#     print(j*"*",end="")
#     print("")

num=int(input("enter the num : "))
for i in range(1,num*2):
    if i<=num:
        m=i
    else:
        m=(num*2)-i
    for j in range(m):
        print("*",end="")
    print("")