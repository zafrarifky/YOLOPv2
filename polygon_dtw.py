import numpy as np
# from polygon_dtw import dtw
from fastdtw import fastdtw
import matplotlib.pyplot as plt

# Load the matrix from the .npy file
polygon1 = np.load("chart_matrix1.npy")
polygon2 = np.load("chart_matrix2.npy")

# alignment = dtw(polygon1, polygon2)

# print(f"DTW Distance: {alignment.distance}")


dtw_distance_value, alignment_path = fastdtw(polygon1, polygon2)
print("Alignment Path:", alignment_path)
print("DTW Distance:", dtw_distance_value)


# Create a new plot
plt.figure(figsize=(10, 8))

# Plot the points from curve1 and polygon2
plt.scatter(polygon1[:, 0], polygon1[:, 1], c='red', label='Curve 1', marker='o')
plt.scatter(polygon2[:, 0], polygon2[:, 1], c='blue', label='Curve 2', marker='x')

# Plot the alignment path
aligned_points_polygon1 = [polygon1[i] for i, _ in alignment_path]
aligned_points_polygon2 = [polygon2[j] for _, j in alignment_path]
plt.plot(
    [point[0] for point in aligned_points_polygon1],
    [point[1] for point in aligned_points_polygon1],
    color='green',
    linestyle='dashed',
    label='Alignment Path'
)

# Customize the plot
plt.title("Curves Alignment with DTW")
plt.legend()
plt.show()
