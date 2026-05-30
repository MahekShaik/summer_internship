import cv2
import numpy as np

video_path = "videos/plant_video.mp4"
cap = cv2.VideoCapture(video_path)

ret, prev = cap.read()
if not ret:
    print("Error: Cannot read video")
    exit()

prev_gray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

motion_scores = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(prev_gray, gray)
    score = np.mean(diff)

    motion_scores.append(score)

    prev_gray = gray

cap.release()

motion_scores = np.array(motion_scores)

# smoothing
window = 5
smoothed = np.convolve(motion_scores, np.ones(window)/window, mode='valid')

stress_index = (np.mean(smoothed) - np.min(smoothed)) / (np.max(smoothed) - np.min(smoothed))

print("\nRESULTS")
print("Average Motion:", np.mean(smoothed))
print("Max Motion:", np.max(smoothed))
print("Stress Index:", round(stress_index, 3))

if stress_index > 0.6:
    print("HIGH STRESS (High wind effect)")
else:
    print("LOW STRESS (Stable condition)")

np.save("output/motion_scores.npy", smoothed)