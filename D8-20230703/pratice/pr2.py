yr=int(input("enter your year:"))
def eligible_yr(yr):
    if yr >=2021:
        return "you are eligible"
    else:
        return "you are not eligible"
    
check=eligible_yr(yr)
print(check) 
    