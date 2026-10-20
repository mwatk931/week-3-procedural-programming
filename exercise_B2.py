number = int(input("Enter an integer: "))

if number > 0:
    print("Positive number")
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

if number > 100:
    print("This is a large number.")