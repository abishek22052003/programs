nums=[2,2,1]
def unique(nums):
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                count=count+1
        if count==1:
            print(nums[i])
unique(nums)


