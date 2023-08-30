lists=[{"name":"Vijay","age":21,"place":"Marthandam"},
      {"name":"Abishek","age":30,"place":"kottar"},
      {"name":"Vinusha","age":21,"place":"Ethamozhli"},
      {"name":"Siva Gayathri","age":20,"place":"kottar"},
      {"name":"Vinusha","age":21,"place":"vadasery"}]
def details(lists):
    for list in lists:
        print("I am",list["name"],"I am",list["age"],"years old and I am from",list["place"])
details(lists)
print("\n")
def age(lists):
    for list in lists:
        if list["age"]>21:
            print("I am",list["name"],"I am",list["age"],"years old and I am from",list["place"])
age(lists)

