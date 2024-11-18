import random

print('Welcome to the Guess Number!')
choice_number = input('Please enter the limit number for the challenge: ')

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print('Error: the value entered is not a number. Please run again and enter a number.')
    quit()

random_number = random.randint(0, choice_number)
n_choices = 0

while True:
    answer_user = input('Guess the number: ')

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print('Error: the value entered is not a number. Please enter a valid number.')
        continue

    n_choices = n_choices + 1
    if answer_user == random_number:
        print('You got it right!')
        break
    elif answer_user > random_number:
        print('You guessed too high, the number is smaller than that...')
    else:
        print('You guessed too low, the number is larger than that...')

print("Your number of attempts was: " + str(n_choices))
