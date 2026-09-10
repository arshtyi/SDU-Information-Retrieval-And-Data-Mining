import ast
import math


def entropy(labels):
    n = len(labels)
    count = {}
    for label in labels:
        count[label] = count.get(label, 0) + 1
    h = 0.0
    for c in count.values():
        p = c / n
        h -= p * math.log2(p)
    return h


def gain_ratio(data, feature_index):
    n = len(data)
    labels = [row[-1] for row in data]
    base_entropy = entropy(labels)
    groups = {}
    for row in data:
        value = row[feature_index]
        if value not in groups:
            groups[value] = []
        groups[value].append(row[-1])
    conditional_entropy = 0.0
    split_info = 0.0
    for group_labels in groups.values():
        p = len(group_labels) / n
        conditional_entropy += p * entropy(group_labels)
        split_info -= p * math.log2(p)
    information_gain = base_entropy - conditional_entropy
    if split_info == 0:
        return 0.0
    return information_gain / split_info


data = ast.literal_eval(input())
feature_count = len(data[0]) - 1
best_index = 0
best_ratio = -1.0
for i in range(feature_count):
    ratio = gain_ratio(data, i)
    if ratio > best_ratio:
        best_ratio = ratio
        best_index = i
print(best_index)
