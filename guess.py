import random

number = random.randint(1,50)

number_of_guesses = 0

while number_of_guesses < 5:
    print('Guess a number between 1 and 50: ')

    guess = input()
    guess = int(guess)

    if guess > 0 and guess <= 50:
        number_of_guesses += 1
    else:
        print("Not in range: Try again")

    if abs(5) >= number - guess >= 0:
        print('You are close!')
        print(number - guess)
    else:
        print('you are not close.')
        print(number - guess)

    if number_of_guesses == 5:
        print("Game Over")
        break

    if guess == number:
        break

if guess == number:
    print("Guessed the number in " + str(number_of_guesses) + ' tries!')

else:
    print("The number was: " + str(number))
