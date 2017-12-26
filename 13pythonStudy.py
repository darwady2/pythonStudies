"""
Replace all spaces in a string with "%20", i.e.
Input: "Mr. John Smith"
Output: Mr%20John%20Smith"

Steps:
1. Trim the string
2. Get the length
3. Replace s[i] with %20 if == "_"
"""
def url(s):
    s = s.Trim()
    return s

def main():
    R = url(s = 'dan   ')
    print R

if __name__ == "__main__":
    main()
