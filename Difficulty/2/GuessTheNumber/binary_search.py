min = 0
max = 1001
while True:
	guess = (min+max)//2
	print(guess)
	in_stream = input()
	if in_stream == "correct":
		break
	elif in_stream == "higher":
		min = guess
	else:
		max = guess