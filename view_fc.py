from keras.applications import VGG16
from vis.utils import utils
from keras import activations
from vis.visualization import visualize_activation
from matplotlib import pyplot as plt
from vis.input_modifiers import Jitter
import numpy as np
import os
import cv2

categorias = np.random.permutation(1000)[:15]

model = VGG16(weights='imagenet', include_top=True)
layer_idx = utils.find_layer_idx(model, 'predictions') # -1 tambien vale (es la ultima)

#Softmax a linear

model.layers[layer_idx].activation = activations.linear
model = utils.apply_modifications(model)

if not os.path.isdir("fc"):
    os.mkdir("fc")

for categoria in categorias:
    img = visualize_activation(model, layer_idx, filter_indices=categoria,max_iter=500, input_modifiers=[Jitter(16)])
    img = utils.draw_text(img, utils.get_imagenet_label(categoria))
    cv2.imwrite("fc/" + utils.get_imagenet_label(categoria)+ ".png", img)