from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

# 加载模型
model = tf.keras.models.load_model('/model/mnist_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    # 获取请求中的图片数据
    image = request.json['image']
    # 预处理数据
    prediction = model.predict([image])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

