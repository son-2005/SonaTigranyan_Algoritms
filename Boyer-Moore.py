def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    bad_char = {}
    for i in range(len(pattern)):
        ch = pattern[i]
        bad_char[ch] = i

    result = []
    shift = 0

    while shift <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            result.append(shift)
            shift += 1  
        else:
            mismatch_char = text[shift + j]
            last_index = bad_char.get(mismatch_char, -1)
            shift += max(1, j - last_index)

    return result


text = "abadcad"
pattern = "ca"
result = boyer_moore(text, pattern)
print(f"Pattern գտնվեց {result} ինդեքսում")
