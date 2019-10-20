# Total cost of the shopping cart:
sum=0
input_of_items = int(input(" Enter the number of items: "))
print(" Enter the price of your items")
for items in range(input_of_items):
    price = int(input("  Cart= "))
    sum = sum + price
print(sum, " the total price")