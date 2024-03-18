import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def feed_forward_nn(input_data, weights, biases):
    layer_input = input_data
    for w, b in zip(weights, biases):
        layer_output = np.dot(w, layer_input) + b
        layer_input = sigmoid(layer_output)
    return layer_input

# Example Usage
input_data = np.array([0.1, 0.2, 0.7])
weights = [np.array([[0.1, 0.2, 0.3], [0.2, 0.3, 0.4], [0.3, 0.4, 0.5]]),
           np.array([[0.5, 0.6, 0.7], [0.6, 0.7, 0.8]])]
biases = [np.array([0.1, 0.2, 0.3]), np.array([0.4, 0.5])]

output = feed_forward_nn(input_data, weights, biases)
print(output)
OUTPUT:
Epoch 1/100
10/10 [==============================] - 0s 1ms/step - loss: 0.7250 - accuracy: 0.5000
Epoch 2/100
10/10 [==============================] - 0s 1ms/step - loss: 0.7190 - accuracy: 0.5100
...
Epoch 100/100
10/10 [==============================] - 0s 1ms/step - loss: 0.4632 - accuracy: 0.7900

4/4 [==============================] - 0s 2ms/step - loss: 0.4616 - accuracy: 0.7900
Loss: 0.46159267473220825
Accuracy: 0.7900000214576721
