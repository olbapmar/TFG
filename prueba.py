import keras
from vis.utils import utils
import numpy as np
from vis.visualization import get_num_filters
from vis.visualization import visualize_activation
from matplotlib import pyplot as plt
import os
from vis.input_modifiers import Jitter

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


layer_names = ['block4_conv2','block4_conv3','block5_conv1','block5_conv2','block5_conv3',]
for layer_name in layer_names:
    layer_idx = utils.find_layer_idx(model, layer_name)

    if not os.path.isdir("features/"+layer_name):
        os.mkdir("features/"+layer_name)

    # Visualize all filters in this layer.
    filters = np.arange(get_num_filters(model.layers[layer_idx]))

    vis_images = []
    for i, idx in enumerate(filters):
        img_old = visualize_activation(model, layer_idx, filter_indices=idx, input_modifiers=[Jitter(0.05)], tv_weight=0)
        img = visualize_activation(model, layer_idx, filter_indices=idx, input_modifiers=[Jitter(0.05)], seed_input=img_old)
        # Utility to overlay text on image.
        #img = utils.draw_text(img, 'Filter {}'.format(idx))  

        plt.imshow(img)
        plt.axis('off')
        plt.savefig("features/"+layer_name+"/"+str(idx)+".png", dpi=200)



        #vis_images.append(img)

    # Generate stitched image palette with 8 cols.
    #stitched = utils.stitch_images(vis_images, cols=8)    
    #plt.imshow(stitched)
    #plt.title(layer_name)
    #plt.savefig(layer_name + ".png", dpi=3000)
    #plt.show()
