door1 = input("Room 1 - choose left or right: ").lower()

if door1 == "left":
    door2 = input("Room 2 - choose left or right: ").lower()
    if door2 == "right":
        bonus_choice = input(
            "Room 2 bonus - choose bonus or continue: "
        ).lower()
        if bonus_choice == "bonus":
            print("You found a bonus!")
        elif bonus_choice == "continue":
            print("You continue without a bonus.")
        else:
            print("Game over!")

        if bonus_choice == "bonus" or bonus_choice == "continue":
            door3 = input("Room 3 - choose left or right: ").lower()
            if door3 == "right":
                door4 = input("Room 4 - choose left or right: ").lower()
                if door4 == "left":
                    print("You found the treasure!")
                else:
                    print("Game over!")
            else:
                print("Game over!")
    else:
        print("Game over!")
else:
    print("Game over!")