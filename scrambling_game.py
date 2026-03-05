import random

words = ["python", "computer", "programming", "keyboard",
    "monitor", "internet", "developer", "algorithm",
    "database", "function", "variable", "network"]

def scramble_word(word):
    word_letters = list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)

def play_game():
    score = 0
    rounds_played = 0
    
    print("Welcome to the Word Scramble Game!")
    print("You have 3 attempts to guess the correct word.")
    
    while True:
        rounds_played += 1
        attempts = 3
        
        word = random.choice(words)
        scrambled = scramble_word(word)
        
        print(f"\nRound {rounds_played}")
        print("Scrambled word:", scrambled)
        
        while attempts > 0:
            guess = input("Your guess: ").lower()
            
            if guess == word:
                print("Correct! You win this round!")
                score += 1
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Incorrect! Attempts remaining: {attempts}")
                else:
                    print("Sorry, you're out of attempts.")
                    print("The correct word was:", word)
        
        print("Current Score:", score)
        
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break
    
    print("\nGame Over!")
    print("Final Score:", score)

play_game()