def InsertionSort(Array):
    for arrayPosition in range(1, len(Array)):
        actualElement = Array[arrayPosition]
        if arrayPosition > 0 and Array[arrayPosition - 1] > actualElement:
            Array[arrayPosition] = Array[arrayPosition - 1]
            arrayPosition -= 1
            Array[arrayPosition] = actualElement
            return Array, 1
    return Array, 0

def CocktailShakerSort(Array):
    for i in range(len(Array) - 1, 0, -1):
        for j in range(i, 0, -1):
            if Array[j] < Array[j - 1]:
                Array[j], Array[j - 1] = Array[j - 1], Array[j]
                return Array, 2
        for j in range(i):
            if Array[j] >Array[j + 1]:
                Array[j], Array[j + 1] = Array[j + 1], Array[j]
                return Array, 2
    return Array, 0

def BubbleSort(Array):
    for i in range(len(Array) - 1):
        if Array[i] > Array[i + 1]:
            Array[i], Array[i + 1] = Array[i + 1], Array[i]
            return Array, 2

    return Array, 0