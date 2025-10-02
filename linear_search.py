def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # վերադարձնում է ինդեքսը, եթե գտավ
    return -1          # վերադարձնում է -1, եթե չգտավ


numbers = [14, 17, 1, 9, 3, 5]
x = 9

result = linear_search(numbers, x)

if result != -1:
    print(f"{x} թիվը գտնվեց ինդեքս {result}-ում")
else:
    print(f"{x} թիվը ցուցակում չկա")
