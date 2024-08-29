# def display_item(item):    # item is an parameter
#     print(item)
# display_item(356)    # 365 is an argument


# display_item("this is a function")    # call with a value

# number = 20
# display_item(number)    # call with a variable

# a = "Monday "
# b = "12. Feb. 24 "
# date = a + b
# display_item(date)   # call with an expression 

# def sum_with_ten(input):
#     number_10 = 10
#     result = number_10 + input
#     print(result)

# print(number_10)

# def greeting(name):
#     print("Mingalarpar " + name)    # Mingalarpar is greeting in burmese language

# greeting('Tun Tun Win')
# print(name)


# x = 5
# def local():
#     x = 10
#     print(x)

# local()
# print(x) 



# def print_circum(radius):
#     pi = 3.14159    # where π = 3.14159
#     circumference = 2 * pi * radius    # The circumference of a circle is calculated by 2πr
#     print(circumference)

# # calling function three times with different values for radius. 
# print_circum(7.5)
# print_circum(10)
# print_circum(12.5)


# price of each product item
item1_price = 200
item2_price = 400
item3_price = 600

def discount_amount(item_total_price, discount):
    discount_price = item_total_price * discount
    total_price = item_total_price - discount_price
    print(f"Your total payment amount is: {total_price:.2f}")

def individual_item(item1):
    item_total = item1
    discount_amount(item_total, 0)

def combo_pack(item1, item2):
    item_total = item1 + item2
    discount_amount(item_total, 0.10)

def gift_pack(item1, item2, item3):
    discount = 0.25
    item_total = item1 + item2 + item3
    discount_amount(item_total, 0.25)

print("Online Store")
print("------------------------------------------------")
print("Product(S)                     Price")
individual_item(item1_price)
individual_item(item2_price)
individual_item(item3_price)
combo_pack(item1_price, item2_price)
combo_pack(item2_price, item3_price)
combo_pack(item1_price, item3_price)
gift_pack(item2_price, item1_price, item3_price)
print("------------------------------------------------")
print("For delivery contact:98764678899")