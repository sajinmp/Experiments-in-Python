def longest_word(s):

	"""	(str) -> str
	
	Return the largest alphabet sequence (largest word) from the given string.

	>>> longest_word("Arguement goes here")
		 'Arguement'
	>>> longest_word("132234 5432")
		 ''
	"""
	x = list(s)
	y = [[]]
	c = 0
	for i in range(len(x)):
		if x[i].isalpha():
			y[c].append(x[i])
		else:
			c = c + 1
			y.append([])
	l = 0
	z = []
	for i in range(len(y)):
		if len(y[i]) > l:
			l = len(y[i])
			z = y[i]
	if len(z) != 0:
		return ''.join(z)
	else:
		return ''


print longest_word(raw_input("Enter the string : ))
