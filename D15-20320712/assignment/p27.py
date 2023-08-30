def add_keychains(n):
    add=int(input(f"you have {n} keychains how many to add? "))
    keychains=n+add
    print(f"you now have {keychains} keychains\n")
    return keychains
def remove_keychains(n1):
       minus=int(input(f"you have {n1}.how many to remove? "))
       sub=n1-minus
       print(f"you now have {sub} keychains")
       return sub   
def view_order(n2):
        print(f"you have {n2} keychains")
        print("keychains cost $10 each")
        total_cost=10*n2
        print(f"total cost is {total_cost}")
        return total_cost
def checkout(keychains,total_cost):
        print("CHECKOUT")
        name=input("what is your name? ")
        print(f"you have {keychains} keychains")
        print("keychains cost $10 each")
        print(f"total cost is {total_cost}")
        print(f"thank you for your order {name}")
        exit()
n=0
while True:
    print("Ye olde keychain shoppe\n")
    print("1) Add keychains to order\n2) Remove keychains from order\n3) view current order\n4) checkout\n")
    one=int(input("enter your choice : "))   
    if one==1:
            n1=add_keychains(n)         
    elif one==2:
            n2=remove_keychains(n1)
    elif one==3:
            n3=view_order(n2)
    elif one==4:
            checkout(n1,n3)
        
        
        
        
