def fandv(items_list):
    for item in items_list:
        category=item["category"]
        fruits=item["name"]
        if category=="Fruits":
            fruity.append(fruits)
        if category=="Vegetables":
            veggy.append(fruits)
    return fruity,veggy
items_list = [{'name': 'Apple', 'category': 'Fruits'},
    {'name': 'Carrot', 'category': 'Vegetables'},
    {'name': 'Banana', 'category': 'Fruits'},
    {'name': 'Broccoli', 'category': 'Vegetables'},]
fruity=[]
veggy=[]
fandv(items_list)
dictionary={"fruits":fruity,"vegetables":veggy}
print(dictionary)


# items_list = [
#     {'name': 'Apple', 'category': 'Fruits'},
#     {'name': 'Carrot', 'category': 'Vegetables'},
#     {'name': 'Banana', 'category': 'Fruits'},
#     {'name': 'Broccoli', 'category': 'Vegetables'},
# ]
# dictionary=[]
# def itemlist(items_list):
#     for item in items_list:
#         category=item["category"]
#         name=item["name"]
#         if category=="Fruits":
#             dictionary.append(name)
#         else:
#             dictionary.append(name)
# itemlist(items_list)
# c={"vv":dictionary}
# print(c)

