def ssort(array):
    for i in range(len(array)):
        indxMin = i
        for j in range(i + 1, len(array)):
            if array[j] < array[indxMin]:
                indxMin = j
        tmp = array[indxMin]
        array[indxMin] = array[i]
        array[i] = tmp
    return a