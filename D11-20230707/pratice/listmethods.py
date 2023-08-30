#append this list method add the new element in the list
veggies=["carrot","ginger","cabbage","beetroot","tomato","potato","onion"]
veggies.append("broccoli")
print(veggies)

#remove this list method removes the certain element
remove=veggies.remove("ginger")
print(veggies)

#copy() copies the list 
copy=veggies.copy()
print(veggies)
 
#count()
count=veggies.count("cabbage")
print(count)

#extend() add the elements in tha last of the list
veggies.extend("a")
print(veggies)

#index()
index=veggies.index("carrot")
print(index)

#insert()
veggies.insert(0,"rabbit")
print(veggies)