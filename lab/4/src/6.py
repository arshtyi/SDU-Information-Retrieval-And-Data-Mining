n = int(input())
documents = []
positive_count = 0
negative_count = 0
word_count = {}
for _ in range(n):
    line = input()
    label, text = line.split("\t", 1)
    words = text.split()
    unique_words = set(words)
    if label == "positive":
        positive_count += 1
        idx = 0
    else:
        negative_count += 1
        idx = 1
    for word in unique_words:
        if word not in word_count:
            word_count[word] = [0, 0]
        word_count[word][idx] += 1
k = int(input())
features = []
for word, (A, B) in word_count.items():
    C = positive_count - A
    D = negative_count - B
    row1 = A + B
    row2 = C + D
    col1 = A + C
    col2 = B + D
    chi2 = 0.0
    if n > 0:
        E_A = row1 * col1 / n
        E_B = row1 * col2 / n
        E_C = row2 * col1 / n
        E_D = row2 * col2 / n
        observations = (A, B, C, D)
        expectations = (E_A, E_B, E_C, E_D)
        for O, E in zip(observations, expectations):
            if E != 0:
                chi2 += (O - E) ** 2 / E
    features.append((word, chi2))
features.sort(key=lambda x: (-x[1], x[0]))
for word, _ in features[:k]:
    print(word)
