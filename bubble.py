def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):            
        for j in range(n - 1 - i):    
            if a[j] > a[j + 1]:       
                a[j], a[j + 1] = a[j + 1], a[j]  
    return a


num = [10, 64, 5, 12, 45]
print(bubble_sort(num))
