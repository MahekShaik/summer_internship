from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.predict(
    source="videos/raw.mp4",
    save=True
)