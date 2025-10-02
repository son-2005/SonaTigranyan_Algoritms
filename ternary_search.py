def ternary_search(arr, target, left, right):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            return ternary_search(arr, target, left, mid1 - 1)
        elif target > arr[mid2]:
            return ternary_search(arr, target, mid2 + 1, right)
        else:
            return ternary_search(arr, target, mid1 + 1, mid2 - 1)

    return -1  


numbers = [1, 3, 4, 6, 7, 9, 12, 15, 18, 21]  
x = 12

result = ternary_search(numbers, x, 0, len(numbers) - 1)

if result != -1:
    print(f"{x} թիվը գտնվեց ինդեքս {result}-ում")
else:
    print(f"{x} թիվը ցուցակում չկա")
