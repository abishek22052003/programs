def add_keychains():
        print("ADD KEYCHAINS")
def remove_keychains():
        print("REMOVE KEYCHAINS")
def view_order():
        print("VIEW ORDER")
def checkout():
        print("CHECKOUT")
print("Ye olde keychain shoppe\n")
print("1) Add keyvhains to order")
print("2) Remove keychains from order")
print("3) view current order")
print("4) checkout\n")    
one=int(input("enter your choice : ")) 
if one==1:
        add_keychains()
elif one==2:
        remove_keychains()
elif one==3:
        view_order()
elif one==4:
        checkout()
        
        
        
        
