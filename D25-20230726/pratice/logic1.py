n=int(input("Enter the num : "))   
for i in range((n*n)+1,1,-1):
    print(i,end=" ")
    if i%n==0:
        print("")


# n=int(input("Enter the num : "))   
# for i in reversed(range(1,(n*n)+1)): 
#     if i%n==0:
#         print("")
#     print(i,end=" ")