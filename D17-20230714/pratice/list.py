rows=[{"name":"abishek","place":"kottar","hobbies":["listn music","movies","browsing"]},
{"name":"vijay","place":"marthandam","hobbies":["music","movies","cricket"]},
{"name":"vinusha","place":"ethamozhi","hobbies":["listening", "music,movies","playing"]},
{"name":"siva gaythri","place":"kottar", "hobbies":["dancing","movies","cricket"]},
{"name":"shalini","place":"vadasery","hobbies":["drawing","music","friends"]}]
# for row in rows:
#      print(row)
# print(rows[0])
# names={"name":"abi","place":"kottar"}
# print(names["name"])
# print(rows[2]["hobbies"])
l=[]
for row in rows:
    h=row["hobbies"]
    l.append(h)
print(l[3][0:2])