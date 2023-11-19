# GUI HW digits app

from tkinter import *
import tkinter as tk
from PIL import ImageGrab, Image
import numpy as np
import tkcap
import matplotlib.pyplot as plt
from keras.models import load_model
import time

model = load_model('HW_Digit_Recognizer.h5')




class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        
        # Creating elements
        self.canvas = tk.Canvas(self, width=300, height=300, bg = "white", cursor="cross")
        self.label = tk.Label(self, text="Thinking..", font=("Helvetica", 48))
        self.classify_btn = tk.Button(self, text = "Recognise") 
        self.button_clear = tk.Button(self, text = "Clear", command = self.clear_all)
        
        # Grid structure
        self.canvas.grid(row=0, column=0, pady=2, sticky=W, )
        self.label.grid(row=0, column=1,pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)        
        self.canvas.bind("<B1-Motion>", self.draw_lines)
        
    def clear_all(self):
        self.canvas.delete("all")
 
    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r=8
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='black')
        
app = App()
print(type(tkcap.CAP(app)))
def predict_digit():
    cap = tkcap.CAP(app)
    #cap.capture('window.png') # save picture
    
    img = cap.resize((28,28))
    img = img.convert('L')
    img = np.array(img)
    img = img.reshape(1,28,28,1)
    img = img/255.0
    
    res = model.predict([img])[0]
    print(res)
    return np.argmax(res), max(res)
time.sleep(10)
predict_digit()
mainloop()




        
        
        
        