def calculate_elerctricity_bill():
    reading=consumer_data["eb_reading"]
    value1=reading[1]-reading[0]
    value2=reading[2]-reading[1]
    value3=reading[3]-reading[2]
    value4=reading[4]-reading[3]
    value=[value1,value2,value3,value4]
    for i in value:  
        if i<=100 and i<=150:
            total1=i*2
            print("Month 1")
            print("units consumed :",i)
            print("bill amount :",total1)
            print("\n")
        if i>=150 and i<300:
            total2=i*2
            print("Month 2")
            print("units consumed :",i)
            print("bill amount :",total2)
            print("\n")
        if i>=300 and i<400:
            total3=i*5
            print("Month 3")
            print("units consumed :",i)
            print("bill amount :",total3)
            print("\n")
        if i>=400:
            total4=i*5
            print("Month 4")
            print("units consumed :",i)
            print("bill amount :",total4)
            print("\n") 
            total_amount=total1+total2+total3+total4
            print ("Total amount :",total_amount)
consumer_data = {
    "consumer_name": "user",
    "eb_reading": [1100, 1200, 1350, 1650, 2050]}
calculate_elerctricity_bill()
