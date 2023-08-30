from pprint import pprint
monthly_gold_rate=[{"month":"january","gold_rate":1500,"jewel_list":[{"name":"chain","making_cost":12
                                                                      },{"name":"ring","making_cost":6}]},
                   {"month":"february","gold_rate":1000,"jewel_list":[{"name":"chain","making_cost":10
                                                                      },{"name":"ring","making_cost":5}]},
                   {"month":"march","gold_rate":800,"jewel_list":[{"name":"chain","making_cost":8},
                                                                 {"name":"ring","making_cost":4}]},
                   {"month":"april","gold_rate":2500,"jewel_list":[{"name":"chain","making_cost":16},
                                                       {"name":"ring","making_cost":8}]}]
my_list=[]
dictionary={}
for month in monthly_gold_rate:
    month_per=month["month"]
    gold=month["gold_rate"]
    cost=month["jewel_list"]
    dictionary["month"]=month_per
    dictionary["gold_rate"]=gold
    for calc in cost:
        making=calc["making_cost"]
        name=calc["name"]
        add=(making)/100
        percentage=gold*add
        total=gold+percentage
        dictionary[name]=total
    my_list.append(dictionary)
    dictionary={}    
pprint(my_list)
        
        
    
     
        
        
