def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
    tp = tn = fp = fn = 0
    for a, p in zip(actual, predicted):
        if a == 1 and p == 1:
            tp += 1
        elif a == 0 and p == 0:
            tn += 1
        elif a == 0 and p == 1:
            fp += 1
        elif a == 1 and p == 0:
            fn += 1
    confusion_matrix = [[tp, fn], [fp, tn]]
    total = tp + tn + fp + fn
    accuracy = (tp + tn) / total if total else 0
    precision = tp / (tp + fp) if tp + fp else 0
    recall = tp / (tp + fn) if tp + fn else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0
    specificity = tn / (tn + fp) if tn + fp else 0
    negativePredictive = tn / (tn + fn) if tn + fn else 0
    return (
        confusion_matrix,
        round(accuracy, 3),
        round(f1, 3),
        round(specificity, 3),
        round(negativePredictive, 3),
    )


if __name__ == "__main__":
    actual = eval(input())
    predicted = eval(input())
    print(performance_metrics(actual, predicted))
