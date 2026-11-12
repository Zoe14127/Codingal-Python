def great_customer():
    print("Welcome to the lemonade stand.")
    print("Fresh lemonade made just for you.")
great_customer()

price_per_cup = float(input("Enter the price per cup of in dollars: "))
cups_sold = int(input("Enter the number of cups sold: "))

def calculate_total(price_per_cup,cups_sold):
    total_sales = price_per_cup * cups_sold
    return total_sales

total=calculate_total(price_per_cup,cups_sold)
print(total)

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("Total cost: ",rounded_total)

amount_paid = float(input("Enter the amount paid by the customer: "))

def calculate_change(amount_paid, total_cost):
    change = amount_paid - total_cost
    return change

change_due = calculate_change(amount_paid, total_cost)
rounded_change = round(change_due, 2)

def thank_u_message(cups):
    if cups >= 5:
        return "Wow! Big order! Thank you for your support!"
    else:
        return "Thank you for stopping by the stand!"
thank_u_message(cups_sold)

print("Lemonade Stand Summary:")
print("Cups sold:", cups_sold)
print("Total sales: $", rounded_total)
print("Amount paid: $", amount_paid)
print("Change due: $", rounded_change)
print(thank_u_message(cups_sold))