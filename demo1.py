number = 10
guess = -1

print("guess the number")
while guess!=number:
	guess = int(input('Is it...'))

	if guess == number:
		print('you guessed it right')
	elif guess < number:
		print('it is small')
	elif guess > number:
		print('it is bigger')