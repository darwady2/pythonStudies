"""
Replace all spaces in a string with "%20", i.e.
Input: "Mr. John Smith"
Output: Mr%20John%20Smith"

Steps:
1. Trim the string
2. Get the length
3. Replace s[i] with %20 if == "_".
 -- Do this with a list, since strings are immutable in Python and we have to iterate through at least once to find the spaces.
"""

def url(s):
    sList = list(s.strip())
    for i, j in enumerate(sList):
        if j == " ":
            sList[i] = "%20"
    sList = ''.join(sList)
    return sList

def main():
    R = url(s = 'dan is neat  ')
    print R

if __name__ == "__main__":
    main()
