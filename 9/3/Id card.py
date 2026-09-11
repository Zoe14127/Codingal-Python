name = input("What is your name?")
gadget = input("What is your favorite gadget?")
agent_num = 7
speed_rating = 9.5
machine_count = 12
height = 1.65
is_active = True

print(type(name))
print(type(gadget))
print(type(agent_num))
print(type(speed_rating))
print(type(machine_count))
print(type(height))
print(type(is_active))

agent_num_text = str(agent_num)
machine_count_text = str(machine_count)
speed_rating_text = str(speed_rating)
status_text = str(is_active)
print(type(speed_rating_text))
print(type(status_text))
print(type(agent_num_text))
print(type(machine_count_text))

first_3 = name[0:3]
last_letter = name[-1]
code_name = first_3 + last_letter
print("The first 3 letters of your name are:", first_3)
print("The last letter of your name is:", last_letter)
print("Your code name is:", code_name)

reversed_gadget = gadget[::-1]
print("Your favorite gadget spelled backwards is:", reversed_gadget)

batch_line_1 = "agent" + code_name .upper()
batch_line_2 = "Id" + agent_num_text + "machines" + machine_count_text
batch_line_3 = "speed" + speed_rating_text + "active" + status_text
batch_line_4 = "Secret gadget code" + reversed_gadget .upper()
print(batch_line_1)
print(batch_line_2)
print(batch_line_3)
print(batch_line_4)