def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]  # որպես pivot վերցնում ենք առաջին էլեմենտը
    smaller = []
    greater = []
    for x in a[1:]:
        if x <= pivot:
            smaller.append(x)
        else:
            greater.append(x)
    return quick_sort(smaller) + [pivot] + quick_sort(greater)


num = [10, 64, 5, 12, 45]
print(quick_sort(num))
