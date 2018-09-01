from tkinter import ttk
from tkinter import *

class BottomCombos:
    def __init__(self, root):
        self.root = root
        frame = ttk.Frame(self.root.root)
        self.combo_block = ttk.Combobox(frame,state="readonly")
        self.combo_feature = ttk.Combobox(frame,state="disabled")
        frame.pack(side=BOTTOM)
        self.combo_block.grid(column=0, row=0)
        self.combo_feature.grid(column=1, row=0)
        
        self.config = root.filters_config

        blocks_values = ["Bloque " + aux for aux in self.config] + ["Clasificar"]
        self.combo_block["values"] = blocks_values
        self.combo_block.bind("<<ComboboxSelected>>", self.block_selected)
        self.combo_feature.bind("<<ComboboxSelected>>", self.filter_selected)


    def block_selected(self, event):
        if self.combo_block.get().startswith("Bloque"):
            index = self.combo_block.get().replace("Bloque ", "")
            self.combo_feature["values"] = [value for value in self.config[index]]
            self.combo_feature["state"] = "readonly"
            self.current_block = index
        else:
            self.combo_feature["state"] = "disabled"

    def filter_selected(self, event):
        filt = self.config[self.current_block][self.combo_feature.get()]
        layer, number = filt.split(":")
        number = int(number)

    