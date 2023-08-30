lists=[{"name":"Raja","email":"raja123@gmail.com","password":"1234","logged-in":"","hobbies":["horse riding","swimming","running"],"friends_list":["pooja,rani,mani"]},
       {"name":"Mohan","email":"mohan123@gmail.com","password":"5678","logged-in":"","hobbies":["browsing","skipping","coding"],"friends_list":["ajay,robin,rohan"]},
       {"name":"Vijay","email":"vijay123@gmail.com","password":"9101","logged-in":"","hobbies":["listening music","gaming","dancing"],"friends_list":["perumal,aswin,mathan"]}]
user_mail=input("Enter your Email : ")
user_password=(input("Enter you password : "))
for list in lists:
    mail=list["email"]
    password=list["password"]
    login=list["logged-in"]
    name=list["name"]
    hobby=list["hobbies"]
    friend=list["friends_list"]
    if user_mail==mail and user_password==password:
        list["logged-in"]=True
        for hob in hobby:
            print(hob,",",end="")
        print("")
        for friends in friend:
            print(friend,",",end="")
    # else:
    #     list["logged-in"]=False
        



              
        