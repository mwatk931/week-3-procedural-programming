try:
    loan_amount = float(input("Enter the loan amount in pounds: "))
    annual_rate = float(input("Enter the annual interest rate (%): "))
    years = float(input("Enter the repayment period in years: "))
except ValueError:
    print("Invalid input.")
else:
    if loan_amount <= 0 or years <= 0 or annual_rate < 0:
        print("Invalid input.")
    elif annual_rate == 0:
        number_of_payments = years * 12
        monthly_payment = loan_amount / number_of_payments
        total_repaid = monthly_payment * number_of_payments
        total_interest = total_repaid - loan_amount
    else:
        monthly_rate = annual_rate / 100 / 12
        number_of_payments = years * 12
        rate_factor = (1 + monthly_rate) ** number_of_payments
        monthly_payment = (
            loan_amount * monthly_rate * rate_factor / (rate_factor - 1)
        )
        total_repaid = monthly_payment * number_of_payments
        total_interest = total_repaid - loan_amount

    if loan_amount > 0 and years > 0 and annual_rate >= 0:
        print(f"Monthly payment: £{monthly_payment:.2f}")
        print(f"Total amount repaid: £{total_repaid:.2f}")
        print(f"Total interest: £{total_interest:.2f}")

        if monthly_payment > 500:
            print("Warning: Your monthly payments are high.")
        if total_interest > loan_amount * 0.25:
            print("Warning: Total interest is more than 25% of the loan amount.")