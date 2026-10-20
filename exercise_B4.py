amount = float(input("Enter shopping total: £"))

if amount < 0:
    print("Invalid shopping total.")
else:
    if amount >= 100:
        discount_rate = 0.20
    elif amount >= 50:
        discount_rate = 0.10
    else:
        discount_rate = 0

    discount = amount * discount_rate
    final_amount = amount - discount

    print(f"Original amount: £{amount:.2f}")
    print(f"Discount: £{discount:.2f}")
    print(f"Final amount: £{final_amount:.2f}")