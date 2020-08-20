"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
Kyle Muccignat
"""
BONUS_THRESHOLD = 1000
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < BONUS_THRESHOLD:
        print(sales * 0.1)
        sales = float(input("Enter sales: $"))
    else:
        print(sales * 0.15)
        sales = float(input("Enter sales: $"))
