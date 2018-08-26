from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import cv2
import PIL.Image, PIL.ImageTk
from main_canvas import MainCanvas

class MainWindow():
    def __init__(self):
        self.root = Tk()
        self.root.title("TFG Pablo Pastor Martín")
        self.root.resizable(0,0)

        menubar = Menu(self.root)
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Open image", command=self.openfile)
        menubar.add_cascade(label="File...", menu=menu1)
        menu2 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=menu2)
        menu2.add_command(label="About...", command=self.info)

        self.root.config(menu=menubar)

        self.mainCanvas = MainCanvas(self.root) 

        self.root.mainloop()

    def openfile(self):
        path = filedialog.askopenfilename(title="Select image")
        if path is not "":
            self.img = cv2.cvtColor(cv2.imread(path),cv2.COLOR_BGR2RGB)
            self.mainCanvas.new_image(PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2.resize(self.img, (448,448)))))
    
    def info(self):
        messagebox.showinfo("About",
                            "Trabajo de Fin de Grado de Pablo Pastor Martín \
                            \nUniversidad de La Laguna")

def main():
    MainWindow()

if __name__ == "__main__":
    main()