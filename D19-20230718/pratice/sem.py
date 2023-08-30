education_details=[{"study":"B.com","institute":"cape",
                    "sem_marks":[{"semester_name":1,"subjects":"commerce,accounts","sem_grade":"O"},
                                 {"semester_name":2,"subjects":"marketing,Audit","sem_grade":"B"}]},
                    {"study":"Bsc.comp.science","institute":"Manonmaniam",
                     "sem_marks":[{"semester_name":1,"subjects":"computer architecture,big data","sem_grade":"A",},
 
                                 {"semester_name":2,"subjects":"cloud computing,multimedia","sem_grade":"S"}]}]
l=[]
for i in education_details:
    j=i["sem_marks"]
    for c in j:
        g=c["sem_grade"]
        for h in g:
            l.append(h)
a={"sem grsde":l[3]}
print(a)
            