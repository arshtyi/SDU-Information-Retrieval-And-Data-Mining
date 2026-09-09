import math
from collections import Counter


def learn_decision_tree(examples: list[dict], attributes: list[str], target_attr: str) -> dict:
    def majority_value(data):
        counts = Counter(example[target_attr] for example in data)
        max_count = max(counts.values())
        candidates = [k for k, v in counts.items() if v == max_count]
        return sorted(candidates, key=str)[0]

    def entropy(data):
        if not data:
            return 0.0
        counts = Counter(example[target_attr] for example in data)
        total = len(data)
        result = 0.0
        for count in counts.values():
            p = count / total
            result -= p * math.log2(p)
        return result

    def information_gain(data, attr):
        total_entropy = entropy(data)
        total = len(data)
        groups = {}
        for example in data:
            value = example[attr]
            groups.setdefault(value, []).append(example)
        conditional_entropy = 0.0
        for subset in groups.values():
            conditional_entropy += len(subset) / total * entropy(subset)
        return total_entropy - conditional_entropy

    def build_tree(data, attrs):
        labels = [example[target_attr] for example in data]
        if len(set(labels)) == 1:
            return labels[0]
        if not attrs:
            return majority_value(data)
        best_attr = max(attrs, key=lambda attr: information_gain(data, attr))
        tree = {best_attr: {}}
        values = sorted({example[best_attr] for example in data}, key=str)
        remaining_attrs = [attr for attr in attrs if attr != best_attr]
        for value in values:
            subset = [example for example in data if example[best_attr] == value]
            if not subset:
                tree[best_attr][value] = majority_value(data)
            else:
                tree[best_attr][value] = build_tree(subset, remaining_attrs)
        return tree

    if not examples:
        return {}
    usable_attributes = [attr for attr in attributes if attr != target_attr]
    return build_tree(examples, usable_attributes)


def print_tree(tree):
    outs = []
    for key, value in sorted(tree.items()):
        outs.append(f"{key}:{print_tree(value) if isinstance(value, dict) else value}")
    return "{" + ",".join(outs) + "}"


if __name__ == "__main__":
    examples = eval(input())
    attributes = eval(input())
    target_attr = eval(input())
    print(print_tree(learn_decision_tree(examples, attributes, target_attr)))
