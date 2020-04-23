import random


def generate_random_number(stage):
	value = 0
	if stage == 1:
		value = random.randint(1, 10)
	elif stage == 2:
		value = random.randint(1, 20)
	elif stage == 3:
		value = random.randint(1, 50)
	return value


def guess_number(trials, my_stage):
	global random_number
	maxi = 0
	if my_stage == 1:
		maxi = 10
	elif my_stage == 2:
		maxi = 20
	elif my_stage == 3:
		maxi = 50
	while trials > 0:
		guess_value = int(input(f'Guess the number between 1 and {maxi}:'))
		random_number = generate_random_number(my_stage)
		if guess_value > maxi:
			print('You have entered a number above the limit')
		if guess_value == random_number:
			print('You got it right!')
			exit()
		trials -= 1
		print(f'You have {trials} left')
	print('Game over!')
	print(f'The answer was {random_number}')
	exit()


print('Welcome to the number guessing game')
try:
	level = int(input('Select your level: \n 1 for Easy; 2 for Medium; 3 for Hard :'))
except ValueError:
	print('There are 3 levels, easy, medium and hard')
	exit()
else:
	guesses = 0
	if level == 1:
		guesses = 6
		guess_number(guesses, 1)
	elif level == 2:
		guesses = 4
		guess_number(guesses, 2)
	elif level == 3:
		guesses = 3
		guess_number(guesses, 3)
	else:
		print('You have entered an invalid input')
	exit()
