def largest_num(lists):
    larger=lists[0]
    for list in lists:
        if larger<list:
            larger=list
    return larger
lists=[1,100,300,4]
check=largest_num(lists)
print("largest number",check)





# nums=[200,300,400,2]
# def smallest_num(nums):
#     smaller=nums[0]
#     for num in nums:
#         if smaller>num:
#             smaller=num
#     return smaller
# result=smallest_num(nums)
# print("smallest number",result)



    

    