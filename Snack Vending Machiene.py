def calculate_change(paid,price):
    change = paid - price
    return change

snack_price = 25
print("Snack Vending machine")
print("Snack price is",snack_price)
print("Accepted coins 1,5,10,25/n")
total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert coin:(1,5,10,25)"))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin")
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted: {total_inserted} cents in {coins_inserted} coins")
    if total_inserted >= snack_price:
        print("Enough money inserted")
        break

change_due = calculate_change(total_inserted,snack_price)
print("Dispensing your snack")
if change_due == 0:
    pass
else:
    print("Here is your change",change_due)

print("Purchase Summary:")
print("Snack price:",snack_price)
print("Coins inserted:",coins_inserted)
print("Total pay:",total_inserted)
print("Change given:",change_due)
print("Thank you for your purchase")
