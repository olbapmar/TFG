from keras import backend as K
import keras
import cv2
import numpy as np

model = keras.applications.VGG16()

inp = model.input                                           
outputs = [layer.output for layer in model.layers]          
functor = K.function([inp] , outputs ) 

# Testing
img = cv2.imread("features/block2_conv1/8.png", 1)
img = np.expand_dims(img, axis=0)
layer_outs = functor([img])
print(layer_outs[1][0,0,0,1])