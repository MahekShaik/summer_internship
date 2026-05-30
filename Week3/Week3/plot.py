import numpy as np
import matplotlib.pyplot as plt

data = np.load("output/motion_scores.npy")

plt.plot(data)
plt.title("Crop Motion Trend (Smoothed)")
plt.xlabel("Frame")
plt.ylabel("Motion Intensity")

plt.grid()
plt.savefig("output/motion_plot.png")
plt.show()