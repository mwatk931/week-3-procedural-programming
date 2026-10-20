age = int(input("Enter your age: "))
height = float(input("Enter your height in centimetres: "))

if age < 12:
    print("You are too young for this ride.")
elif height >= 140:
    print("You can ride!")
else:
    print("You do not meet the height requirement.")