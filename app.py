secret_number = 9
gues_count = 0
gues_limit = 3
while gues_count < gues_limit:
    guess = int(input("Guess: "))
    gues_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry you failed!")
    print("Try again.")




