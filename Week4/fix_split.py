import os
import shutil
import random

base = r"C:\Users\tamta\OneDrive\Desktop\summer_internship\Week4\dataset"

# IMPORTANT: folder has space "final dataset"
src = os.path.join(base, "images", "final dataset")

img_train = os.path.join(base, "images", "train")
img_val   = os.path.join(base, "images", "val")

lbl_train = os.path.join(base, "labels", "train")
lbl_val   = os.path.join(base, "labels", "val")

os.makedirs(img_train, exist_ok=True)
os.makedirs(img_val, exist_ok=True)
os.makedirs(lbl_train, exist_ok=True)
os.makedirs(lbl_val, exist_ok=True)

images = [f for f in os.listdir(src) if f.endswith(".jpg") or f.endswith(".png")]
random.shuffle(images)

split = int(0.8 * len(images))

train_imgs = images[:split]
val_imgs = images[split:]

def copy_files(file_list, img_dir, lbl_dir):
    for f in file_list:
        img_path = os.path.join(src, f)
        label_path = os.path.join(base, "labels", f.rsplit(".",1)[0] + ".txt")

        shutil.copy(img_path, img_dir)

        if os.path.exists(label_path):
            shutil.copy(label_path, lbl_dir)

copy_files(train_imgs, img_train, lbl_train)
copy_files(val_imgs, img_val, lbl_val)

print("DONE: Dataset split successful")