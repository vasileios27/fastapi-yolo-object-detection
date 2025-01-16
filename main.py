# from fastapi import FastAPI

# import cv2
# import numpy as np
# from ultralytics import YOLO
# from fastapi import File, UploadFile
# model = YOLO("yolov8n.pt")

# app = FastAPI()

# @app.get("/")
# async def read_root():
#  return {"message": "Hello, World!"}



# @app.post("/detect/")
# async def detect_objects(file: UploadFile):
#  # Process the uploaded image for object detection
#  image_bytes = await file.read()
#  image = np.frombuffer(image_bytes, dtype=np.uint8)
#  image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
#  # Perform object detection with YOLOv8
#  detections = model.predict(image)
 
#  return {"detections": detections}



from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.post("/detect/")
async def detect_objects(file: UploadFile):
    # Process the uploaded image for object detection
    image_bytes = await file.read()
    image = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    # Perform object detection with YOLOv8
    results = model.predict(image)
    
    # Extract relevant data from detections
    detections = []
    for result in results:
        for box in result.boxes:
            detections.append({
                "class": box.cls.item(),  # Class ID
                "confidence": box.conf.item(),  # Confidence score
                "box": box.xyxy.tolist()  # Bounding box [x1, y1, x2, y2]
            })
    
    return {"detections": detections}
