age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 12:
    print("You can watch a children's film.")
elif age <= 14:
    print("You can watch a 12+ film.")
elif age <= 17:
    print("You can watch a 15+ film.")
else:
    print("You can watch any age-rated film in this example.")