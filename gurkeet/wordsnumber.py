def convert_to_words(num):
	l = len(num)

	# Base cases
	if (l == 0):
		print("empty string")
		return

	if (l > 4):
		print("Length more than 4 is not supported")
		return

	
	single_digits = ["zero", "one", "two", "three",
					"four", "five", "six", "seven",
					"eight", "nine"]

	two_digits = ["", "ten", "eleven", "twelve",
				"thirteen", "fourteen", "fifteen",
				"sixteen", "seventeen", "eighteen",
				"nineteen"]

	
	tens_multiple = ["", "", "twenty", "thirty", "forty",
					"fifty", "sixty", "seventy", "eighty",
					"ninety"]

	tens_power = ["hundred", "thousand"]

	# Used for debugging purpose only
	print(num, ":", end=" ")

	# For single digit number
	if (l == 1):
		print(single_digits[int(num[0])])
		return

	# Iterate while num is not '\0'
	x = 0
	while (x < len(num)):

		# Code path for first 2 digits
		if (l >= 3):
			if (int(num[x]) != 0):
				print(single_digits[int(num[x])],
					end=" ")
				print(tens_power[l - 3], end=" ")
				# here len can be 3 or 4

			l -= 1

		# Code path for last 2 digits
		else:

			# Need to explicitly handle
			# 10-19. Sum of the two digits
			# is used as index of "two_digits"
			# array of strings
			if (int(num[x])  == 1):
				sum = (int(num[x]) +
					int(num[x+1]) )
				print(two_digits[sum])
				return

			# Need to explicitly handle 20
			elif (int(num[x])  == 2 and
				int(num[x + 1])  == 0):
				print("twenty")
				return

			# Rest of the two digit
			# numbers i.e., 21 to 99
			else:
				i = int(num[x])
				if(i > 0):
					print(tens_multiple[i], end=" ")
				else:
					print("", end="")
				x += 1
				if(int(num[x])  != 0):
					print(single_digits[int(num[x]) ])
		x += 1


# Driver Code
#convert_to_words("9923") # Four Digits
#convert_to_words("523") # Three Digits
#convert_to_words("89") # Two Digits
#convert_to_words("8") # One Digits
num=input('enter the number upto 4 digits you want to convert:\n')
convert_to_words(num)