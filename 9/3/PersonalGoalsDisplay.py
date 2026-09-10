import keyword

daily_minutes = 30
name = input("What is your name? \n")
skill = input("What is your skill? \n")
month = input("What is your target month? \n")

print("\nGoal Plan \n")
print("My name is", name, "\nMy skill is", skill, "\nMy target month is", month, "\nI will practice for", daily_minutes, "minutes every day.")
print("My name is", name, "My skill is", skill, "My target month is", month, end="") 
print("I will practice for", daily_minutes, "minutes every day.")
print(keyword.kwlist)