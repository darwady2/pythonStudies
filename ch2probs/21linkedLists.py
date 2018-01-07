#O(2N) runtime (simplifies to O(N) runtime.)


from collections import deque

def main():
    d = deque('abcdefgghh')
    print d
    dupes = listDupes(d)
    newD = removeDupes(d, dupes)

    print newD


def listDupes(d):
    values = {}
    take_out = []
    for item in d:
        if item in values:
            take_out.append(item)
        else:
            values[item] = 1
    return take_out

def removeDupes(d, dupes):
    for item in dupes:
        d.remove(item)

    return d



if __name__ == "__main__":
    main()
