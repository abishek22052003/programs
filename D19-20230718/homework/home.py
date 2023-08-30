items_list = [
    {"name": "Apple", "category": "Fruits"},
    {"name": "Carrot", "category": "Vegetables"},
    {"name": "Banana", "category": "Fruits"},
    {"name": "Broccoli", "category": "Vegetables"},]
fruit=[]
veggies=[]
for item in items_list:
    category=item["category"]
    name=item["name"]
    if category=="Fruits":
       fruit.append(name)
    if item["category"]=="Vegetables":
        veggies.append(name)
dictionary={"Fruits":fruit,"Vegetables":veggies}
print(dictionary)




        
    

        
