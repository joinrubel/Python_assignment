print("Customer Name : ")
name = input()

print("How many Items in your Cart: ")
n = int(input())

item_names = []
item_prices = []
total_price = 0

for i in range(n):

    name_input = input(f"Enter item {i+1} name: ")
    price_input = int(input(f"Enter price for {name_input}: "))
    

    item_names.append(name_input)
    item_prices.append(price_input)
    

    total_price += price_input


def calculate_discount(total):
    if total >= 5000:
        return total * 0.20
    else:
        return 0.0

less = calculate_discount(total_price)
final_price = total_price - less

#Output
print(f"\nCustomer name : {name}")

print("\n"+"="*30)

for i in range(n):
    print(f"  {item_names[i]}       = {item_prices[i]} Tk")

print(f"Sub-Total     = {total_price:.2f} Tk")
print(f"Discount (20%)= {less:.2f} Tk")
print(f"Final Price   = {final_price:.2f} Tk")
print("="*30)