# nums=[[1,2],[3,4]]
# first_list=nums[0]
# second_list=nums[1]
# for i in range(len(first_list)-1):
#     for j in range(i+1,len(first_list)):
#         first=first_list[i]+first_list[j]
# for k in range(len(second_list)-1):
#     for h in range(i+1,len(second_list)):
#         second=second_list[i]+second_list[j]
# print(first+second)


nums=[[1,2],[3,4]]
new=0
new_string=[]
qn=input("enter the operation : ")
for i in (nums):
    for j in range(len(i)):
        if qn=="add":
            new=new+i[j]
        elif qn=="string":
            new_string=new_string+[i[j]]
            string=str(new_string)
if qn=="add":
    print(new)
else:
    print(new_string)


    