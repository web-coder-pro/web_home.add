a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

value = input('Choose the value(+,-,*,/): ')

if value == '+':
	print('Answer:', a + b)
	
elif value == '-':
	print('Answer:', a - b)
	
elif value == '*':
	print('Answer:', a * b)

elif value == '/':
	print('Answer:', a / b)
	
else:
	print('False value, please try again')