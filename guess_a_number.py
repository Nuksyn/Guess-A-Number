import random

computer_number = random.randint(1, 100)

while True:
    try:
        number = int(input('Guess the number (1-100): '))
    except ValueError:
        print('Invalid input')
        continue
    if number == computer_number:
        print('You guessed the number')
        break
    if number > computer_number:
        print('Too high')
    if number < computer_number:
        print('Too low')


