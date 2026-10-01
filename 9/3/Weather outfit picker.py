temp = int(input("Enter the temprature"))

if temp < 20:
    outfit = "jacket"
    print("It is cold today, you should wear a", outfit)
else:
    outfit = "t-shirt"
    print("It is warm today, you should wear a", outfit)

is_raining = input("Is it raining? (yes/no)")

if is_raining == "yes":
    print("You should also bring an umbrella")

wind_speed = int(input("Enter the wind speed in mph"))
if wind_speed > 30:
    print("It is windy today, you should wear a windbreaker over your", outfit)
else:
    print("There is no wind, you can wear your", outfit, "without a windbreaker")

has_puddles = input("Are there puddles on the ground? (yes/no)")
if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet, you should wear " ,shoes, "today")
else:
    shoes = "sneakers"
    print("The ground is dry, you can wear your", shoes, "today")

print("")
print("Weather check complete!")

print("Weather Outfit Picker")
print("Temperature: ", temp)
print("Raining: ", is_raining)
print("Wind Speed: ", wind_speed)
print("Puddles: ", has_puddles)
print("Outfit: ", outfit)
print("Shoes: ", shoes)
