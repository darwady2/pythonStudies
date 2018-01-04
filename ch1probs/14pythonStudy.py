#1.4: Check if a string is a permutation of a palindrome.

"""
Steps:
1. Do a frequency distribution of each letter.
2. Determine if it's odd or even, then check if it has the proper distribution.

"""

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
					return 'Not a permutation of a palindrome.'
			return 'Permutation of a palindrome.'

		# Odd letter string.
		if l % 2 == 1:
			odd_count = 0
			for k, v in d.items():
				if v % 2 != 0:
					odd_count += 1
			if odd_count != 1:
				return 'Not a permutation of a palindrome.'
			return 'Permutation of a palindrome.'

	# All else.
	except:
		return 'Input must be a string.'

def main():
	s = raw_input('\nType in a string to test if it\'s a permutation of a palindrome.\n\n')
	r = pal(s)
	print r

if __name__ == '__main__':
	main()
