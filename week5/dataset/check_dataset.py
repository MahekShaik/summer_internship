import os

# Update this to your dataset path
BASE_PATH = r"C:\Users\tamta\OneDrive\Desktop\summer_internship\week5\dataset"

IMG_DIRS = [
    os.path.join(BASE_PATH, "images", "train"),
    os.path.join(BASE_PATH, "images", "val")
]

# Note: folder is "label", not "labels"
LABEL_DIRS = [
    os.path.join(BASE_PATH, "label", "train"),
    os.path.join(BASE_PATH, "label", "val")
]

def check_dataset():
    total_images = 0
    missing_labels = []
    empty_labels = []

    for img_dir, lbl_dir in zip(IMG_DIRS, LABEL_DIRS):
        print(f"\nChecking:\nImages: {img_dir}\nLabels: {lbl_dir}\n")

        if not os.path.exists(img_dir):
            print("❌ Image folder missing:", img_dir)
            continue

        if not os.path.exists(lbl_dir):
            print("❌ Label folder missing:", lbl_dir)
            continue

        images = [f for f in os.listdir(img_dir) if f.endswith((".jpg", ".png", ".jpeg"))]

        for img in images:
            total_images += 1

            label_file = os.path.splitext(img)[0] + ".txt"
            label_path = os.path.join(lbl_dir, label_file)

            # Check missing label
            if not os.path.exists(label_path):
                missing_labels.append(label_path)
                continue

            # Check empty label
            if os.path.getsize(label_path) == 0:
                empty_labels.append(label_path)

    print("\n================ RESULTS ================\n")

    print(f"Total images checked: {total_images}")

    print(f"\nMissing labels: {len(missing_labels)}")
    for m in missing_labels[:10]:
        print(" -", m)

    print(f"\nEmpty labels: {len(empty_labels)}")
    for e in empty_labels[:10]:
        print(" -", e)

    if len(missing_labels) == 0 and len(empty_labels) == 0:
        print("\n✅ Dataset is PERFECT for YOLO training!")
    else:
        print("\n⚠️ Fix missing/empty labels before training!")

if __name__ == "__main__":
    check_dataset()