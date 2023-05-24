import PIL
from PIL import ImageTk
import os
from tkinter.filedialog import askopenfilename
from customtkinter import *
from tkinter import *
from tkinter import messagebox
from Tools.widgets import *
from Tools.color import *
import numpy as np
import random
LOGIN_IMG = "Images/Login.png"
USERNAME = "Your username"
PASSWORD = "Your password"
ENCRYPTED_TAG = "ore niwa yume ga aru"
ENCRYPTED_FOLDER = "Encrypted"

class Encryptor(CTkFrame):

    def __init__(self, master, frame_bg_color = complete_background_color, frame_fg_color = login_frame_color, frame_width = 500, frame_height = 300, frame_border_width = 3, frame_border_color = mygreen_color, frame_corner_radius = 20,
    file_heading_bg_color = login_frame_color, file_heading_fg_color = login_frame_color, file_heading_width = 100, file_heading_height = 25, file_heading_corner_radius = 0, file_heading_text_color = "white", file_heading_text_font = MyFont(25), file_heading_x = 30, file_heading_y = 30, file_heading_anchor = "nw", 
    e_normal_bg = login_frame_color, e_normal_fg = entry_inactive_color, e_hover_fg = None, e_active_fg = None, e_text_color = entry_text_color, e_text_hover_color = None, e_text_active_color = None, e_bd = 3, e_corner_radius = 10, e_font = MyFont(17), e_width = 440, e_height = 40, e_default_text = "", e_default_active = True, e_erase_default_text = False, e_bd_color = mygreen_color, e_bd_hover_color = None, e_bd_active_color = None, e_x = 30, e_y = 90, e_anchor = "nw",
    ebtn_normal_fg = login_button_color, ebtn_hover_fg = login_button_hover_color, ebtn_bd = 3, ebtn_normal_bd_color = login_button_color, ebtn_hover_bd_color = "black", ebtn_normal_text_color = "black", ebtn_hover_text_color = "black", ebtn_font = MyFont(32, weight = "bold"), ebtn_normal_width = 200, ebtn_normal_height = 50, ebtn_hover_width = 204, ebtn_hover_height = 64, ebtn_corner_radius = 10, ebtn_x = 30, ebtn_y = 180, ebtn_anchor = "nw",
    dbtn_x = 260, dbtn_y = 180, dbtn_anchor = "nw"):
        
        super().__init__(master = master, bg_color = frame_bg_color, fg_color = frame_fg_color, width = frame_width, height = frame_height, border_width = frame_border_width, border_color = frame_border_color, corner_radius = frame_corner_radius)
        
        # To Change the focus from file entry once the file is chosen
        self.sake_entry = MyEntryCtkWidget(master = self)
        self.sake_entry.place(relx = 50, rely = 0.5)
        
        # Choose File
        self.file_heading = CTkLabel(master = self, bg_color = file_heading_bg_color, fg_color = file_heading_fg_color, text_color = file_heading_text_color, corner_radius = file_heading_corner_radius, width = file_heading_width, height = file_heading_height, text = "Chosen File: ", text_font = file_heading_text_font)
        self.file_heading.place(in_ = self, x = file_heading_x, y = file_heading_y, anchor = file_heading_anchor)

        # Choose File Entry
        self.file_entry = MyEntryCtkWidget(master = self, normal_bg = e_normal_bg, normal_fg = e_normal_fg, hover_fg = e_hover_fg, active_fg = e_active_fg, text_color = e_text_color, text_hover_color = e_text_hover_color, text_active_color = e_text_active_color, bd = e_bd, corner_radius = e_corner_radius, font = e_font, width = e_width, height = e_height, default_text = e_default_text, default_active = e_default_active, erase_default_text = e_erase_default_text, bd_color = e_bd_color, bd_hover_color = e_bd_hover_color, bd_active_color = e_bd_active_color)
        self.file_entry.bind("<FocusIn>", self.Browse)
        self.file_entry.place(in_ = self, x = e_x, y = e_y, anchor = e_anchor)

        self.encrypt_btn = MyButtonCtk(master = self, bg = frame_fg_color, bd = ebtn_bd, normal_fg = ebtn_normal_fg, hover_fg = ebtn_hover_fg, normal_bd_color = ebtn_normal_bd_color, hover_bd_color = ebtn_hover_bd_color, text = "Encrypt", normal_text_color = ebtn_normal_text_color, hover_text_color = ebtn_hover_text_color, font = ebtn_font, normal_width = ebtn_normal_width, normal_height = ebtn_normal_height, hover_width = ebtn_hover_width, hover_height = ebtn_hover_height, corner_radius = ebtn_corner_radius)
        self.encrypt_btn.configure(command = self.Encrypt_File)
        self.encrypt_btn.place(in_ = self, x = ebtn_x, y = ebtn_y, anchor = ebtn_anchor)
    
        self.decrypt_btn = MyButtonCtk(master = self, bg = frame_fg_color, bd = ebtn_bd, normal_fg = ebtn_normal_fg, hover_fg = ebtn_hover_fg, normal_bd_color = ebtn_normal_bd_color, hover_bd_color = ebtn_hover_bd_color, text = "Decrypt", normal_text_color = ebtn_normal_text_color, hover_text_color = ebtn_hover_text_color, font = ebtn_font, normal_width = ebtn_normal_width, normal_height = ebtn_normal_height, hover_width = ebtn_hover_width, hover_height = ebtn_hover_height, corner_radius = ebtn_corner_radius)
        self.decrypt_btn.configure(command = self.Decrypt_File)
        self.decrypt_btn.place(in_ = self, x = dbtn_x, y = dbtn_y, anchor = dbtn_anchor)
        
        self.encoding_matrix = np.array([[1, -1, 1],
                                         [2, -1, 0],
                                         [1, 0, 0]], dtype = np.dtype(int))
        self.decoding_matrix = np.linalg.inv(self.encoding_matrix).astype(int)
    
    # File Encryption
    def Encrypt_File(self):
        filepath = self.file_entry.get()
        
        # If no file is chosen
        if filepath.strip() == "":
            messagebox.showerror("Choose File", "Please choose a file first!")
            return
        
        # Final encrypted line of numbers
        encrypted_line = ""

        try:
            with open(file = filepath, mode = "r") as File:
                readlines = File.readlines()
                
                isEncrypted = self.CheckIfEncrypted(readlines[0])

                if not isEncrypted:
                    readlines.insert(0, f"{ENCRYPTED_TAG}")
                    encrypted_line = self.Encrypt_Lines(readlines)
                else:
                    messagebox.showinfo("Already Encrypted", "The Chosen File has already been encrypted.")
                    return
            if encrypted_line == None:
                return
            isConfirm = messagebox.askyesno("Confirmation", f"Are you sure you wish to encrypt the file '{filepath}'?")
            if not isConfirm:
                return

            # Creating a backup
            new_filepath = ""
            for i in range(-1, - len(filepath) - 1, -1):
                if filepath[i] == "/":
                    new_filepath = filepath[i+1:]
                    break
            else:
                new_filepath = "hello-encrypted.txt"
            while new_filepath in os.listdir(ENCRYPTED_FOLDER):
                new_filepath = str(random.randint(1, 1000)) +  "-encrypted.txt"
            else:
                with open(file = ENCRYPTED_FOLDER + "/" + new_filepath, mode = "w") as File:
                    File.write(encrypted_line)
            
            with open(file = filepath, mode = "w") as File:
                File.write(encrypted_line)
                messagebox.showinfo("Encrypted", f"The file'{filepath}' has been encrypted successfully!")
            
        except Exception as err:
            self.ShowFileError()
            return
            
    # Encrypt the given lines
    def Encrypt_Lines(self, lines):
        try:
            encrypted_matrix = []

            for i in range(len(lines)):
                
                # Fill up empty spaces with null char
                line = ""
                if len(lines[i]) % 3 != 0:
                    line = lines[i] + chr(7) * (3 - len(lines[i]) % 3)
                else:
                    line = lines[i]
                # List of Matrices containing 3 chars each
                char_list = []

                for i in range(int(len(line)/3)):
                    word = line[i * 3 : (i+1) * 3]
                    new_word = []
                    for i in word:
                        new_word.append(i)

                    char_list.append(new_word)
                
                # The final list of matrices to be encoded
                to_be_encoded = []
                for i in char_list:
                    list = []
                    for j in i:
                        list.append(ord(j))
                    to_be_encoded.append(list)
                
                for i in range(len(to_be_encoded)):
                    encoded_word = np.dot(to_be_encoded[i], self.encoding_matrix).tolist()
                    encrypted_matrix.append(encoded_word)
            encrypted_line = ""

            for i in encrypted_matrix:
                for j in i:
                    encrypted_line += str(j) + " "
            encrypted_line = encrypted_line[:-1]
        
            return encrypted_line
        except:
            messagebox.showerror("Error", "An unexpected error has occured while encrypting the file. Please Check for corruption!")
            return None
    
    # File Decryption
    def Decrypt_File(self):
        
        filepath = self.file_entry.get()
        
        # If no file is chosen
        if filepath.strip() == "":
            messagebox.showerror("Choose File", "Please choose a file first!")
            return
            
        try:
            with open(file = filepath, mode = "r") as File:
                readline = File.readline()
                
                isEncrypted = self.CheckIfEncrypted(readline)
                if isEncrypted:
                    decrypted_line = self.Decrypt_Lines(readline)
                    decrypted_line = decrypted_line.replace(ENCRYPTED_TAG, "")
                    
                else:
                    messagebox.showinfo("Already decrypted", "The Chosen File hasn't been encrypted. So you cannot decrypt it.")
                    return
            
            if decrypted_line == None:
                return

            isConfirm = messagebox.askyesno("Confirmation", f"Are you sure you wish to decrypt the file '{filepath}'?")
            if not isConfirm:
                return
            with open(file = filepath, mode = "w") as File:
                File.write(decrypted_line)
                messagebox.showinfo("Decrypted", f"The file'{filepath}' has been decrypted successfully!")
        
        except:
            self.ShowFileError()
            return

    # Decrypt the given lines     
    def Decrypt_Lines(self, line):
        try:
            line_as_list = line.split(" ")
            
            list_of_encoded_matrices = []
            for i in range(len(line_as_list)):
                if i % 3 == 0:
                    strlist = line_as_list[i : i + 3]
                    
                    list_of_encoded_matrices.append([int(i) for i in strlist])
            decrypted_matrix = []
            for i in list_of_encoded_matrices:
                decrypted_matrix.append(np.dot(i, self.decoding_matrix).tolist())

            line = ""
            for i in decrypted_matrix:
                for j in i:
                    line += chr(j)

            line = line.replace(chr(7), "")

            return line
        except ValueError:
            pass
        except Exception as err:
            messagebox.showerror("Error", "An unexpected error has occured while decrypting the file. Please Check for corruption!")
            return 

    # Check if the file is already encrypted
    def CheckIfEncrypted(self, line):
        try:
            if ENCRYPTED_TAG in self.Decrypt_Lines(line):
                return True
        except ValueError:
            return False
        
        except:
            return None
        
        return False

    # Browse for files 
    def Browse(self, event):
        self.sake_entry.focus_set()
        
        filepath = askopenfilename(initialdir = "D:")
        
        if filepath == "":
            pass

        elif not filepath[-4:] == ".txt":
            self.ShowFileError()

        else:
            self.file_entry.delete(0, END)
            self.file_entry.insert(0, filepath)
        
    # Show file error
    def ShowFileError(self):
        messagebox.showerror("Choose File", "Please select an existing file of type '.txt'.")
        self.file_entry.delete(0, END)

