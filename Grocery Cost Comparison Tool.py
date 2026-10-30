rice = 12
milk = 4
fruit = 8
baskets = 2
family_members = 4
cost_per_person = (rice + milk + fruit) * baskets/family_members
print("The cost per person is:", cost_per_person)

people = int(input("How many people are there?"))
total_items = int(input("How many items are there?"))
if people == 0:
    print("You cannot share between 0 people.")
else:
    remainder = total_items % people
if remainder == 0:
    print("The items can be shared equally. There will be", total_items // people, "items per person.")
else:
    print("The items cannot be shared equally. There will be", remainder, "items left over.")

average = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80
total_cost = average * total_weeks
corrected_total = total_cost - wrong_week_cost + correct_week_cost
corrected_average = corrected_total / total_weeks
print("Average:", average)
print("Wrong Week Cost:", wrong_week_cost)
print("Corrected Average:", corrected_average)

store_a = 70
store_b = 75
store_c = 80
if corrected_average < store_a and corrected_average < store_b and corrected_average < store_c:
    verdict = "Cheaper than all stores"
else:
    verdict = "Not cheaper than all stores"

print(" ")
print("Basket Cost Per Person:", cost_per_person)
print("Corrected Average Cost:", corrected_average)
print("Store Comparison Verdict:", verdict)