import os
import random
import shutil

img_dir = r"C:\Users\tamta\OneDrive\Desktop\summer_internship\Week4\dataset\images\train"
val_dir = r"C:\Users\tamta\OneDrive\Desktop\summer_internship\Week4\dataset\images\val"

os.makedirs(val_dir, exist_ok=True)

images = os.listdir(img_dir)
random.shuffle(images)

split_ratio = 0.2  # 20% validation

val_count = int(len(images) * split_ratio)

val_images = images[:val_count]

for img in val_images:
    src = os.path.join(img_dir, img)
    dst = os.path.join(val_dir, img)
    shutil.move(src, dst)

print("Train images:", len(os.listdir(img_dir)))
print("Val images:", len(os.listdir(val_dir)))