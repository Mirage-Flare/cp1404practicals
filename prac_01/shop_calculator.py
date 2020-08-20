"""
Calculating total price from a number of items with different prices
Kyle Muccignat
"""
number_of_items = int(input("Number of items: "))
price_of_items = 0
for number in range(number_of_items):
    price_of_items += float(input("Price of item: "))
if price_of_items > 100:
    price_of_items *= 0.9
print("Total price for", number_of_items, "is", price_of_items)
