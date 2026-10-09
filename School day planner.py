print("Smart School Day Planner")
print("Answer the 3 questions, and I will plan your day.")

day = input("What day is it? (Monday to Sunday) ").strip().capitalize()
homework = input("Do you have homework today? (yes/no) ").strip().lower()
weather = input("What is the weather? (sunny/rainy/snowy) ").strip().lower()
print("")
print("Your day is planned as follows:", day)
print("-" * 35)
if day in ("Saturday", "Sunday"):
    print("You have a weekend! Enjoy your day off.")
elif day == "Monday":
    print("It's Monday! Time to start the week strong.")
elif day == "Friday":
    print("It's Friday! Finish your tasks and prepare for the weekend.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("It's a weekday. Stay focused and productive.")
else:
    print("Invalid day input. Please enter a valid day of the week.")

if homework == "yes" and weather == "sunny":
    print("After school head to the park - great weather and homework is done.")
if weather == "rainy" or weather == "cloudy":
    print("Weather tip: pack your umbrella; it may get wet outside.")
if not (homework == "yes"):
    print("Homework not done yet. Finish it before going out.")

if weather == "rainy" and not (homework == "yes"):
    print("Best plan: stay inside and finish homework.")    
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan: finish homework and then enjoy the sunny weather outside.")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan: enjoy your weekend and the sunny weather outside.")
else:
    print("Best plan: stay inside and finish homework.")
print("Plan complete. Have a great day!")
