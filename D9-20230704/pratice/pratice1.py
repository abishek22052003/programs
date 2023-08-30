#list
name_lists=["vijay","ranjith","abishek","vinusha","siva gayathri","shalini"]
print(name_lists)
#set
name_set={"vijay","ranjith","abishek","vinusha","siva gayathri","shalini"}
print(name_set)
#find my name in the list
my_name=name_lists[2]
print(my_name)
#any_name=name_set[2]
#print(any_name)
#slicing
#slicing in list
first_four_names=name_lists[0:3]
print(first_four_names)
#slicing in string
letter="karka"
slce=letter[0:4]
print(slce)
#using index in list
# print(name_lists[0])
# print(name_lists[1])
# print(name_lists[2])
# print(name_lists[3])
# print(name_lists[4])
# print(name_lists[5])
#for 
#letters here is to represent the names in the name_lists
for letters in name_lists:
     print(letters.upper())
     print(letters.capitalize())
     print(letters.count('a'))
     print("my name is",letters)
     print(letters.lower())
# for i,letters in enumerate(name_lists):
#     if(i<3):
#         print(letters)
#     else:
#         break
          

