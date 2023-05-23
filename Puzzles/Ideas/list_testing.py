def in_order(values):
    i = 0
    size = len(values)
    print(f'This list has {size} elements')
    while i < size - 1:
        if values[i+1] < values [i]:
            return False
        i += 1
    return True
