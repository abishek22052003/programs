dup_val=[1,2,3,2,5,1,5]
new_val=[]
for num in dup_val:
    if num not in new_val:
        new_val.append(num)
print(new_val)