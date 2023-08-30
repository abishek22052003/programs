nums=[2, 5, 8, 1, 9, 3, 7]
num=0
new=0
# a,b=0,0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        total=nums[i]-nums[j]
        value=abs(total)
        if value>new:
            new=value
            # a,b=num[i],num[j]
print(new)
            


            
