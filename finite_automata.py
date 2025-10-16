def finite_automata(pattern, alphabet):
    n = len(pattern)
    transitions = []

    for i in range(n + 1):
        d = {}
        for alpha in alphabet:
            d[alpha] = 0 
        transitions.append(d)

    for q in range(n + 1):          
        for a in alphabet:
            k = min(n, q + 1)
            while k > 0:
                last_k = (pattern[:q] + a)[-k:]   
                if last_k == pattern[:k]:
                    break
                k -= 1
            transitions[q][a] = k
    return transitions

def automata_search(text, pattern):
    if pattern == "":
        return list(range(len(text)+1))  

    alphabet = sorted(set(pattern + text))
    trans = finite_automata(pattern, alphabet)

    results = []
    state = 0
    index = 0  

    for letter in text:
        if letter not in trans[state]:
            state = 0
        else:
            state = trans[state][letter]

        if state == len(pattern):
            results.append(index - len(pattern) + 1)

        index += 1

    return results

text = "ABAEFABAACDAF"
pattern = "BAACD"

positions = automata_search(text, pattern)
print("Pattern found at positions:", positions)

