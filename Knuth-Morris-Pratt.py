def build_lps(pattern):
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps

def kmp(text, pattern):
    lps = build_lps(pattern)
    i = j = 0
    found = []
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                found.append(i-j)
                j = lps[j-1]
        else:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1
    return found

text = "abcaaadcab"
pattern = "aa"
result = kmp(text, pattern)
print(f"Pattern գտնվեց {result} ինդեքսում")
