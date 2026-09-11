name = input("Enter your name: ")
club = input("Enter your school club name: ")

member_num = 8
points = 9.5
events = 6
hrs = 1.5
is_active = True

print("Name:", name, "-> type:", type(name))
print("Club:", club, "-> type:", type(club))
print("Member Number:", member_num, "-> type:", type(member_num))
print("Points:", points, "-> type:", type(points))
print("Events:", events, "-> type:", type(events))
print("Hours:", hrs, "-> type:", type(hrs))
print("Is Active:", is_active, "-> type:", type(is_active))

member_num_text = str(member_num)
points_text = str(points)
events_text = str(events)
status_text = str(is_active)

print("Member Number Text:", member_num_text, "-> type:", type(member_num_text))
print("Points Text:", points_text, "-> type:", type(points_text))
print("Events Text:", events_text, "-> type:", type(events_text))
print("Status Text:", status_text, "-> type:", type(status_text))

first_3 = name[0:3]
last_letter = name[-1]
badge_code = first_3 + last_letter

print("The first 3 letters of your name are:", first_3)
print("The last letter of your name is:", last_letter)
print("Your badge code is:", badge_code)

reversed_club = club[::-1]
print("Your school club name spelled backwards is:", reversed_club)

batch_line_1 = "member" + badge_code.upper()
batch_line_2 = "Id" + member_num_text + "events" + events_text
batch_line_3 = "points" + points_text + "active" + status_text
batch_line_4 = "Secret club code" + reversed_club.upper()

print("")
print(batch_line_1)
print(batch_line_2)
print(batch_line_3)
print(batch_line_4)
