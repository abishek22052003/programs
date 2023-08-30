monthly_gold_rate=[{"month":"january","gold_rate":1500},{"month":"february","gold_rate":1000},{"month":"march","gold_rate":800},
                   {"month":"april","gold_rate":2500}]
num=monthly_gold_rate[0]["gold_rate"]
monthly=monthly_gold_rate[0]["month"]
for rate in monthly_gold_rate:
    month_rate=rate["gold_rate"]
    if month_rate<num:
        num=month_rate
        monthly=rate["month"]
print(num,monthly)

