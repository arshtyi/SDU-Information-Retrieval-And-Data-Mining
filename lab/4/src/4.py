import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(list(map(float, input().split())))
    k = int(input().strip())

    y = [data[i][m] for i in range(n)]
    mean_y = sum(y) / n
    dy = [y[i] - mean_y for i in range(n)]
    den_y = sum(d * d for d in dy) ** 0.5

    results = []
    for j in range(m):
        x = [data[i][j] for i in range(n)]
        mean_x = sum(x) / n
        dx = [x[i] - mean_x for i in range(n)]
        den_x = sum(d * d for d in dx) ** 0.5
        num = sum(dx[i] * dy[i] for i in range(n))
        corr = num / (den_x * den_y) if den_x * den_y > 0 else 0.0
        results.append((j, corr))

    results.sort(key=lambda t: (-t[1], t[0]))
    for idx, corr in results:
        print(f"{idx} {corr:.4f}")


main()
