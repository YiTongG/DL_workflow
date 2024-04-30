import numpy as np
from PIL import Image
import requests
import json

def prepare_image(image_path):
    img = Image.open(image_path).convert('L')  # 
    img = img.resize((28, 28))  #  28x28
    img_array = np.array(img)  #  NumPy 
    img_array = img_array / 255.0  #  0-1
    img_array = img_array.tolist()  # JSON 
    return img_array

def send_request(image_data, url):
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({"image": image_data})
    response = requests.post(url, data=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    image_path = '1.jpg'  # path to the image
    inference_url = 'http://34.69.143.226/predict'  # url for the outer ip

    image_data = prepare_image(image_path)

    result = send_request(image_data, inference_url)
    print("Inference result:", result)

