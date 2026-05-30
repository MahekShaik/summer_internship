import os
import shutil

BASE_PATH = r"C:\Users\tamta\OneDrive\Desktop\summer_internship\week5\dataset"

IMG_DIR = os.path.join(BASE_PATH, "images", "train")
LABEL_DIR = os.path.join(BASE_PATH, "label", "train")

images = [f for f in os.listdir(IMG_DIR) if f.endswith(".jpg")]

fixed = 0
missing = 0

for img in images:
    # YOLO label name requirement
    clean_name = os.path.splitext(img)[0].replace(" (2)", "")
    label_name = clean_name + ".txt"

    label_path = os.path.join(LABEL_DIR, label_name)

    # If label exists already → OK
    if os.path.exists(label_path):
        continue

    # Try alternative matches
    alt1 = os.path.join(LABEL_DIR, os.path.splitext(img)[0] + ".txt")
    alt2 = os.path.join(LABEL_DIR, clean_name + ".txt")

    if os.path.exists(alt1):
        shutil.copy(alt1, label_path)
        print(f"✔ Fixed: {alt1} → {label_path}")
        fixed += 1

    elif os.path.exists(alt2):
        shutil.copy(alt2, label_path)
        print(f"✔ Fixed: {alt2} → {label_path}")
        fixed += 1

    else:
        print(f"❌ Still missing: {label_path}")
        missing += 1

print("\n====================")
print("Fixed labels:", fixed)
print("Still missing:", missing)
print("====================")