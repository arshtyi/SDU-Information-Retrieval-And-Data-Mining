from collections import defaultdict


def support(itemset, transactions):
    return sum(itemset.issubset(t) for t in transactions) / len(transactions)


def confidence(antecedent, consequent, transactions):
    return support(antecedent.union(consequent), transactions) / support(antecedent, transactions)


def combinations(iterable, r):
    iterable = list(iterable)
    n = len(iterable)
    if r > n:
        return []
    result = []
    for i in range(1 << n):
        if i.bit_count() == r:
            result.append(frozenset(iterable[j] for j in range(n) if i & (1 << j)))
    return result


def apriori(transactions, min_sup, min_conf):
    transactions = [set(t) for t in transactions]
    n = len(transactions)
    support_table = {}
    item_count = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_count[item] += 1
    current_frequent = set()
    for item, cnt in item_count.items():
        itemset = frozenset([item])
        sup = cnt / n
        if sup + 1e-12 >= min_sup:
            current_frequent.add(itemset)
            support_table[itemset] = sup
    all_frequent = set(current_frequent)
    k = 2
    while current_frequent:
        current_list = list(current_frequent)
        candidates = set()
        for i in range(len(current_list)):
            for j in range(i + 1, len(current_list)):
                candidate = current_list[i] | current_list[j]
                if len(candidate) != k:
                    continue
                valid = True
                for subset in combinations(candidate, k - 1):
                    if subset not in current_frequent:
                        valid = False
                        break
                if valid:
                    candidates.add(candidate)
        if not candidates:
            break
        count = defaultdict(int)
        for transaction in transactions:
            for candidate in candidates:
                if candidate.issubset(transaction):
                    count[candidate] += 1
        next_frequent = set()
        for candidate in candidates:
            sup = count[candidate] / n
            if sup + 1e-12 >= min_sup:
                next_frequent.add(candidate)
                support_table[candidate] = sup
        all_frequent.update(next_frequent)
        current_frequent = next_frequent
        k += 1
    for itemset in all_frequent:
        if len(itemset) < 2:
            continue
        for r in range(1, len(itemset)):
            for antecedent in combinations(itemset, r):
                consequent = itemset - antecedent
                conf = support_table[itemset] / support_table[antecedent]
                if conf + 1e-12 >= min_conf:
                    rules.append((antecedent, consequent, conf))
    return rules


if __name__ == "__main__":
    n = int(input())
    transactions = []
    for _ in range(n):
        transactions.append(input().split())
    min_sup, min_conf = map(float, input().split())
    rules = apriori(transactions, min_sup, min_conf)
    for rule in sorted(rules, key=lambda x: (-x[2], len(x[0]), len(x[1]))):
        print(f"{set(rule[0])} -> {set(rule[1])}: {rule[2]:.2f}")
