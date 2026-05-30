import cv2
import os

video_path = "../dataset/video.mp4"
output_train = "../dataset/images/train"

os.makedirs(output_train, exist_ok=True)

cap = cv2.VideoCapture(video_path)

count = 0
saved = 0
frame_skip = 5

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if count % frame_skip == 0:
        cv2.imwrite(f"{output_train}/img_{saved:05d}.jpg", frame)
        saved += 1

    count += 1

cap.release()
print("Done frames:", saved)