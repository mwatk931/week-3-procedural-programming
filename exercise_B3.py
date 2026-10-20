correct_username = "student"
correct_password = "python123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username:
    print("Username recognised")

if username == correct_username and password == correct_password:
    print("Login successful!")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Access granted")
    else:
        print("You must be at least 18.")
else:
    print("Incorrect username or password.")