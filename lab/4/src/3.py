import math
from collections import Counter, defaultdict


def entropy(labels):
    n = len(labels)
    if n == 0:
        return 0.0
    cnt = Counter(labels)
    ans = 0.0
    for c in cnt.values():
        p = c / n
        ans -= p * math.log2(p)
    return ans


def gain_ratio(data, feature_index, base_entropy):
    n = len(data)
    groups = defaultdict(list)
    for row in data:
        value = row[feature_index]
        label = row[-1]
        groups[value].append(label)
    conditional_entropy = 0.0
    for labels in groups.values():
        p = len(labels) / n
        conditional_entropy += p * entropy(labels)
    gain = base_entropy - conditional_entropy
    iv = 0.0
    for labels in groups.values():
        p = len(labels) / n
        iv -= p * math.log2(p)
    if iv == 0:
        return 0.0
    return gain / iv


def solve(data):
    feature_count = len(data[0]) - 1
    labels = [row[-1] for row in data]
    base_entropy = entropy(labels)
    best_index = 0
    best_ratio = -1.0
    for i in range(feature_count):
        ratio = gain_ratio(data, i, base_entropy)
        if ratio > best_ratio:
            best_ratio = ratio
            best_index = i
    return best_index


data = eval(input())
print(solve(data))
