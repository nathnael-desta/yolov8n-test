from ultralytics import YOLO

#Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# run infernce on the source
results = model(source='gymnasts.mp4', show=True, conf=0.4, save=True) # generator of Results objects

