import random

print('Welcome to the number guessing game')
level = int(input('Select your level: \n 1 for Easy; 2 for Medium; 3 for Hard :'))

guesses = 0


def generate_random_number(stage):
	value = 0
	if stage == 1:
		value = random.randint(1, 10)
	elif stage == 2:
		value = random.randint(1, 20)
	elif stage == 3:
		value = random.randint(1, 50)
	return value


if level == 1:
	guesses = 6
	while guesses > 0:
		guess_value = int(input('Guess the number between 1 and 10:'))
		random_number = generate_random_number(1)
		if guess_value == random_number:
			print('You got it right')
			exit()
		guesses -= 1
		print(f'You have {guesses} left')
	print('Game Over!!!')
	print(f'The answer was {random_number}')
	exit()
elif level == 2:
	guesses = 4
	random_number = generate_random_number(2)
elif level == 3:
	guesses = 3
	random_number = generate_random_number(3)
else:
	print('You have entered an invalid input')
	exit()
