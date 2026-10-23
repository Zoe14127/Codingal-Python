Camera = 2
Microphone = 1
Storage = 8
Location = 4

approved_apps = ["google","youtube"]

restricted_apps = ["instagram","tiktok"]
name = input("Enter your name: ").lower()
requested_app = input("Enter the app you want to access: ").lower()

if type(name) is str:
    print("The name is a string.")

if type(requested_app) is not int:
    print("The requested app is not a number.")

if requested_app in approved_apps:
    print(requested_app, "is an approved app.")
else:
    print(requested_app, "is not an approved app.")

student_permissions = Camera | Microphone | Storage
print(bin(student_permissions))

if student_permissions & Camera:
    print("Camera: Enabled")
else:
    print("Camera: Disabled")
 
if student_permissions & Microphone:
    print("Microphone: Enabled")
else:
    print("Microphone: Disabled")
 
if student_permissions & Storage:
    print("Storage: Enabled")
else:
    print("Storage: Disabled")
 
if student_permissions & Location:
    print("Location: Enabled")
else:
    print("Location: Disabled")

next_permission = Camera << 1
 
print("Camera bit:", bin(Camera))
print("After left shift:", bin(next_permission))

previous_permission = Storage >> 1
 
print("Storage bit:", bin(Storage))
print("After right shift:", bin(previous_permission))

if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access granted for", requested_app)
else:
    print("Access denied for", requested_app)