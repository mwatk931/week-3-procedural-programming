secret_number = 7
guess = int(input("Guess the secret number: "))

if guess == secret_number:
    print("Correct! You win!")
elif guess < secret_number:
    print("Too low!")
else:
    print("Too high!")