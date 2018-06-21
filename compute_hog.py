import cv2
import os

os.chdir("features")


hog = cv2.HOGDescriptor((224,224),(16,16),(8,8),(8,8),9)

for directorio in [x[0] for x in os.walk('.')]:
    if directorio != '.':
        os.chdir(os.path.normpath(directorio))
        if not os.path.isdir("../../descriptores/"+directorio):
            os.makedirs("../../descriptores/"+directorio)

        for f in os.listdir():
            img = cv2.imread(f)
            h = hog.compute(img)

            fs_write = cv2.FileStorage("../../descriptores/"+directorio+'/'+f.split('.')[0]+'.yml', cv2.FILE_STORAGE_WRITE)
            fs_write.write("descriptor", h)
            fs_write.release()


        os.chdir("..")

