raw_item_name = "cyberpunk mousepad"
raw_price = "45.50"
raw_quantity = "3"
raw_discount_percent = "15"

item_name = str(raw_item_name)
price = float(raw_price)
quantity = int(raw_quantity)
discount_percent = int(raw_discount_percent)

price_without_discount = price * quantity
total_price = price_without_discount / 100 * (100 - discount_percent)

print(type(item_name))
print(type(price))
print(type(quantity))
print(type(discount_percent))
print(type(price_without_discount))
print(type(total_price))

print(price_without_discount)
print(total_price)