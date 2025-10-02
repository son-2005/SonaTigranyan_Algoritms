
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while prev < min(step, n):
        if arr[prev] == target:
            return prev
        prev += 1

    return -1  


numbers = [1, 3, 4, 6, 7, 9, 12, 15, 18, 21, 25, 30]
x = 18

result = jump_search(numbers, x)

if result != -1:
    print(f"{x} թիվը գտնվեց ինդեքս {result}-ում")
else:
    print(f"{x} թիվը ցուցակում չկա")
