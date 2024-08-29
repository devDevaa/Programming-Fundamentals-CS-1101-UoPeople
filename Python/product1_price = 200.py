#price of each product items
item1_price = 200
item2_price = 400
item3_price = 600

# Discount amount
def discount_amount(item_total_price, discount):
    discount_price = item_total_price * discount
    total_price = item_total_price - discount_price
    return total_price

# If a customer purchases individual items, he does not receive any discount
def individual_item(item_name, item_price):
    print(f"{item_name} : {item_price:.2f}")

# If a customer purchases a combo pack with two unique items, he gets a 10% discount
def combo_pack(item1_name, item1_price, item2_name, item2_price):
    item_total = item1_price + item2_price
    item_total_price = discount_amount(item_total, 0.10)    # 10% = 10/100 = 0.10
    print(f"Combo ({item1_name} + {item2_name}) : {item_total_price:.2f}")

# If the customer purchases a gift pack, he gets a 25% discount
def gift_pack(item1_name, item1_price, item2_name, item2_price, item3_name, item3_price):
    item_total = item1_price + item2_price + item3_price
    item_total_price = discount_amount(item_total, 0.25)    # 25% = 25/100 = 0.25
    print(f"Gift ({item1_name} + {item2_name} + {item3_name}) : {item_total_price:.2f}")

# Call functions to create output
print("Online Store")
print("--------------------------")
print("Product(S)               Price")
individual_item("Item 1", item1_price)
individual_item("Item 2", item2_price)
individual_item("Item 3", item3_price)
combo_pack("Item 1", item1_price, "Item 2", item2_price)
combo_pack("Item 2", item2_price, "Item 3", item3_price)
combo_pack("Item 1", item1_price, "Item 3", item3_price)
gift_pack("Item 2", item2_price, "Item 1", item1_price, "Item 3", item3_price)
print("---------------------------")
print("For delivery Contact:98764678899")