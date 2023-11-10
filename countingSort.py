def countingSort(array):
    size = len(array)
    output = [0] * size

    count = [0] * 1000

    for i in range(0, size):
        count[array[i][0]] += 1

    for i in range(1, 1000):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i][0]] - 1] = array[i]
        count[array[i][0]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
        
        

def sort(array):
    neg_arr = []
    pos_arr = []
    
    for i in range(len(array)):
        if array[i][0] >= 0:
            pos_arr.append(array[i])
        else:
            neg_arr.append([-array[i][0],array[i][1]])
    
    countingSort(pos_arr)
    countingSort(neg_arr)
    
    result = [[-neg_arr[i][0], neg_arr[i][1]] for i in range(len(neg_arr)-1, -1, -1)] + pos_arr
    return result