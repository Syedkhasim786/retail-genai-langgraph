def optimize_price(cost, competitor_price, demand, stock):
    if demand == "high" and stock == "low":
        return competitor_price + 5
    elif demand == "low":
        return cost + 2
    else:
        return competitor_price
