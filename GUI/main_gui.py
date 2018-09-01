from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import cv2
import PIL.Image, PIL.ImageTk
from canvas import MainCanvas
from keras_handler import KerasHandler
from visualize_filter import VisualizeFilter
from config_parser import ConfigParser
from tkinter import ttk
from bottom_combos import BottomCombos

class MainWindow():
    def __init__(self):
        self.keras_handler = KerasHandler()

        self.filters_config = ConfigParser.parse("GUI/filters.json")

        self.root = Tk()
        self.root.title("TFG Pablo Pastor Martín")
        self.root.resizable(0,0)
        menubar = Menu(self.root)
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Open image", command=self.openfile)
        menubar.add_cascade(label="File...", menu=menu1)
        menu2 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Visualizar", menu=menu2)
        menu2.add_command(label="Filtro", command=self.visualize_filter)
        menu3 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=menu3)
        menu3.add_command(label="About...", command=self.info)
        self.root.config(menu=menubar)
        self.mainCanvas = MainCanvas(self) 

        self.create_combos()

        self.root.mainloop()

    def openfile(self):
        path = filedialog.askopenfilename(title="Select image")
        if path is not "":
            img = cv2.imread(path)
            img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.mainCanvas.new_image(PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2.resize(img2, (448,448)))))
            self.keras_handler.initialize(cv2.resize(img, (224,224)))

    def info(self):
        messagebox.showinfo("About",
                            "Trabajo de Fin de Grado de Pablo Pastor Martín \
                            \nUniversidad de La Laguna")

    def visualize_filter(self):
        VisualizeFilter(self)

    def create_combos(self):
        BottomCombos(self)


def main():
    MainWindow()

if __name__ == "__main__":
    main()