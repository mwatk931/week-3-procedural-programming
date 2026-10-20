try:
    age = int(input("Enter your age: "))
    order_total = float(input("Enter order total: £"))
except ValueError:
    print("Invalid age or order total.")
else:
    account_status = input("Is your account active? (yes/no): ").lower()
    discount_code = input("Do you have a valid discount code? (yes/no): ").lower()

    if order_total <= 0:
        print("Invalid order total.")
    elif age < 0 or account_status not in ("yes", "no") or discount_code not in ("yes", "no"):
        print("Invalid input.")
    elif account_status == "no":
        print("Please activate your account.")
    elif age < 18:
        if order_total < 100:
            parental_authorisation = input("Do you have parental authorisation? (yes/no): ").lower()
            if parental_authorisation == "yes" and discount_code == "yes":
                final_total = order_total * 0.90
                print("Order approved.")
                print(f"Final order total: £{final_total:.2f}")
            elif parental_authorisation == "yes":
                final_total = order_total
                print("Order approved.")
                print(f"Final order total: £{final_total:.2f}")
            elif parental_authorisation == "no":
                print("Order not approved: parental authorisation is required.")
            else:
                print("Invalid input.")
        else:
            print("Order not approved: users under 18 need an order total below £100.")
    elif order_total <= 500:
        if discount_code == "yes":
            final_total = order_total * 0.90
        else:
            final_total = order_total
        print("Order approved.")
        print(f"Final order total: £{final_total:.2f}")
    else:
        verification = input("Has additional verification been completed? (yes/no): ").lower()
        if verification == "yes" and discount_code == "yes":
            final_total = order_total * 0.90
            print("Order approved.")
            print(f"Final order total: £{final_total:.2f}")
        elif verification == "yes":
            final_total = order_total
            print("Order approved.")
            print(f"Final order total: £{final_total:.2f}")
        elif verification == "no":
            print("Additional verification required.")
        else:
            print("Invalid input.")