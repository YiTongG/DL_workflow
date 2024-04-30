from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

model = tf.keras.models.load_model('/model/mnist_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    image = request.json['image']
    prediction = model.predict([image])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

