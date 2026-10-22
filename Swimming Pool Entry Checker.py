print("===Swimming Pool Entry Checker===")
print("Answer 3 questions and I will tell you which pool you can use")

age = int(input("How old are you? "))
can_swim = input("Can you swim? (yes/no) ").strip().lower()
adult_here = input("Is there an adult with you? (yes/no) ").strip().lower()

print("")
print("===Entry Decision===")
print("-"  * 35)

if age <= 4:
    print("Toddler, you can use the splash pool only, always with an adult.")
elif age >= 5 and age <=11:
    print("Child, you can use the main pool with an adult.")
elif age >= 12 and age <=17:
    print("Teen, you can use the main pool alone if you can swim")
else:
    print("Adult, all pools are available to you.")

if can_swim != "yes" and can_swim != "no":
    print("Invalid input.")
    swim_known = False
else:
    swim_known = True

if can_swim == "yes" and adult_here == "yes":
    print("You can swim in the deep end.")
else:
    print("You cannot swim in the deep end.")

if age <12 or can_swim == "no":
    print("Warning: deep end may be dangerous for you. Please stay in the shallow end.")

if adult_here != "yes" and adult_here != "no":
    print("Invalid input.")
    adult_known = False
else:
    adult_known = True
if adult_here == "no" and adult_known == True:
    print("Reminder: Lifeguards are not responsible for children left unattended. Please stay with an adult.")

print("")
print("Have a safe swim!")
print("")