import random
number = random.randint(0, 100)
count = 0
while True:
    guess = int(input("\nGive Your Guess : "))
    if number > guess:
        print("\nToo Low")
        count += 1
        continue
    elif number < guess:
        print("\nToo High")
        count += 1
        continue
    else:
        print("\nYou have guessed the number!")
        print(f"You have taken {count+1} guesses")
        print("You have WON!!\n")
        break
