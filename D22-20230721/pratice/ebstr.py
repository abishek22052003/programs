import json
def eb():
    reading=consumer_data["eb_reading"]
    dictionary_view=[]
    for unit in range(len(reading)-1):
        unit1=reading[unit]
        unit2=reading[unit+1]
        total=unit2-unit1
        month=unit+1
        if total>=100 and total<200:
            rs=2
            amount=total*rs
            diction={"month":month,"units consumed":total,"bill amount":amount}
        elif total>=200:
            rs=5
            amount=total*rs
            diction={"month":month,"units consumed":total,"bill amount":amount}
        dictionary_view.append(diction)
    return dictionary_view
consumer_data = {
    "consumer_name": "user",
    "eb_reading": [1100, 1200, 1350, 1650, 2050]}
check=eb()
string=str(check)
jason=json.dumps(string)
print(jason)
t=type(jason)
# print(t)
# load=json.loads(diction)
# print(load)
def eb():
    reading=consumer_data["eb_reading"]
    dictionary_view=[]
    for unit in range(len(reading)-1):
        unit1=reading[unit]
        unit2=reading[unit+1]
        total=unit2-unit1
        month=unit+1
        if total>=100 and total<200:
            rs=2
            amount=total*rs
            diction={"month":month,"units consumed":total,"bill amount":amount}
        elif total>=200:
            rs=5
            amount=total*rs
            diction={"month":month,"units consumed":total,"bill amount":amount}
        dictionary_view.append(diction)
    return dictionary_view
consumer_data = {
    "consumer_name": "user",
    "eb_reading": [1100, 1200, 1350, 1650, 2050]}
check1=eb()
load=json.loads(check1)
print(load)
