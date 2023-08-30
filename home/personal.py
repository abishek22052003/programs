def personal_det(lists):
    for list in lists:
        print("i am ",list["name"],"my age ",list["age"])
    if list["age"]>21:
            print(list["name"])

lists=[{"name":"Vijay","age":21,"place":"Marthandam"},
      {"name":"Abishek","age":30,"place":"kottar"},
      {"name":"Vinusha","age":21,"place":"Ethamozhli"},
      {"name":"Siva Gayathri","age":20,"place":"kottar"},
      {"name":"Vinusha","age":21,"place":"vadasery"}]
personal_det(lists)


