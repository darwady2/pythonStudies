def binarySearch(item, values):
    l = len(values)
    if l == 0:
        return False
    midpoint = l // 2
    if item == values[midpoint]:
        return item
    elif item < values[midpoint]:
        return binarySearch(item, values[:midpoint])
    elif item > values[midpoint]:
        return binarySearch(item, values[midpoint+1:])

def strLister(s):
    l = []
    for i, j in enumerate(s):
        l.append(s[i])
    l = sorted(l)
    return l

def strChecker(r, s1, s2): #r is how many letters must match.
    A = strLister(s1)
    B = strLister(s2)
    matchCount = 0
    for letter in A:
        if binarySearch(letter, B):
            matchCount += 1
    if matchCount >= r:
        return 'One edit away.'
    else:
        return 'More than one edit away.'


def edits(s1, s2):
    dif = len(s1) - len(s2)
    d = {}

    if dif < -1 or dif > 1:
        return 'More than one edit away.'

    # s1 is 1 shorter than s2.
    elif dif == -1:
        r = len(s1) #This many letters must match.
        return strChecker(r, s1, s2)

    # Both the same letters.
    elif dif == 0:
        r = len(s1) - 1 #This many letters must match.
        return strChecker(r, s1, s2)

    # s1 is 1 longer than s2.
    elif dif == 1:
        r = len(s1) - 1 # This many letters must match.
        return strChecker(r, s1, s2)


def main():
    #s1 = raw_input('Name the first string to check.')
    #s2 = raw_input('Name the second string to check.')
    s1 = 'pales'
    s2 = 'pales'
    print edits(s1, s2)

if __name__ == "__main__":
    main()
