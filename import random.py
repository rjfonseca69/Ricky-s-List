import random

def play_guessing_game():
    
    target_number = random.randint(1, 10)

    
    attempts = 0

    while True:
    
        user_guess = int(input("Enter your guess (1-10): "))
        attempts += 1

        
        if user_guess == target_number:
            print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts.")
            break
        else:
            if user_guess < target_number:
                print("Guess higher.")
            else:
                print("Guess lower.")

if __name__ == "__main__":
    play_guessing_game()