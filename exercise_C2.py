balance = 1000.00
correct_pin = "1234"

pin = input("Enter your PIN: ")

if pin != correct_pin:
    print("Incorrect PIN!")
else:
    choice = input("Choose an option (balance, withdraw, deposit): ").lower()

    if choice == "balance":
        print(f"Current balance: £{balance:.2f}")
    elif choice == "withdraw":
        try:
            amount = float(input("Enter withdrawal amount: £"))
        except ValueError:
            print("Invalid amount.")
        else:
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                print("Withdrawal successful.")
                print(f"New balance: £{balance:.2f}")
    elif choice == "deposit":
        try:
            amount = float(input("Enter deposit amount: £"))
        except ValueError:
            print("Invalid amount.")
        else:
            if amount <= 0:
                print("Deposit amount must be positive.")
            else:
                balance += amount
                print("Deposit successful.")
                print(f"New balance: £{balance:.2f}")
    else:
        print("Invalid menu choice.")