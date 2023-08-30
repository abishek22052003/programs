# def area_of_triangle(a,b,c):
#     s=(a+b+c)/2
#     area=s*(s-a)*(s-b)*(s-c)
#     return area
# a=float(input("length of side a= "))
# b=float(input("length of side b= "))
# c=float(input("length of side c= "))
# result=area_of_triangle(a,b,c)
# print(result)

# def area_of_square():
#     A=a*a
#     return A
# a=int(input("area of square : "))
# check=area_of_square()
# print(check)

# def area_of_rectangle(w,l):
#     A=w*l
#     return A
# w=int(input("enter the width : "))
# l=int(input("enter the length : "))
# check1=area_of_rectangle(w,l)
# print(check1)

# def area_of_circle(radius):
#     circle=3.14*radius*radius
#     return circle
# radius=int(input("enter the radius : "))
# check=area_of_circle(radius)
# print(check)

def area_of_trapezium(a,b,h):
    trapezium=a+b/2*(h)
    return trapezium
a=int(input("enter the value a : "))
b=int(input("enter the value of b : "))
h=int(input("enter the value of h : "))
check=area_of_trapezium(a,b,h)
print(check)


