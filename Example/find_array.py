def find(array, element):
    count = 0
    for i, a in enumerate(array):
        if a == element:
            count += 1
    return count

array = list(map(int, input().split()))
element = int(input())

print(find(array, element))
