from flask import Flask, request
from ultralytics import YOLO
from PIL import Image
import io

app = Flask(__name__)
model = YOLO("yolov8n.pt")  # Pretrained model

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        image = Image.open(io.BytesIO(request.files['image'].read()))
        results = model(image)
        labels = [model.names[int(cls)] for cls in results[0].boxes.cls]
        print("Detected:", labels)
        return {"detected": labels}
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

