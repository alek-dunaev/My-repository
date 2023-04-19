import random

def binary_search(array, element, left, right):
    if left > right:  
        return False  

    middle = (right + left) // 2 
    if array[middle] < element and array[middle + 1] >= element:  
        return middle  
    elif element < array[middle]:  
        return binary_search(array, element, left, middle - 1)
    else:  
        return binary_search(array, element, middle + 1, right)

def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)

try:
    array = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
except ValueError as e:
        print('Вы ввели не число')

qsort_random(array,0,(len(array)-1))
print(array)

try:
    element = int(input('Введите любое число: '))
except ValueError as e:
        print('Вы ввели не число')

index = binary_search(array,element,0, len(array))
print('Номер позиции = ', index)
