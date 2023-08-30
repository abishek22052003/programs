"""first=int(input("enter the first number:"))
operator=input("enter the operator:")
last=int(input("enter the last number:"))
def arithmetic_operations(first,operator,last):
    if operator == "+":
        return first+last
    if operator=="-":
            return first-last
    if operator=="*":
        return first*last
    if operator=="%":
        return first%last
    if operator=="**":
        return first**last
        
    
                
check=arithmetic_operations(first,operator,last)
print(check)"""

def operator(first,op,last):
    if op=="+":
        result=first+last
    elif op=="-":
        result=first-last
    elif op=="*":
        result=first*last
    elif op=="%":
        result=first%last
    return result
    
first=int(input("enter the first num:"))
op=input("enter the operator:")
last=int(input("enter the last num:"))
check=operator(first,op,last)
print(check)









