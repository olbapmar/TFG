from tkinter import *
import PIL.Image, PIL.ImageTk
from sound_manager import SoundManager

class MainCanvas():
    DEFAULT_SIZE = 448
    INPUT_SIZE = 224

    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(master=self.root.root,width=448, height=448)
        self.canvas.pack(side=TOP)
        self.canvas.bind('<Motion>', self.motion)
        #self.canvas.bind('<MouseWheel>', self.zoom)
        self.canvas.bind('<Button-1>', self.click)
        self.canvas.bind('<B1-Motion>', self.click)
        self.has_image = False
        self.zoom_level=0
        self.sound = SoundManager()

    def new_image(self, img):
        self.current_image = img
        self.canvas.create_image(0,0,image=img,anchor=NW)
        self.has_image = True

    def motion(self, event):
        '''
        if self.has_image:
            self.canvas.delete("all")
            self.canvas.create_image(0,0,image=self.current_image,anchor=NW)

            size = MainCanvas.DEFAULT_SIZE * 2**self.zoom_level
            x = event.x - size
            y = event.y - size

            x = max(1, x)
            y = max(1, y)

            if x >= self.canvas.winfo_width() - size*2:
                x = self.canvas.winfo_width() - size*2
            if y >= self.canvas.winfo_height() - size*2:
                y = self.canvas.winfo_height() - size*2

            self.canvas.create_rectangle(x,y,x+size*2,y+size*2, width=3)
            self.current_pos = [x,y]
        '''
        if self.has_image and self.zoom_level >= 0:
            self.canvas.delete("all")
            self.canvas.create_image(0,0,image=self.current_image, anchor=NW)

            size = MainCanvas.DEFAULT_SIZE/MainCanvas.INPUT_SIZE * (2**self.zoom_level)
            x = event.x
            y = event.y
            x0 = round((event.x + 0.0)/size) * size
            y0 = round((event.y + 0.0)/size) * size

            self.canvas.create_rectangle(x0,y0,x0 + size, y0 + size)

    '''
    def zoom(self, event):
        direction = -1 if event.delta > 1 else 1
        self.zoom_level = direction + self.zoom_level 
        if self.zoom_level < -3:
            self.zoom_level = -3
        if self.zoom_level > 1:
            self.zoom_level = 1
        self.motion(event)
    '''

    def click(self, event):
        if self.has_image:
            if self.zoom_level == -1:
                self.root.keras_handler.whole_image()
            else:
                self.motion(event)
                x, y = self.change_coords(event.x, event.y)
                print(x, y, self.target[int(y)][int(x)])
                if self.target[int(y)][int(x)] > 10:
                    frequency = 400 + 14*self.target[int(y)][int(x)]
                    self.sound.sound_new(frequency=frequency, duration=0.05)


    def new_target_activation(self, activations):
        self.target = activations

    def change_coords (self, x, y):
        x = x/ (MainCanvas.DEFAULT_SIZE/MainCanvas.INPUT_SIZE)
        y = y/ (MainCanvas.DEFAULT_SIZE/MainCanvas.INPUT_SIZE)
        size =  (2**self.zoom_level)
        x0 = round((x + 0.0)/size) * size
        y0 = round((y + 0.0)/size) * size
        return x0 / 2**self.zoom_level,y0/2**self.zoom_level