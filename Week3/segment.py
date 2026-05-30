from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

model.predict(
    source="videos/raw.mp4",
    save=True
)