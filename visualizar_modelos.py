import keras
from keras.utils import plot_model

model1 = keras.applications.vgg16.VGG16()
model2 = keras.applications.inception_v3.InceptionV3()

plot_model(model1, to_file='vgg.png')
plot_model(model2, to_file='inceptionv3.png')