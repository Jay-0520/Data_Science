import numpy as np
import tkinter as tk
from tkinter import filedialog
from tensorflow.keras.preprocessing.image import img_to_array,array_to_img
import sys
import os
from PIL import ImageTk, Image


class MainApp(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        # some parameters
        self.basewidth = 250
        
        # add welcome text
        self.welcometext = Label(root, text="Hello! Welcome to our GAN model!")
        self.welcometext.place(x=50, y=5)

        # add paramters 01,02,03,04,05,06
        self.para01_lbl = tk.Label(root, text="parameter01").place(x=10,y=300)
        self.para01=tk.Spinbox(root, from_=1, to=50, width=10)
        self.para01.place(x=10,y=320)
        self.para02_lbl = tk.Label(root, text="parameter02").place(x=180,y=300)
        self.para02=tk.Spinbox(root, from_=1, to=50, width=10)
        self.para02.place(x=180,y=320)
        self.para03_lbl = tk.Label(root, text="parameter03").place(x=350,y=300)
        self.para03=tk.Spinbox(root, from_=1, to=50, width=10)
        self.para03.place(x=350,y=320)
        
        self.para04_lbl = tk.Label(root, text="parameter04").place(x=10,y=360)
        self.para04=tk.Entry(root,width=10)
        self.para04.place(x=10,y=380)
        self.para04.insert(0,0)
        self.para05_lbl = Label(root, text="parameter05").place(x=180,y=360)
        self.para05 = Entry(root,width=10)
        self.para05.place(x=180,y=380)
        self.para05.insert(0,0)
        self.para06_lbl = Label(root, text="parameter06").place(x=350,y=360)
        self.para06 = Entry(root,width=10)
        self.para06.place(x=350,y=380)
        self.para06.insert(0,0)
        
        # add help button
        self.btn_help = Button(root, text="Help", padx=10,pady=0,width=3, bg="green", fg="black", command=self.help_).place(x=400,y=470)
        # add run button
        self.btn_run = Button(root, text="Run", padx=10,pady=0,width=3, bg="green", fg="black", command=self.run_).place(x=160,y=470)
        # add reset button
        self.btn_reset = Button(root, text="Reset", padx=10,pady=0,width=3, bg="green", fg="black", command=self.reset_).place(x=240,y=470)
        # add quit button
        self.btn_quit = Button(root, text="Quit", padx=10,pady=0,width=3, bg="green", fg="black", command=quit).place(x=320,y=470)
        # add Load_image button
        self.btn_loadimage = Button(root, text="Load image",padx=10,pady=0,width=6, bg="green", fg="black", command=self.load_img)
        self.btn_loadimage.place(x=10,y=48)

        # add a frame on the root windows
        self.frame = Frame(root, bg='white')
        self.frame.place(relwidth=0.6, relheight=0.5, relx=0.3, rely=0.1)

    def setText(self,text, set_val):
        text.delete(0,END)
        text.insert(0,set_val)
    
    def help_(self):
        self.help_Window = tk.Toplevel(self.parent) 
        self.help_Window.title('Help')
        self.help_Window.geometry('400x400')
        self.helptext = tk.Label(self.help_Window, text="If you need help, please visit this website").place(x=5, y=5)
        
    def reset_(self):
        self.setText(self.para01,1); self.setText(self.para02,1); self.setText(self.para03,1)
        self.setText(self.para04,0); self.setText(self.para05,0); self.setText(self.para06,0)

    def load_img(self):
        #global img, image_data
        for img_display in self.frame.winfo_children():
            img_display.destroy()

        self.image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                       filetypes=(("all files", "*.*"), ("png files", "*.png")))
        #self.basewidth = 250 # Processing image for dysplaying
        self.img = Image.open(self.image_data)
        wpercent = (self.basewidth / float(self.img.size[0]))
        #print(self.basewidth)
        hsize = int((float(self.img.size[1]) * float(wpercent)))
        self.img = self.img.resize((self.basewidth, hsize), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        file_name = self.image_data.split('/')
        panel = Label(self.frame, text= str(file_name[len(file_name)-1]).upper()).pack()
        panel_image = tk.Label(self.frame, image=self.img)
        panel_image.pack()
    
    def run_(self):
        p01 = self.para01.get();p02 = self.para02.get();p03 = self.para03.get()
        p04 = self.para04.get();p05 = self.para05.get();p06 = self.para06.get()
    
        input_image = Image.open(self.image_data)
        numpy_image = img_to_array(input_image)
        check_shape=str(numpy_image.shape)
    
        output_text01 = "Paramters are "+p01+" , "+p02+" , "+p03+" , "\
        +p04+" , "+p05+" , "+p06+"\n"+" , and the image has shape of "+check_shape
    
        self.welcometext.configure(text="Please wait! GAN is running now..."+output_text01)
        
        # <... any process that takes as input a image and outputs a image ... >#
        # get output image 
        output_image = array_to_img(numpy_image)

        output_Window = tk.Toplevel(self.parent) 
        output_Window.title('Output image')
        output_Window.geometry('500x500')
    
        self.frame02 = tk.Frame(output_Window , bg='white')
        self.frame02.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        for img_display in self.frame02.winfo_children():
            img_display.destroy()
        
        self.output_image = Image.open(self.image_data) # image_data is a file object
        
        wpercent = (self.basewidth / float(self.output_image.size[0]))
        hsize = int((float(self.output_image.size[1]) * float(wpercent)))
        self.output_image = self.output_image.resize((self.basewidth, hsize), Image.ANTIALIAS)
        self.output_image = ImageTk.PhotoImage(self.output_image)
        
        # show image on the frame
        panel_image02 = tk.Label(self.frame02, image=self.output_image).pack()
        panel_image02.pack(side = "bottom", fill = "both", expand = "yes") # show image on the frame


if __name__ == "__main__":

    root = tk.Tk()
    root.title('Generative adversarial network')
    root.geometry('500x500')

    myapp = MainApp(root)

    root.mainloop()

