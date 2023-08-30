def add_keychains(n):
    add=int(input(f"you have {n} keychains how many to add? "))
    keychains=n+add
    print(f"you now have {keychains} keychains\n")
    return keychains
def remove_keychains(n1):
       minus=int(input(f"you have {n1}.how many to remove? "))
       sub=n1-minus
       if sub<0:
            print("error")
            return
       else:
            print(f"you now have {sub} keychains")
       return sub   
def view_order(n2,sales_tax,shipping_cost,keychain_per_shipping):
        print(f"you have {n2} keychains")
        print("keychains cost $10 each")
        total_cost=10*n2
        sales_tax=(total_cost+sales_tax)/100
        shipping_charge=shipping_cost+(n2*keychain_per_shipping)
        total_cost=sales_tax+shipping_charge+total_cost
        print(f"sales tax {sales_tax}")
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
sales_tax=8.25
shipping_cost=5.00
keychain_per_shipping=1.00
while True:
    print("Ye olde keychain shoppe\n")
    print("1) Add keychains to order\n2) Remove keychains from order\n3) view current order\n4) checkout\n")
    one=int(input("enter your choice : "))   
    if one==1:
            n1=add_keychains(n)         
    elif one==2:
            n2=remove_keychains(n1)
    elif one==3:
            n3=view_order(n2,sales_tax,shipping_cost,keychain_per_shipping)
    elif one==4:
            checkout(n1,n3)
        
        
        
        
