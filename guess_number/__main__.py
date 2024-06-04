import random

ATTEMPS = 7


def guess_number() -> None:
    secret_number = random.randint(1, 100)

    print("🕹️ Welcome to 'Guess the Number'! 🕹️")
    print("A number between 1 and 100 has been chosen. Can you guess what it is?")
    print(f"🤞 You have {ATTEMPS} attempts. Good luck! 🍀")

    for attempt in range(1, ATTEMPS + 1):
        guess = int(input(f"Attempt {attempt}: "))
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("🎉 Congratulations! You guessed the number! 🎉")
            break
    else:
        print(f"😢 Out of attempts! The number was {secret_number}.")



if __name__ == "__main__":
    guess_number()
