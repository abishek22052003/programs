# import string
# user=input("enter the password : ")
# def gen_password(user):
#     if len(user)<6:
#         return "weak password "
#     lower=string.ascii_lowercase
#     upper=string.ascii_uppercase
#     num=string.digits
#     symbols=string.punctuation
#     all=lower+upper+num+symbols
#     if not all:
#         return "password must contain atleast onen uppercase and lowercase and digits"
#     if len(user)>=6 and len(user)<=10:
#         return "moderate passoword"
#     if len(user)>=11 and len(user)<15:
#         return "strong password"
#     if len(user)>=15:
#         return "very strong password"    
# print(gen_password(user))

password=input("Enter the password: ")

def pwd(password):
    if len(password) < 6:
        return "Weak password, Try another password"
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for i in password:
        if i.isupper():
            has_uppercase=True
        if i.islower():
            has_lowercase=True
        if i.isdigit():
            has_digit=True
    if not (has_uppercase and has_lowercase and has_digit):
        return "Password must contain atleast one upper case letter, one lower case letter and one digit"
    if len(password) >=6 and len(password) <=10:
        return "Moderate password"
    elif len(password) >=11 and len(password) <15:
        return "Strong password"
    elif len(password) >=15:
        return "Very strong password"
    else:
        return "Very strong password"
    
print(pwd(password))