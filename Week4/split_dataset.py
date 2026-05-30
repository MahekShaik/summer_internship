import os
import shutil
import random

base = r"C:\Users\tamta\OneDrive\Desktop\summer_internship\Week4\dataset"

img_src = os.path.join(base, "images")
lbl_src = os.path.join(base, "labels")

img_train = os.path.join(base, "images", "train")
img_val   = os.path.join(base, "images", "val")

lbl_train = os.path.join(base, "labels", "train")
lbl_val   = os.path.join(base, "labels", "val")

os.makedirs(img_train, exist_ok=True)
os.makedirs(img_val, exist_ok=True)
os.makedirs(lbl_train, exist_ok=True)
os.makedirs(lbl_val, exist_ok=True)

images = [f for f in os.listdir(img_src) if f.endswith(".jpg") or f.endswith(".png")]
random.shuffle(images)

split = int(0.8 * len(images))

train_imgs = images[:split]
val_imgs = images[split:]

def move(files, img_dir, lbl_dir):
    for f in files:
        img_path = os.path.join(img_src, f)
        lbl_path = os.path.join(lbl_src, f.rsplit(".",1)[0] + ".txt")

        if os.path.exists(img_path):
            shutil.move(img_path, img_dir)

        if os.path.exists(lbl_path):
            shutil.move(lbl_path, lbl_dir)

move(train_imgs, img_train, lbl_train)
move(val_imgs, img_val, lbl_val)

print("DONE: YOLO dataset split completed")