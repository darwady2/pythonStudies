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
