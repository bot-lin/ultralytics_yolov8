
from ultralytics import YOLO

model = YOLO("best.pt")
path = model.export(format="onnx")