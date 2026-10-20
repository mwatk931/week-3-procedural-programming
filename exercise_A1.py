weather = input("What is the weather like? ").lower()

if weather == "sunny":
   print("Great! Go for a walk.")
elif weather == "rainy":
    print("Take an umbrella.")
elif weather == "snowy":
    print("Stay warm and be careful!")
else:
    print("I don't recognise that weather.")