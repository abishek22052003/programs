
passed_out_yr=int(input("which year you passed out from college :"))
print(passed_out_yr)
#example line type_of_passed_out_year=type(passed_out_yr)
#print(type_of_passed_out_year)
#int_passed_out_year=int(passed_out_yr)
eligible=passed_out_yr > 2021
if eligible:
    print("you are eligible")
else:
    print("you are not eligible")