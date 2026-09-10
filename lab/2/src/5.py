def relu(z: float) -> float:
    return max(z, 0)


if __name__ == "__main__":
    z = eval(input())
    print(relu(z))
