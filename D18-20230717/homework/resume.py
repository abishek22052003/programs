my_resume={"name":"Abishek","E-mail":"abi@gmail.com","mobile_no":9345558020,
            "soft_skills":["negotiating","critical thinking","work ethic"],
            "hard_skills":["programing skills","project management","book keeping"],
            "education_qualification":[{"level":"sslc","school":"DVD matric school","percentage":80,"mark":420},
            {"level":"hsc","school1":"SLB government school","percentage":70,"marks":405},
            {"level":"institute","college":"S.T.hindu college","percentage":80,"university":"manonmaniam sundaranar university"}],
            "projects":"Naan mudhalvan project","experience":[{"company_name":"capestart","role":"software developer","place":"nagercoil","duration":1},
            {"company_name":"kabb wings","role":"block chain developer","place":"nagercoil","duration":2},
            {"company_name":"AK infopark","role":"data scientist","place":"nagercoil","duration":1}],
            "hobbies":["dancing","intsrument playing","browsing"],
            "personal_details":{"father name":"C.Murugesan","father_occupation":"mechanic",
            "language_known":["tamil","hindi","english"],"DOB":"22-05-2003","gender":"male",
            "martial status":"single","address":{"door no":"39G/3","street":"chenthooran nagar","place":"nagercoil","pincode":629002}}}
print(my_resume["personal_details"]["language_known"][2])
# educate=my_resume["education_ qualification"]
# print(educate)
# for i in educate:
#     print(i["level"])
# educate=my_resume["education_qualification"]
# for resume in educate:
#     print(resume["percentage"])
g=my_resume["personal_details"]["address"]
print(g)
for i in g:
    if i=="pincode":
        print(g[i])

# home=details["address"]
# for key in home:
#     if key=="pincode":
#         print(home[key])
# print(my_resume.values())
# print(my_resume.keys())
# print(my_resume.items())

# print(details.values())
# educate=my_resume["education_qualification"]
# for i in educate:
#         if i==["level":"sslc"]:
#             print(i["percentage"])
    







