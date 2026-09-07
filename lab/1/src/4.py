import numpy as np


def preprocess_data():
    n = int(input())
    data = np.array([float(input()) for _ in range(n)], dtype=float)
    data[data == -1] = np.nan
    mean_value = np.nanmean(data)
    data = np.where(np.isnan(data), mean_value, data)
    data = data[(data >= 200) & (data <= 800)]
    return data


def main():
    ans = preprocess_data()
    for i in range(len(ans)):
        print(f"{ans[i]:.4f}")


if __name__ == "__main__":
    main()
