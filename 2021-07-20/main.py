#With insert
def rotate_right_insert(array, k):

    copycat = [array[i] for i in range(len(array) - k)]
    for i in range(k):
        copycat.insert(i, array[len(array) - (k-i)])
    return copycat

array = [i for i in range(20)]

print(array)
array = rotate_right_insert(array, 3)
print(array)


#Without insert + with temporary array
def rotate_right(array, k):
    copycat = [None for i in range(len(array))]
    for i in range(len(array) - k):
        copycat[k+i] = array[i]
    surplus = [array[i] for i in range(len(array) - k, len(array))]
    for i in range(k):
        copycat[i] = surplus[i]
    return copycat


array = [i for i in range(20)]
print(array)
array = rotate_right(array, 3)
print(array)