# find the total cost
def calculated_totalcost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item['price']*item['quantity']
    return total_cost
cart = [
    {'name':'apple','price':0.5,'quantity':4},
    {'name':'banana','price':0.3,'quantity':6},
    {'name':'orange','price':0.7,'quantity':3}
]
total_cost=calculated_totalcost(cart)
print(total_cost)     