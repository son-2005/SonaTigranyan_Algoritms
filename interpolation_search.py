def interpolation_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right and target >= arr[left] and target <= arr[right]:
        # հաշվարկում ենք մոտավոր դիրքը
        pos = left + ((target - arr[left]) * (right - left) // (arr[right] - arr[left]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1

    return -1


numbers = [11, 23, 28, 40, 69, 71, 73, 76, 90, 122]
x = 71

result = interpolation_search(numbers, x)

if result != -1:
    print(f"{x} թիվը գտնվեց ինդեքս {result}-ում") 
else:
    print(f"{x} թիվը ցուցակում չկա") 
