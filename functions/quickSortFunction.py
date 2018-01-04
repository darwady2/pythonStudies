def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        p = array[0]
        for i in array:
            if p > i:
                less.append(i)
            elif p == i:
                equal.append(i)
            else:
                greater.append(i)
        return quickSort(less) + equal + quickSort(greater)

    else:
        return array
