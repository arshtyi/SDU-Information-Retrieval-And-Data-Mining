import math


def sigmoid(z: float) -> float:
    return round(1.0 / (1 + math.exp(-z)), 4)


if __name__ == "__main__":
    z = float(input())
    print(f"{sigmoid(z):.4f}")
