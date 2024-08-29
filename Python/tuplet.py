# calculate total cost using tuples with loops and zip
def total_cost(items, prices):
    """ This Function will output the total cost of the each items with looping and
    in each looping it will return pair of item and price """
    total_cost = 0
    for item, price in zip(items, prices):
        total_cost += price
        print(f'{item}: ${price}')
    print(f'Total cost: ${total_cost}')

# example function call
items = ['fridge', 'washing_machine', 'electric_pan']
prices = [100.99, 150.99, 52.49]
total_cost(items, prices)
