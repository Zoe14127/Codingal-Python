def greet_customer():
    print("Welcome to the Art Supplies Store!")
    print("Get your colours, brushes, and paper here.")
greet_customer()

price_per_item = float(input("Enter the price per item in dollars: "))
items_bought = int(input("Enter the number of items bought: "))

def calculate_total(price, items):
    total = price * items
    return total

total_cost = calculate_total(price_per_item, items_bought)
rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)

amount_paid = float(input("Enter the amount paid by the customer: "))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_u_message(items):
    if items >= 5:
        return "Great choice! You picked a lot of supplies."
    else:
        return "Thanks for shopping at the art supplies store!"

print("Art supplies receipt:")
print("Price Per Item:", price_per_item)
print("Items Bought:", items_bought)
print("Total Cost:", rounded_total)
print("Amount Paid:", amount_paid)
print("Change Due:", rounded_change)
print(thank_u_message(items_bought))

