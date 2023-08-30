consumer_data = {
    "consumer_name": "user",
    "eb_reading": [1100, 1200, 1350, 1650, 2050]}
reading=consumer_data["eb_reading"]
dictionary_view={}
for unit in range(len(reading)-1):
    unit1=reading[unit]
    unit2=reading[unit+1]
    total=unit2-unit1
    if total<100:
        print("no amount to pay")
    if total>=100 and total<200:
        print("month 1")
        print("units consumed ",total)
        print("total amount",total*2)
        print("\n")
    if total>=200 and total<300:
        print("month 2")
        print("units consumed ",total)
        print("total amount",total*5)
        print("\n")
    if total>=300 and total<400:
        print("month 3")
        print("units consumed ",total)
        print("total amount",total*5)
        print("\n")
    if total>=400:
        print("month 4")
        print("units consumed ",total)
        print("total amount",total*5)
        print("\n")




        