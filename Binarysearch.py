list1 = [12, 24, 32, 39, 45, 50, 54]


def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if list1[mid] < n:
            low = mid + 1


        elif list1[mid] > n:
            high = mid - 1

        else:
            return mid

    return -1


result = binary_search(list1, 45)

if result != -1:
    print("element is present at index ", str(result))
else:
    print("element is not present in list1")


def linear_search(list1, n, key):
    for i in range(0, n):
        if (list1[i] == key):
            return i
    return -1


key = 54
n = len(list1)
res = linear_search(list1, n, key)
if res == -1:
    print("Element not found")
else:
    print("Element found at index: ", res)
