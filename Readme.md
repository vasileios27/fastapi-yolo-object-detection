# YOLOv8 Object Detection API with FastAPI

This repository provides a RESTful API to perform object detection using the YOLOv8 model, built with [FastAPI](https://fastapi.tiangolo.com/). The project is inspired by the Medium article ["Step-on-Step Guide to Deploy YOLO Model Using FastAPI"](https://medium.com/latinxinai/step-on-step-guide-to-deploy-yolo-model-using-fastapi-1a764dbd270d).

## Features

- **Upload Images**: Accepts images via POST requests.
- **Object Detection**: Detects objects in the uploaded image using the YOLOv8 model.
- **API Response**: Returns detected objects with their class, confidence scores, and bounding box coordinates.

## How It Works

1. The application uses the `ultralytics` library to load a YOLOv8 pre-trained model (`yolov8n.pt`).
2. Images are uploaded to the `/detect/` endpoint.
3. YOLOv8 processes the image and identifies objects.
4. The API responds with detection results, including:
   - Object class
   - Confidence score
   - Bounding box coordinates

## Requirements

- **Python**: 3.8 or later
- **Dependencies**:
  - FastAPI
  - OpenCV
  - NumPy
  - Ultralytics

Install all dependencies via the provided `requirements.txt`.

## Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/vasileios27/fastapi-yolo-object-detection.git
cd fastapi-yolo-object-detection

### 2. Install Dependencies
```bash
pip install -r requirements.txt

### 3. Run the Application
Start the server using uvicorn:
```bash
uvicorn app.main:app --reload

### 4. Test the API
Access the root endpoint at http://127.0.0.1:8000/ to verify the server is running.
Use the /detect/ endpoint to perform object detection.
Example Request
Using curl:

bash
Copy
Edit
curl -X POST "http://127.0.0.1:8000/detect/" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@path_to_image.jpg"