class Login(Tk):
    def __init__(self):
        super().__init__()

        self.minsize(600, 800)
        self.title("Encryptor")
        self.configure(bg = complete_background_color)
        
        
        
        self.Load_Directory()
        self.Load_Images()
        self.Initialize()
        self.Place()
        self.BindAll()
        
    def Load_Directory(self):
        path = str(os.getcwd())
        for i in range(1, len(path)+1):
            if path[-i] == "\\":
                index = len(path) - i + 1
                break
        
        self.path = path[:index-1]

        temp_file_list = os.listdir(self.path)

        self.file_list = []
        for i in temp_file_list:
            if i[-4:] == ".txt":
                self.file_list.append(i)
        
        
        
    def Load_Images(self):
        
        self.login_img = ImageTk.PhotoImage(PIL.Image.open(LOGIN_IMG))
           
    def Initialize(self):
        self.login_label = Label(self, image = self.login_img, bd = 0)
        
        self.user_entry = MyEntryCtkWidget(master = self, normal_bg = login_frame_color, normal_fg = login_entry_inactive_color, hover_fg = login_entry_hover_color, active_fg = login_entry_active_color, text_color = "white", text_hover_color = "black", bd = 3, corner_radius = 10, font = MyFont(23, weight = "bold"), width = 250, height = 50, default_text = "Username...", bd_color = login_entry_hover_color)
        self.password_entry = MyEntryCtkWidget(master = self, normal_bg = login_frame_color, normal_fg = login_entry_inactive_color, hover_fg = login_entry_hover_color, active_fg = login_entry_active_color, text_color = "white", text_hover_color = "black", bd = 3, corner_radius = 10, font = MyFont(23, weight = "bold"), width = 250, height = 50, default_text = "Password...", type = "password", bd_color = login_entry_hover_color)
                
        self.submit_button = MyButtonCtk(master = self, bg = login_frame_color, bd = 5, normal_fg = login_button_color, normal_bd_color = login_button_color, hover_bd_color = "black", text = "Submit", normal_text_color = "black", hover_text_color = "black", font = MyFont(30, weight = "bold"), normal_width = 140, normal_height = 50, hover_width = 154, hover_height = 64, corner_radius = 25)
        self.submit_button.configure(command = self.Submit)

        self.exclamation_symbol = CTkLabel(master = self, bg_color = login_frame_color, fg_color = login_frame_color, text = "!", text_color = "#FFFFFF", text_font = MyFont(30), width = 1, height = 30)
        
        self.browser = Encryptor(master = self)
    def Place(self):
        self.login_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.user_entry.place(in_ = self.login_label, relx = 0.5, rely = 0.65, anchor = CENTER)
        self.password_entry.place(in_ = self.login_label, relx = 0.5, rely = 0.77, anchor = CENTER)

        self.submit_button.place(in_ = self.login_label, relx = 0.5, rely = 0.89, anchor = CENTER)
        self.exclamation_symbol.place(in_ = self.login_label, relx = 10, rely = 0.5, anchor = CENTER)
    
    def PlaceAway(self):
        self.login_label.place(in_ = self, relx = 10, rely = 10, anchor = CENTER)
        self.user_entry.place(in_ = self.login_label, relx = 10, rely = 10, anchor = CENTER)
        self.password_entry.place(in_ = self.login_label, relx = 10, rely = 10, anchor = CENTER)
        self.submit_button.place(in_ = self.login_label, relx = 10, rely = 10, anchor = CENTER)
        
        self.browser.place(in_ = self, relx = 0.5, rely = 0.5, anchor = CENTER)    
    
    def Submit(self):
        username = self.user_entry.entry.get()
        password = self.password_entry.entry.get()
        
        if username == USERNAME and password == PASSWORD:
            self.PlaceAway()
            self.main_menu = Encryptor(master = self)
        elif username == USERNAME:
            self.exclamation_symbol.place(in_ = self.password_entry, relx = -0.1, rely = 0.5, anchor = CENTER)
        else:
            self.exclamation_symbol.place(in_ = self.user_entry, relx = -0.1, rely = 0.5, anchor = CENTER)

            
        
    def BindAll(self):
        
        self.bind("<Button-1>", self.keep_flat)
        
    
    def keep_flat(self, event):
        if event.widget is self.submit_button:
            event.widget.configure(relief = FLAT)

if __name__ == "__main__":
    root = Login()
    root.mainloop()