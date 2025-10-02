def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    left = i // 2
    right = min(i, n - 1)
    return binary_search(arr, target, left, right)


numbers = [2, 5, 7, 10, 14, 18, 21, 25, 30, 36, 40]  
x = 21

result = exponential_search(numbers, x)

if result != -1:
    print(f"{x} թիվը գտնվեց ինդեքս {result}-ում")
else:
    print(f"{x} թիվը ցուցակում չկա")
