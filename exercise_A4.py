mark = float(input("Enter your mark: "))

if mark < 0 or mark > 100:
    print("Invalid mark")
elif mark >= 70:
    print("Grade: First")
elif mark >= 60:
    print("Grade: Upper Second")
elif mark >= 50:
    print("Grade: Lower Second")
elif mark >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")