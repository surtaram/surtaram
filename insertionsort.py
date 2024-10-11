l = [23, 45, 20, 45, 67, 2, 3, 4, 5]


def insertion_sort(input):
    n = len(input)

    for i in range(0, n):
        key = input[i]
        j = i - 1

        while j >= 0 and key < input[j]:
            input[j + 1] = input[j]
            j -= 1
            input[j + 1] = key
    return input


print(insertion_sort(l))


def selection_sort(input):
    n = len(input)

    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if input[j] < input[min]:
                min = j
                input[i], input[min] = input[min], input[i]

        return input


print(selection_sort(l))
