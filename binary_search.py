def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  

        if arr[mid] == target:
            return mid   
        elif arr[mid] < target:
            left = mid + 1   
        else:
            right = mid - 1  

    return -1


numbers = [1, 3, 4, 6, 7, 9, 12, 15]
x = 6

result = binary_search(numbers, x)

if result != -1:
    print(f"{x} թիվը գտնվեց ինդեքս {result}-ում")
else:
    print(f"{x} թիվը ցուցակում չկա")
