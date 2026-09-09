import numpy as np


def k_means_clustering(points, k, initial_centroids, max_iterations):
    points = np.array(points, dtype=float)
    centroids = np.array(initial_centroids, dtype=float)
    for _ in range(max_iterations):
        distances = np.linalg.norm(points[:, np.newaxis, :] - centroids[np.newaxis, :, :], axis=2)
        labels = np.argmin(distances, axis=1)
        new_centroids = centroids.copy()
        for i in range(k):
            cluster_points = points[labels == i]
            if len(cluster_points) > 0:
                new_centroids[i] = np.mean(cluster_points, axis=0)
        if np.allclose(centroids, new_centroids):
            centroids = new_centroids
        centroids = new_centroids
    return [tuple(np.round(centroid, 4)) for centroid in centroids]


def main():
    # Read input for points
    points = eval(input())

    # Read input for number of clusters
    k = int(input())

    # Read input for initial centroids
    initial_centroids = eval(input())

    # Read input for maximum iterations
    max_iterations = int(input())

    # Perform k-Means clustering
    final_centroids = k_means_clustering(points, k, initial_centroids, max_iterations)

    # Print the final centroids
    print(final_centroids)


if __name__ == "__main__":
    main()
