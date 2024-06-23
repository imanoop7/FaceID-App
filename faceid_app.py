from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.logger import Logger
import cv2
import tensorflow as tf
from layers import L1Dist
import os
import numpy as np



class camApp(App):

    def build(self):
        self.web_cam = Image(size_hint=(1,.8))
        self.button = Button(text="Verify",on_press = self.verfy, size_hint=(1,.1))
        self.verfication_label=Label(text="Verfication Label", size_hint=(1,.1))

        






    
if __name__ == '__main__':
    camApp().run()