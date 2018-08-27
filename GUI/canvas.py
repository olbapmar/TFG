from tkinter import *
import PIL.Image, PIL.ImageTk

class MainCanvas():
    DEFAULT_SIZE = 112

    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(master=self.root.root,width=448, height=448)
        self.canvas.pack(side=TOP)
        self.canvas.bind('<Motion>', self.motion)
        self.canvas.bind('<MouseWheel>', self.zoom)
        self.canvas.bind('<Button>', self.click)
        self.has_image = False
        self.zoom_level=0

    def new_image(self, img):
        self.current_image = img
        self.canvas.create_image(0,0,image=img,anchor=NW)
        self.has_image = True

    def motion(self, event):
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

    def zoom(self, event):
        direction = -1 if event.delta > 1 else 1
        self.zoom_level = direction + self.zoom_level 
        if self.zoom_level < -3:
            self.zoom_level = -3
        if self.zoom_level > 1:
            self.zoom_level = 1
        self.motion(event)

    def click(self, event):
        if self.zoom_level == 1:
            self.root.keras_handler.whole_image()