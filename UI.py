import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import funtions as fn

def select_directory():
    directory = filedialog.askdirectory()
    route_directory_label.config(text=directory)

def action_directory ():
    directory = route_directory_label.cget("text")
    fn.organize_file_by_extension (directory)
    messagebox.showinfo("The directory has been organized", "The directory has been organized correctly.")


def create_interface():
    window = tk.Tk()
    window.geometry("400x300")
    window.title("select directory")
    
    # Configura el tamaño de la ventana
    window_width = 400
    window_height = 300
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcula la posición en la que se debe colocar la ventana
    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    # Establece la posición y el tamaño de la ventana
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

    global route_directory_label
    route_directory_label = tk.Label(window, text="Select  directory")
    route_directory_label.pack(pady=10)
    
    select_directory_buttom = tk.Button(window, text="select directory", command=select_directory)
    select_directory_buttom.pack(pady=10)

    action_directory_buttom = tk.Button (window, text="Organize", command=action_directory)
    action_directory_buttom.pack (pady=10)
    window.mainloop()
