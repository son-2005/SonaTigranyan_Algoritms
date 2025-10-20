def shell_sort(numbers):
    x = len(numbers)
    step = x // 2

    while step > 0:
        for i in range(step, x):
            value = numbers[i]
            pos= i
         
            while pos >= step and numbers[pos - step] > value:
                numbers[pos] = numbers[pos - step]
                pos -= step

            numbers[pos] = value

        step //= 2  

# Օրինակ
n = [23, 12, 1, 8, 34, 54, 2, 3]
print("Մինչև դասավորելը:", n)

shell_sort(n)
print("Դասավորված:", n)
