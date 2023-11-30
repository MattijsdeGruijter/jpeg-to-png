from PIL import Image
import tkinter as tk
import customtkinter as ctk
from tkinter import simpledialog, ttk, filedialog, messagebox
import os
import sys



ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class JpegToPngApp:
    
    def __init__(self, root):
        
        self.root = root
        self.root.title("jpeg to png converter")
        
        # Create a frame to hold the display
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack()
        
        self.STARTING_ROW = 1
        self.STARTING_COL = 1
        self.jpeg_file_names = []
        self.png_file_names = []
        self.file_path_dict = {}
        self.create_widgets()
        
    def create_widgets(self):
        
        self.label_filename = ctk.CTkLabel(self.frame, text=".jpeg files to convert to .png")
        self.label_filename.grid(row=self.STARTING_ROW, column=self.STARTING_COL, sticky="nswe", padx=10, pady=10)

        self.select_file_button = ctk.CTkButton(self.frame, text="Add .jpeg files", command=self.select_file)
        self.select_file_button.grid(row=self.STARTING_ROW+2, column=self.STARTING_COL, columnspan=1, sticky="we", padx=10, pady=1)
        
        self.delete_category_button = ctk.CTkButton(self.frame, text="Remove selected file", command=self.delete_jpeg)
        self.delete_category_button.grid(row=self.STARTING_ROW+3, column=self.STARTING_COL, columnspan=1, sticky="we", padx=10, pady=1)
        
        self.select_file_button = ctk.CTkButton(self.frame, text="Convert to .png", command=self.convert_to_png)
        self.select_file_button.grid(row=self.STARTING_ROW+5, column=self.STARTING_COL, columnspan=1, sticky="we", padx=10, pady=1)
        
        self.jpeg_listbox = tk.Listbox(self.frame, width=50)
        self.jpeg_listbox.grid(row=self.STARTING_ROW+1, column=self.STARTING_COL, sticky="nswe", columnspan=1, padx=10, pady=10)
        
        self.scrollbar = ctk.CTkScrollbar(self.frame, command=self.jpeg_listbox.yview)
        self.scrollbar.grid(row=self.STARTING_ROW+1, column=self.STARTING_COL+1, sticky="ns")
        self.jpeg_listbox.config(yscrollcommand=self.scrollbar.set)
    
    def select_file(self):
        file_path_list = filedialog.askopenfilenames(filetypes=[("JPEG Files", "*.jpeg")])
        if file_path_list:
            for file_path in file_path_list:
                
                jpeg_file_name = os.path.basename(file_path)
                png_file_name = jpeg_file_name.replace('.jpeg', '.png')
                
                self.file_path_dict[file_path] = {"jpeg"    : jpeg_file_name,
                                                  "png"     : png_file_name}
                
                self.jpeg_listbox.insert(tk.END, jpeg_file_name)
             
    def convert_to_png(self):
        for jpeg_file_path, dict in self.file_path_dict.items():
            jpeg_file_name = dict["jpeg"]
            png_file_name = dict["png"]
            im = Image.open(jpeg_file_path)
            
            directory = jpeg_file_path.replace(jpeg_file_name, 'png')

            if not os.path.exists(directory):
                os.makedirs(directory)
            
            png_file_path = jpeg_file_path.replace(jpeg_file_name, f'png/{png_file_name}')
            im.save(png_file_path)
        self.message_done()
    
    def message_done(self):
        msg = messagebox.showinfo("Files converted!", "All jpeg files have been converted to png files.")
        if msg:
            return sys.exit()
        
    def delete_jpeg(self):
        self.jpeg_listbox.delete(tk.ACTIVE)
    
def main():
    
    app_root = ctk.CTk()
    app = JpegToPngApp(app_root)
    # Start the main GUI loop
    app_root.mainloop()

if __name__ == "__main__":
    
    main()
