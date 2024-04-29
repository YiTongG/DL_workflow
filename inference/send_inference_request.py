import numpy as np
from PIL import Image
import requests
import json

def prepare_image(image_path):
    """加载图像，转换大小，归一化像素值"""
    img = Image.open(image_path).convert('L')  # 转换为灰度图像
    img = img.resize((28, 28))  # 调整图像大小为 28x28
    img_array = np.array(img)  # 转换为 NumPy 数组
    img_array = img_array / 255.0  # 归一化到 0-1
    img_array = img_array.tolist()  # 转换回列表以便进行 JSON 序列化
    return img_array

def send_request(image_data, url):
    """发送 POST 请求到模型推理服务"""
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({"image": image_data})
    response = requests.post(url, data=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    image_path = '1.jpg'  # 图像文件路径
    inference_url = 'http://34.69.143.226/predict'  # 推理服务的 URL

    # 准备图像数据
    image_data = prepare_image(image_path)

    # 发送请求并获取推理结果
    result = send_request(image_data, inference_url)
    print("Inference result:", result)

