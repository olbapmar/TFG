import keras
import numpy as np
from keras.applications.vgg16 import preprocess_input, decode_predictions
import matplotlib.pyplot as plt
from vis.utils import utils
from vis.visualization import get_num_filters
from keras import backend as K
import cv2

class KerasHandler:
    def __init__(self):
        self.model = keras.applications.VGG16()

    def initialize(self,img):
        #Clasificacion
        img = np.expand_dims(img, axis=0)
        self.predictions = decode_predictions(self.model.predict(img))[:5][0]
        
        #Activacion de capas intermedias
        inp = self.model.input
        outputs = [layer.output for layer in self.model.layers]
        functor = K.function([inp], outputs)
        self.middle_layers = functor([img])

        self.max_per_layer = [np.amax(layer) for layer in self.middle_layers]

    def whole_image(self):
        
        plt.rcParams['toolbar'] = 'None'
        fig, ax = plt.subplots(num="Clasificacion de imagen")
        
        values = [round(t_uple[2]*100,2) for t_uple in self.predictions]
        y_pos = np.arange(len(self.predictions))
        names = [t_uple[1] for t_uple in self.predictions]

        ax.barh(y_pos, values, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(names)
        ax.invert_yaxis()
        plt.show()

    def get_useful_layers_names(self):
        names = [layer.name for layer in self.model.layers]
        names.pop(0)
        del names[-4:]
        return names

    def get_num_of_channels(self, name):
        idx = utils.find_layer_idx(self.model, name)
        return get_num_filters(self.model.layers[idx])

    def get_img_activations(self, name, filter):
        idx = utils.find_layer_idx(self.model, name)
        aux = self.middle_layers[idx][0,:,:,filter] * (255.0/np.amax(self.middle_layers[idx][0,:,:,filter]))#self.max_per_layer[idx])
        aux = np.expand_dims(aux, axis=2)
        aux = aux.astype(np.uint8)
        return cv2.resize(aux, (224,224))

    def get_activations(self, name, filter):
        idx = utils.find_layer_idx(self.model, name)
        aux = self.middle_layers[idx][0,:,:,filter] * (100/np.amax(self.middle_layers[idx][0,:,:,filter]))
        return aux
