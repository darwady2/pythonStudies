#1.4: Check if a string is a permutation of a palindrome.

def tally(s):
	l = len(s)
	d = {}
	for i in range(l):
		t = s[i]
		try:
			d[t] += 1
		except:
			d[t] = 1
	return l, d

def pal(s):
	try:
		l, d = tally(s)

		# Even letter string.
		if l % 2 == 0:
			for k, v in d.items():
				if v % 2 != 0:
					return 'Not a palindrome.'
			return 'Palindrome.'

		# Odd letter string.
		if l % 2 == 1:
			odd_count = 0
			for k, v in d.items():
				if v % 2 != 0:
					odd_count += 1
			if odd_count != 1:
				return 'Not a palindrome.'
			return 'Palindrome.'

	# All else.
	except:
		return 'Input must be a string.'

def main():
	s = raw_input('\nType in a string to test if it\'s a palindrome.\n\n')
	r = pal(s)
	print r

if __name__ == '__main__':
	main()
