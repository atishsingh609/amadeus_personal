"""
stock_name price
apple       100
apple       200
apple      300

output:

if n = 2
apple [150, 250]

if n =3
apple [200]


input = [100, 200, 300, 400]
"""
def calculate_moving_average(stock_prices, no_of_days):

    res = []
    s = 0
    cur_price = 0
    for i in range(len(stock_prices)):
        cur_price += stock_prices[i]
        if i - s + 1 == no_of_days:
            res.append(cur_price / no_of_days)
            cur_price -= stock_prices[s]
            s +=1
    return res

print(calculate_moving_average([100, 200, 300, 400, 600, 800], 3))




