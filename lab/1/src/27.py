from itertools import combinations
from collections import defaultdict


def generate_frequent_itemsets(transactions, min_support):
    frequent_itemsets = {}
    transactions = [set(t) for t in transactions]
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[item] += 1
    current_frequent = set()
    for item, count in item_counts.items():
        if count >= min_support:
            frequent_itemsets[item] = count
            current_frequent.add((item,))
    k = 2
    while current_frequent:
        items = sorted({item for itemset in current_frequent for item in itemset})
        candidate_counts = defaultdict(int)
        for candidate in combinations(items, k):
            if all(tuple(subset) in current_frequent for subset in combinations(candidate, k - 1)):
                candidate_set = set(candidate)
                for transaction in transactions:
                    if candidate_set.issubset(transaction):
                        candidate_counts[candidate] += 1
        next_frequent = set()
        for candidate, count in candidate_counts.items():
            if count >= min_support:
                frequent_itemsets[candidate] = count
                next_frequent.add(candidate)
        current_frequent = next_frequent
        k += 1
    return frequent_itemsets


# 主程序
T = int(input())
transactions = [input().strip().split(",") for _ in range(T)]

min_support = int(input())

frequent_itemsets = generate_frequent_itemsets(transactions, min_support)

# 输出结果
for itemset, count in sorted(frequent_itemsets.items(), key=lambda x: -x[1]):
    if isinstance(itemset, str):
        print(f"{{{itemset}}}")
    else:
        print(f"{{{', '.join(itemset)}}}")
