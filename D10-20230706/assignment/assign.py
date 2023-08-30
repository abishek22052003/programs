nums=[1,2,3,4,5,6,7,8,9,10]
print(nums)
sum=0
for num in nums:
    #print("before",sum)
    sum=sum+num
    #print("after",sum)
# avg=sum/len(nums)
# print(avg)
print(sum)
print(len(nums))
# n=len(nums)
# print(n)
# avg=sum/n
# print(avg)
avg=sum/len(nums)
print(avg)

costs=[500,200,700,1000]
empty_list=[]
for cost in costs:
    string=str(cost)
    # print("INR "+string)
    empty_list.append("INR "+string)
print(empty_list)
    







    
