import random

highest = 10
answer = random.randrange(1,highest)
x = raw_input('Guess from 1 to ' + str(highest) + ': ')
while (1):
	try:
		x = int(x)
	except:
		print 'It\'s not Number!'
		x = raw_input('Guess from 1 to ' + str(highest) + ': ')
		continue
	if(x == answer):
		raw_input('You Win\n')
		break
	elif(x > answer):
		print ('Guess Lower')
	else:
		print ('Guess Higher')
	x = raw_input('Guess from 1 to ' + str(highest) + ': ')
