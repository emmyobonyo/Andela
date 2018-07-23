
while True:
	#Make sure that the user inputs 5 numbers with exactly one space between them
	try:
		var1, var2, var3, var4, var5 = [int(x) for x in input('Enter five numbers here (enter one space after each number.): ').split(' ')]
	except ValueError:
		print ("Kindly make sure you've entered exactly 5 numbers, or make sure that there is exactly one space between the numbers. Don't put a space between the first and last number")
		continue
	if var1 < 0 or var2 < 0 or var3 < 0 or var4 < 0 or var5 < 0:
		print("Please don't use negaive numbers")
		continue
	else:
		#Printing the 5 inputs separated by a single space.
		print ("The input is: ")
		input1 = [var1, var2, var3, var4, var5]
		input2 = [str(a) for a in input1]
		print (' '.join(input2))
		break
if 1 <= var1 <= 10**9 and 1 <= var2 <= 10**9:
	#Making sure the input values are in the acceptable range
	a = var1 + var2 + var3 + var4
	b = var1 + var2 + var3 + var5
	c = var1 + var2 + var4 + var5
	d = var1 + var3 + var4 + var5
	e = var2 + var3 + var4 + var5
	numlist = [a, b, c, d , e]
	f = [min(numlist), max(numlist)]
	g = [str(a) for a in f]
	print ("The output is: ")
	print (' '.join(g))
else: 
	print("One or more of the values are in the wrong range")

