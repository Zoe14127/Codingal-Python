field_1 = 120
field_2 = 80
field_3 = 150
field_4 = 200
field_5 = 90
total = field_1 + field_2 + field_3 + field_4 + field_5
avg = total / 5
print("Total harvest", total, "kgs")
print("Average per field", avg, "kgs")

price_per_kg = 15
earnings = total * price_per_kg
print("Total earnings from harvest is", earnings, "dollars")
bags = total//25
leftover = total % 25
print("Full bags packed", bags)
print("Leftover produce", leftover, "kgs")

last_year = 500
print("Better than last year?", total > last_year)
print("Same as last year?", total == last_year)
print("At least as good as last year?", total >= last_year)

total += 30
print("After bonus crop: ", total, "kgs")
total -= 15
print("After seed reservation: ", total, "kgs")
bags = total//25
print("Final bags packed", bags)
