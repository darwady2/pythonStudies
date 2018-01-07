def main():
    q = quickSort([7,10,12,9,1,5,6,7,7])
    print q

def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        p = array[0]
        for item in array:
            if item < p:
                less.append(item)
            elif item == p:
                equal.append(item)
            else:
                greater.append(item)

        return quickSort(less) + equal + quickSort(greater)

    else:
        return array



if __name__ == "__main__":
    main()
