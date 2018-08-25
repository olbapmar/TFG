import cv2
import os
from sklearn.cluster import MeanShift,KMeans , estimate_bandwidth
import numpy as np

os.chdir("features")

hog = cv2.HOGDescriptor((224,224),(16,16),(8,8),(8,8),9)

descriptores = []
nombres = []

for directorio in [x[0] for x in os.walk('.')]:
    if directorio != '.':
        os.chdir(os.path.normpath(directorio))
        #if not os.path.isdir("../../descriptores/"+directorio):
            #os.makedirs("../../descriptores/"+directorio)

        for f in os.listdir():
            img = cv2.imread(f)
            h = hog.compute(img)

            #fs_write = cv2.FileStorage("../../descriptores/"+directorio+'/'+f.split('.')[0]+'.yml', cv2.FILE_STORAGE_WRITE)
            #fs_write.write("descriptor", h)
            h = np.transpose(h)[0]
            descriptores.append(h)
            nombres.append(directorio + "_" + f.split('.')[0])


        os.chdir("..")

os.chdir("..")


print("Empieza el cluster")

clustering = MeanShift()
#clustering = KMeans(n_clusters=6)
clustering.fit(descriptores)

f = open("clusters_meanshift.txt", "w")

for i in range(len(clustering.labels_)):
    print(nombres[i] + ": " + str(clustering.labels_[i]))
    f.write(nombres[i] + ": " + str(clustering.labels_[i])+"\n")

f.close()