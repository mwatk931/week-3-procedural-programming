weather = input("Enter the weather (sunny or rainy): ").strip().lower()

try:
    distance = float(input("Enter the journey distance in miles: "))
    budget = float(input("Enter your budget in pounds: "))
except ValueError:
    print("Invalid distance or budget. Please enter numbers.")
else:
    if weather not in ("sunny", "rainy") or distance <= 0 or budget < 0:
        print("Invalid input. Enter sunny or rainy weather, a positive distance, and a non-negative budget.")
    elif distance <= 1 and weather == "sunny":
        print("Walk. The weather is suitable and the journey is short.")
    elif weather == "rainy" and budget >= 3:
        print("Take the bus. The fare is £3.00.")
    elif budget >= distance * 2:
        taxi_cost = distance * 2
        print(f"Take a taxi. The estimated fare is £{taxi_cost:.2f}.")
    elif budget >= 3:
        print("Take the bus. The fare is £3.00.")
    else:
        print("Your budget is not enough for the available transport options.")