import keras
from vis.utils import utils
from keras import activations
import numpy as np
from vis.visualization import get_num_filters
from vis.visualization import visualize_activation
from matplotlib import pyplot as plt

model = keras.applications.VGG16(weights='imagenet', include_top=True)

layer_idx = utils.find_layer_idx(model, 'predictions')

# Swap softmax with linear
model.layers[layer_idx].activation = activations.linear
model = utils.apply_modifications(model)

model.summary()


layer_names = ['block4_conv1','block4_conv1','block4_conv3',
                'block5_conv1','block5_conv2','block5_conv3']
for layer_name in layer_names:
    layer_idx = utils.find_layer_idx(model, layer_name)

    # Visualize all filters in this layer.
    filters = np.arange(get_num_filters(model.layers[layer_idx]))

    vis_images = []
    for idx in filters:
        img = visualize_activation(model, layer_idx, filter_indices=idx)
        
        # Utility to overlay text on image.
        img = utils.draw_text(img, 'Filter {}'.format(idx))    
        vis_images.append(img)

    # Generate stitched image palette with 8 cols.
    stitched = utils.stitch_images(vis_images, cols=8)    
    plt.axis('off')
    plt.imshow(stitched)
    plt.title(layer_name)
    plt.savefig(layer_name + ".png", dpi=1500)
    #plt.show()
