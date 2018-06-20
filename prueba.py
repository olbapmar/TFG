import keras
from vis.utils import utils
import numpy as np
from vis.visualization import get_num_filters
from vis.visualization import visualize_activation
from matplotlib import pyplot as plt
import os
from vis.input_modifiers import Jitter
import sys
import cv2

inicio = 0

if len(sys.argv) >= 2:
    inicio = int(sys.argv[1])

#Windows
import ctypes
ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

model = keras.applications.VGG16(weights='imagenet', include_top=True)

layer_idx = utils.find_layer_idx(model, 'predictions')

# Swap softmax with linear
model.layers[layer_idx].activation = keras.activations.linear
model = utils.apply_modifications(model)

model.summary()

if not os.path.isdir("features"):
    os.mkdir("features")


layer_names = ['block5_conv3']
for layer_name in layer_names:
    layer_idx = utils.find_layer_idx(model, layer_name)

    if not os.path.isdir("features/"+layer_name):
        os.mkdir("features/"+layer_name)

    # Visualize all filters in this layer.
    filters = np.arange(get_num_filters(model.layers[layer_idx]))

    size = len(filters)

    current = inicio
    vis_images = []
    while current < size:
        print(layer_name + " " + str(current))
        img_old = visualize_activation(model, layer_idx, filter_indices=current, input_modifiers=[Jitter(0.05)], tv_weight=0)
        img = visualize_activation(model, layer_idx, filter_indices=current, input_modifiers=[Jitter(0.05)], seed_input=img_old)
        # Utility to overlay text on image.
        #img = utils.draw_text(img, 'Filter {}'.format(idx))  

        #plt.imshow(img)
        #plt.axis('off')
        #plt.savefig("features/"+layer_name+"/"+str(current)+".png", dpi=200)
        cv2.imwrite("features/"+layer_name+"/"+str(current)+".png", img)
        current = current + 1


        #vis_images.append(img)

    # Generate stitched image palette with 8 cols.
    #stitched = utils.stitch_images(vis_images, cols=8)    
    #plt.imshow(stitched)
    #plt.title(layer_name)
    #plt.savefig(layer_name + ".png", dpi=3000)
    #plt.show()
