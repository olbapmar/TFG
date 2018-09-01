from tkinter import *
from tkinter import ttk
import numpy as np
import PIL.Image, PIL.ImageTk
import cv2

class VisualizeFilter():
    def __init__(self, root):
        self.root = root

        self.dialog = Toplevel()

        self.dialog.geometry("300x200+50+50")
        self.dialog.title("Dialogo de filtro")
        self.dialog.resizable(0,0)

        label1 = Label(self.dialog, text="Please, choose layer:", anchor="w")
        label1.pack(side=TOP)

        self.combo = ttk.Combobox(self.dialog,state="readonly")
        self.combo["values"] = root.keras_handler.get_useful_layers_names()
        self.combo.pack(side=TOP)
        self.combo.bind("<<ComboboxSelected>>", self.new_selected)

        self.label2 = Label(self.dialog, text="", anchor="w")
        self.label2.pack(side=TOP)

        self.entry_value = StringVar()
        filter = Entry(self.dialog, width=3, textvariable=self.entry_value)
        filter.pack(side=TOP)
        self.entry_value.trace("w", self.filtermodified)

        self.button = Button(self.dialog, text="Ok", command=self.ok)
        self.button['state'] = DISABLED
        self.button.pack(side=BOTTOM)

    def new_selected(self, event):
        current = self.combo.get()
        self.max = self.root.keras_handler.get_num_of_channels(current) - 1
        self.label2['text'] = "Choose filter (0-" + str(self.max) + ")"

    def filtermodified(self, _, __, ___):
        if self.entry_value.get().isdigit() and int(self.entry_value.get()) <= self.max:
            self.button["state"] = ACTIVE
        else:
            self.button['state'] = DISABLED

    def ok(self):
        img = self.root.keras_handler.get_img_activations(self.combo.get(),int(self.entry_value.get()))
        self.canvas_frame = Toplevel()
        self.canvas_frame.title(self.combo.get() + ":" + self.entry_value.get())
        self.canvas = Canvas(self.canvas_frame, width=224, height=224)
        self.canvas.pack(side=TOP)
        self.img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
        self.canvas.create_image(0,0,image=self.img,anchor=NW)
        self.dialog.destroy()

        