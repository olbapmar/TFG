import keras
import numpy as np
import cv2
import sys
import os 
from vis.utils import utils
from vis.visualization import get_num_filters

if not os.path.exists("single_neuron/block1_conv1"):
    os.makedirs("single_neuron/block1_conv1")

model = keras.applications.VGG16()

layer_idx = utils.find_layer_idx(model, 'block1_conv1')

num_filters = get_num_filters(model.layers[layer_idx])

print(model.layers[layer_idx].get_weights()[0].shape)

max_v = np.amax(model.layers[layer_idx].get_weights()[0])
min_v = np.amin(model.layers[layer_idx].get_weights()[0])

print(max_v)
print(min_v)

pesos = model.layers[layer_idx].get_weights()[0].copy()
if min_v < 0:
    pesos = pesos + abs(min_v)
    max_v = max_v + abs(min_v)

pesos = pesos*(255.0/max_v)

r = pesos[:,:,0,:]
g = pesos[:,:,1,:]
b = pesos[:,:,2,:]

for i in range(0, num_filters):
    img = np.arange(27).reshape((3,3,3))
    img[:,:,2] = b[:,:,i]
    img[:,:,1] = g[:,:,i]
    img[:,:,0] = r[:,:,i]
    img = cv2.resize(img,(99,99), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite("single_neuron/block1_conv1/"+str(i)+".png", img)
    print(img)



