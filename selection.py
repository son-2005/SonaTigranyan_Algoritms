def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a

num = [10, 64, 5, 12, 45]
print(selection_sort(num))
