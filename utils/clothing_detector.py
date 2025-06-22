import requests
from io import BytesIO

def detect_clothing(image_file):
    """
    업로드된 이미지(BytesIO 또는 File-like 객체)를 Roboflow API로 전송하여 의류 종류 감지
    """
    url = "https://detect.roboflow.com/fashion-detection-9tba0/2"
    params = {
        "api_key": "##"
    }
    files = {
        "file": ("image.jpg", image_file, "image/jpeg")
    }
    
    response = requests.post(url, files=files, params=params)
    predictions = response.json().get("predictions", [])
    
    return list(set([p["class"] for p in predictions]))
