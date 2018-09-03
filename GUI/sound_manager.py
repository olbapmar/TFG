from pysine import PySine
from threading import Thread
from time import sleep

class SoundManager:
    
    def __init__(self):
        self.pysine = PySine()

    def sound_new(self, frequency, duration):
        self.pysine.sine(frequency, duration)