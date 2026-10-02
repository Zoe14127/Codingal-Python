hw = int(input("How many hours do you have for homework? "))
free_time = int(input("How many hours do you have for free time? "))

if hw > 60:
     plan = "Start homework now."
     print("That is a long homework session.")
else:
    plan = "Finish homework quickly."
    print("That is a short homework session.")

free_time_aft_hw = input("Is there free time after homework? (yes/no)")

if free_time_aft_hw == "yes":
    print("Remember to pick a hobby")
else:
    print("")

print("")
print("Daily Activity Planner")
print("Homework time: ", hw)
print("Free time: ", free_time)
print("Plan: ", plan)