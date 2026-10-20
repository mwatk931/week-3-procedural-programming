name = input("Enter your name: ")
age = int(input("Enter your age: "))
language = input("Favourite programming language: ")

print(f"Hello, {name}!")

if age < 18:
    print("You are still learning and developing your skills.")
else:
    print("Keep developing your programming skills!")

if language.lower() == "python":
    print("Python is a great language to learn!")
else:
    print(f"Keep building your skills with {language}!")