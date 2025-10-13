def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        if pattern == text[i:i + m]:
            print(f"Pattern found at index {i}")


text = "ABAAABCADACCDAAA"
pattern = "ABCADA"

naive_string_matching(text, pattern)
