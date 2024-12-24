# The secret word to be guessed (can be changed to any word or dynamically generated)
import random
# Function to show hints based on the user's guess
def display_hint(secret_word, guess):
    hint = []
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper())  # Exact match
        elif guess[i] in secret_word:
            hint.append(guess[i].lower())  # Letter in word but wrong position
        else:
            hint.append('_')  # Letter not in word
    return ' '.join(hint)

def play_game(secret_word):
    secret_word = secret_word.lower()
    print(f"Your hint is: {'_ ' * len(secret_word)}")
    attempts = 0
    
    while True:
        guess = input("Enter your guess: ").lower()
        attempts += 1
        
        if len(guess) != len(secret_word):
            print(f"Your guess must be {len(secret_word)} letters long.")
            continue
        
        if guess == secret_word:
            print(f"Congratulations! You've guessed the word '{secret_word}' in {attempts} attempts.")
            break
        
        hint = display_hint(secret_word, guess)
        print(f"Your hint is: {hint}")
        
# Example secret word, but this could be randomized or input
secret_word = "mosiah"
play_game(secret_word)