from ultralytics import YOLO

<<<<<<< HEAD
model = YOLO("yolov8n.pt")

model.predict(
    source="videos/raw.mp4",
    save=True
)
=======
# Load pretrained YOLO model
model = YOLO("yolo11n.pt")

# Run object detection on sample image
results = model("https://ultralytics.com/images/bus.jpg", save=True)

print("Detection completed!")
>>>>>>> d8411c0ea479573c87b8842a6a512eccca9e8f16
