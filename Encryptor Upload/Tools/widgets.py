from tkinter import *


import customtkinter as ctk

def MyFont(size, **kwargs):
    slant = "roman"
    weight = "normal"
    for key, value in kwargs.items():
        if key == "slant":
            slant = value
        elif key == "weight":
            weight = value
    return ("Calibri", size, weight + " " + slant)

class MyEntry(Entry):
    def __init__(self, master, normal_bg = "white", hover_bg = None, active_bg = None, normal_fg = "black", hover_fg = None, active_fg = None, width = 100, default_text = "", default_active = True, bd = 0, relief = FLAT, font = MyFont(15), type = "normal"):
        super().__init__(master = master, bg = normal_bg, fg= normal_fg, width = width, bd = bd, relief = relief, font = font)
        self.normal_bg = normal_bg
        self.hover_bg = normal_bg if hover_bg == None else hover_bg
        self.active_bg = normal_bg if active_bg == None else active_bg
        
        self.normal_fg = normal_fg
        self.hover_fg = normal_fg if hover_fg == None else hover_fg
        self.active_fg = normal_fg if active_fg == None else active_fg

        
        self.default_text = default_text
        self.default_active = default_active

        self.insert(0, self.default_text)
        if type == "password":
            self.bind("<KeyRelease>", self.CheckPassword)

    
    
    def CheckPassword(self, event):
        if not self.get() == self.default_text:
            self.configure(show = "*")
        else:
            self.configure(show = "")

class MyEntryLabel(Label):
    def __init__(self, master, normal_img, hover_img = None, active_img = None, bg = "white", bd = 0, relief = FLAT, font = ("Calibri, 15")):
        super().__init__(master = master, image = normal_img, bd = bd, relief = relief, font = font, bg = bg)
        
        self.normal_img = normal_img
        self.hover_img = normal_img if hover_img == None else hover_img
        self.active_img = normal_img if active_img == None else active_img
        
class MyEntryWidget(Frame):
    def __init__(self, master, e_normal_bg = "white", e_hover_bg = None, e_active_bg = None, e_normal_fg = "black", e_hover_fg = None, e_active_fg = None, 
    e_bd = 0, e_relief = FLAT, e_font = MyFont(30), e_width = 100, e_default_text = "", e_default_active = True, e_type = "normal", 
    l_normal_img = None, l_hover_img = None, l_active_img = None, l_bd = 0, l_bg = "white", l_relief = FLAT, l_font = MyFont(30)):
        
        super().__init__(master, width = l_normal_img.width(), height = l_normal_img.height())
        self.label = MyEntryLabel(master, l_normal_img, l_hover_img,l_active_img, l_bg, l_bd, l_relief, l_font)
        self.entry = MyEntry(master, e_normal_bg, e_hover_bg, e_active_bg, e_normal_fg, e_hover_fg, e_active_fg, e_width, e_default_text, e_default_active, e_bd, e_relief, e_font, e_type)
        
        self.entry.bind("<Enter>", self.OnHover)
        self.entry.bind("<Leave>", self.OnLeave)
        self.entry.bind("<FocusIn>", self.OnActive)
        self.entry.bind("<FocusOut>", self.OnInactive)
        self.label.place(in_ = self, relx = 0, rely = 0, anchor = "nw")
        self.entry.place(in_ = self, relx = 0.5, rely = 0.5, anchor = CENTER)
        self.isActive = False



    def OnHover(self, event):
        if not self.isActive:
            self.label.configure(image = self.label.hover_img)
            self.entry.configure(bg = self.entry.hover_bg, fg = self.entry.hover_fg)

    def OnLeave(self, event):
        if not self.isActive:
            self.label.configure(image = self.label.normal_img)
            self.entry.configure(bg = self.entry.normal_bg, fg = self.entry.normal_fg)
    
    def OnActive(self, event):

        self.isActive = True
        self.label.configure(image = self.label.active_img)
        self.entry.configure(bg = self.entry.active_bg, fg = self.entry.active_fg)
        if self.entry.get() == self.entry.default_text:
            self.entry.delete(0, END)
    
    def OnInactive(self, event):
        self.isActive = False
        self.label.configure(image = self.label.normal_img)
        self.entry.configure(bg = self.entry.normal_bg, fg = self.entry.normal_fg)
        if self.entry.get() == "" and self.entry.default_active:
            self.entry.insert(0, self.entry.default_text)

class MyButton(Button):
    def __init__(self, master, normal_img, hover_img = None, active_img = None, bd = 0, bg = "white", state = ACTIVE, relief = FLAT, activebackground = "white"):
        super().__init__(master = master, image = normal_img, bd = bd, bg = bg, state = state, relief = relief, activebackground = activebackground)
        self.normal_img = normal_img
        self.hover_img = normal_img if hover_img == None else hover_img
        self.active_img = normal_img if active_img == None else active_img
        
        
        self.isActive = False

        self.bind("<Enter>", self.OnHover)
        self.bind("<Leave>", self.OnLeave)
        # self.bind("<Button-1>", self.OnActive)
        self.bind("<FocusOut>", self.OnInactive)

    def OnHover(self, event):
        if not self.isActive:
            self.configure(image = self.hover_img)
            

    def OnLeave(self, event):
        if not self.isActive:
            self.configure(image = self.normal_img)
            

    def OnActive(self, event):
        self.isActive = True
        self.configure(image = self.active_img)
        

    def OnInactive(self, event):
        self.isActive = False
        self.configure(image = self.normal_img)
        

class MySearchFrame(Frame):
    def __init__(self, master, e_normal_bg = "white", e_hover_bg = None, e_active_bg = None, e_normal_fg = "black", e_hover_fg = None, e_active_fg = None, e_bd = 0, e_relief = FLAT, e_font = MyFont(30), e_width = 100, e_default_text = "", e_default_active = True, e_type = "normal", 
    l_normal_img = None, l_hover_img = None, l_active_img = None, l_bd = 0, l_bg = "white", l_relief = FLAT, l_font = MyFont(30), 
    entry_relx = 0, entry_rely = 0, entry_anchor = CENTER, 
    search_bar_image = None, search_bar_bd = 0, search_bar_bg = "white", search_bar_relx = 0, search_bar_rely = 0, search_bar_anchor = CENTER,
    lb_width = 100, lb_height = 100, lb_bg = "white", lb_relief = FLAT, lb_highlightthickness = 0, lb_font = MyFont(30), lb_fg = "black", lb_selectbackground = "white", lb_activestyle = "none", lb_selectmode = SINGLE, lb_relx = 0, lb_rely = 0, lb_anchor = CENTER,
    search_frame_image = None, search_frame_bg = "white", search_frame_bd = 0,
    search_list = [], isChild = False):
        super().__init__(master = master)
        self.search_frame_label = Label(self, image = search_frame_image, bg = search_frame_bg, bd = search_frame_bd)
        self.search_frame_label.pack()
        self.search_entry = MyEntryWidget(self, e_normal_bg, e_hover_bg, e_active_bg, e_normal_fg, e_hover_fg, e_active_fg, e_bd, e_relief, e_font, e_width, e_default_text, e_default_active, e_type, l_normal_img, l_hover_img, l_active_img, l_bd, l_bg, l_relief, l_font)
        self.search_entry.place(in_ = self.search_frame_label, relx = entry_relx, rely = entry_rely, anchor = entry_anchor)
        self.search_bar_label = Label(self, image = search_bar_image, bd = search_bar_bd, bg = search_bar_bg)
        self.search_bar_label.place(in_ = self.search_frame_label, relx = search_bar_relx, rely = search_bar_rely, anchor = search_bar_anchor)
        self.search_listbox = Listbox(self, width = lb_width, height = lb_height, bg = lb_bg, relief = lb_relief, highlightthickness = lb_highlightthickness, font = lb_font, fg = lb_fg, selectbackground = lb_selectbackground, activestyle = lb_activestyle, selectmode = lb_selectmode)
        self.search_listbox.place(in_= self.search_bar_label, relx = lb_relx, rely = lb_rely, anchor = lb_anchor)
        self.search_list = search_list
        if not isChild:
            self.FillListBox()
            self.search_entry.entry.bind("<KeyRelease>", self.Search)
            self.search_listbox.bind("<<ListboxSelect>>", self.AutoFill)
    
    def FillListBox(self):
        self.search_listbox.delete(0, END)
        
        for i in self.search_list:
            self.search_listbox.insert(END, i)
    
    def Search(self, event):
        typed = self.search_entry.entry.get()
        self.search_listbox.delete(0, END)
        for i in self.search_list:
            if typed.lower() in i[0:len(typed)].lower():
                self.search_listbox.insert(END, i)
    
    def AutoFill(self, event):
        self.search_entry.entry.delete(0, END)
        self.search_entry.entry.insert(0, self.search_listbox.get(self.search_listbox.curselection()))
    
class MyEmployeeSearchFrame(MySearchFrame):
    def __init__(self, master, e_normal_bg, e_hover_bg, e_active_bg, e_normal_fg, e_hover_fg, e_active_fg, e_bd, e_relief, e_font, e_width, e_default_text, e_default_active, e_type, 
l_normal_img, l_hover_img, l_active_img, l_bd, l_bg, l_relief, l_font, 
entry_relx, entry_rely, entry_anchor, 
search_bar_image, search_bar_bd, search_bar_bg, search_bar_relx, search_bar_rely, search_bar_anchor,
lb_width, lb_height, lb_bg, lb_relief, lb_highlightthickness, lb_font, lb_fg, lb_selectbackground, lb_activestyle, lb_selectmode, lb_relx, lb_rely, lb_anchor,
search_frame_image, search_frame_bg, search_frame_bd,
search_list1, search_list2):
        super().__init__(master, e_normal_bg, e_hover_bg, e_active_bg, e_normal_fg, e_hover_fg, e_active_fg, e_bd, e_relief, e_font, e_width, e_default_text, e_default_active, e_type, 
l_normal_img, l_hover_img, l_active_img, l_bd, l_bg, l_relief, l_font, 
entry_relx, entry_rely, entry_anchor, 
search_bar_image, search_bar_bd, search_bar_bg, search_bar_relx, search_bar_rely, search_bar_anchor,
lb_width, lb_height, lb_bg, lb_relief, lb_highlightthickness, lb_font, lb_fg, lb_selectbackground, lb_activestyle, lb_selectmode, lb_relx, lb_rely, lb_anchor,
search_frame_image, search_frame_bg, search_frame_bd,
search_list1, True)
        self.search_list1 = search_list1
        self.search_list2 = search_list2
        self.FillListBox()
        self.search_entry.entry.bind("<KeyRelease>", self.Search)
        self.search_listbox.bind("<<ListboxSelect>>", self.AutoFill)

    def FillListBox(self):
        self.search_listbox.delete(0, END)
        
        for i in range(len(self.search_list1)):
            num = str(self.search_list1[i])
            text = " "
            for j in range(4 - len(num)):
                text += "  "
            text += num
            text += "  " + self.search_list2[i]
            
            self.search_listbox.insert(END, text)
    
    def Search(self, event):
        typed = self.search_entry.entry.get()
        self.search_listbox.delete(0, END)
        
        for i in range(len(self.search_list1)):
            if typed.lower() in self.search_list1[i][0:len(typed)].lower() or typed.lower() in self.search_list2[i][0:len(typed)].lower():
                num = str(self.search_list1[i])
                text = " "
                for j in range(4 - len(num)):
                    text += "  "
                text += num
                text += "  " + self.search_list2[i]
                self.search_listbox.insert(END, text)
    
    def AutoFill(self, event):
        self.search_entry.entry.delete(0, END)
        text = self.search_listbox.get(self.search_listbox.curselection())
        text = text.split(" ")
        text = ''.join(text)
        self.search_entry.entry.insert(0, text)
        
class MyDropDown(Frame):
    def __init__(self, master, root, 
    b_bd , b_bg, b_hover_bg, b_active_bg, b_relief, keep_flat, b_font, b_width, b_initial_value, b_fg, b_hover_fg, b_active_fg, b_relx, b_rely,
    lb_bd, lb_bg, lb_select_bg, lb_relief, lb_font, lb_width, lb_height, lb_fg, lb_select_fg, lb_relx, lb_rely, lb_list):
        super().__init__(master)
        
        self.button = Button(self, bd = b_bd, bg = b_bg, relief = b_relief, font = b_font, width = b_width, command = self.OnPress, text = b_initial_value, fg = b_fg, padx = 0, pady = 0, height= 1, activebackground=b_active_bg, activeforeground= b_active_fg)
        self.button.pack()
        self.button.bind("<Enter>", self.OnHover)
        self.button.bind("<Leave>", self.OnLeave)
       
        self.b_bg = b_bg
        self.b_hover_bg = b_hover_bg
        self.b_active_bg = b_active_bg
        self.b_fg = b_fg
        self.b_hover_fg = b_hover_fg
        self.b_active_fg = b_active_fg
        if keep_flat:
            root.bind("<Button-1>", self.KeepFlat)
        
        self.isActive = False
        self.listbox = Listbox(master, bd = lb_bd, bg = lb_bg, relief= lb_relief, font = lb_font, width = lb_width, height = lb_height, fg = lb_fg, selectbackground= lb_select_bg, selectforeground= lb_select_fg, activestyle= "none")
        self.listbox.place(in_ = self.button, relx = -1000, rely = -1000, anchor = "n")
        self.lb_relx, self.lb_rely = lb_relx, lb_rely
        self.listbox.delete(0, END)
        for i in lb_list:
            self.listbox.insert(END, i)
        self.listbox.bind("<<ListboxSelect>>", self.Select)
    
    def KeepFlat(self, event):
        if event.widget is self.button:
            event.widget.configure(relief = FLAT)

    def OnHover(self, event):
        if not self.isActive:
            self.button.configure(bg = self.b_hover_bg, fg = self.b_hover_fg)
    def OnLeave(self, event):
        if not self.isActive:
            self.button.configure(bg = self.b_bg, fg = self.b_fg)
    def OnPress(self):
        
        if not self.isActive:
            self.listbox.place(in_ = self.button, relx = self.lb_relx, rely = self.lb_rely, anchor = "n")
            self.button.configure(bg = self.b_active_bg, fg = self.b_active_fg)
        else:
            self.listbox.place(in_ = self.button, relx = -1000, rely = -1000, anchor = "n")
            self.button.configure(bg = self.b_bg, fg = self.b_fg)

        self.isActive = not self.isActive

    def Select(self, event):
        self.button.configure(text = self.listbox.get(self.listbox.curselection()))

    
class MyEntryCtkWidget(ctk.CTkEntry):
    def __init__(self, master, normal_bg = "white", normal_fg = "black", hover_fg = None, active_fg = None, text_color = "white", text_hover_color = None, text_active_color =  None,
    bd = 0, corner_radius = 0, relief = FLAT, font = MyFont(30), width = 200, height = 50, default_text = "", default_active = True, type = "normal", erase_default_text = True,
    bd_color = "black", bd_hover_color = None, bd_active_color = None, justify = LEFT):
        super().__init__(master = master, bg_color = normal_bg, fg_color = normal_fg, border_width = bd, border_color = bd_color, corner_radius = corner_radius, text_font = font, text_color = text_color, width = width, height = height, relief = relief, justify = justify)
        self.insert(0, default_text)
        self.default_active = default_active
        self.default_text = default_text
        self.type = type
        self.isActive = False
        self.erase_default_text = erase_default_text

        self.normal_bg = normal_bg

        self.normal_fg = normal_fg
        self.hover_fg = normal_fg if hover_fg == None else hover_fg
        self.active_fg = self.hover_fg if active_fg == None else active_fg

        self.bd_color = bd_color
        self.bd_hover_color = bd_color if bd_hover_color == None else bd_hover_color
        self.bd_active_color = self.bd_hover_color if bd_active_color == None else bd_active_color

        self.text_normal_color = text_color
        self.text_hover_color = text_color if text_hover_color == None else text_hover_color
        self.text_active_color = self.text_hover_color if text_active_color == None else text_active_color

        self.BindAll()

    def OnHover(self, event):
        if not self.isActive:
            self.configure(fg_color = self.hover_fg, border_color = self.bd_hover_color, text_color = self.text_hover_color)
            
    def OnLeave(self, event):
        if not self.isActive:
            self.configure(fg_color = self.normal_fg, border_color = self.bd_color, text_color = self.text_normal_color)
            
    
    def OnActive(self, event):
        
        self.isActive = True
        self.configure(fg_color = self.active_fg, border_color = self.bd_active_color, text_color = self.text_active_color)
        if self.get() == self.default_text and self.erase_default_text:
            self.delete(0, END)
    
    def OnInactive(self, event):
        self.isActive = False
        self.configure(fg_color = self.normal_fg, border_color = self.bd_color, text_color = self.text_normal_color)
        if self.get() == "" and self.default_active:
            self.insert(0, self.default_text)

    def BindAll(self):
        self.bind("<Enter>", self.OnHover)
        self.bind("<Leave>", self.OnLeave)
        self.bind("<FocusIn>", self.OnActive)
        self.bind("<FocusOut>", self.OnInactive)
        if self.type == "password":
            self.bind("<KeyRelease>", self.CheckPassword)
    
    def CheckPassword(self, event):
        if not self.get() == self.default_text:
            self.configure(show = "*")
        else:
            self.configure(show = "")
    
class MyDropDownCtk(ctk.CTkButton):
    def __init__(self, master, normal_bg = "white", normal_fg = "black", hover_fg = None, active_fg = None, 
    text_normal_color = "white", text_hover_color = None, text_active_color = None,
    bd = 0, relief = FLAT, font = MyFont(30), width = 200, height = 50, default_text = "", 
    bd_color = "white", bd_hover_color = None, bd_active_color = None, 
    lb_list = [], lb_bd = 0, lb_bg = "white", lb_relief = FLAT, lb_font = MyFont(30), lb_text_color = "white", lb_active_text_color = None, lb_width = None, lb_height = 5, lb_fg = "white", lb_active_fg = None, corner_radius = 0):
        super().__init__(master = master, bg_color = normal_bg, fg_color = normal_fg, hover_color = hover_fg, border_width = bd, border_color = bd_color, relief = relief, text_font = font, width = width, height = height, text = default_text, corner_radius = corner_radius, text_color = text_normal_color)

        self.normal_fg = normal_fg
        self.hover_fg = normal_fg if hover_fg == None else hover_fg
        self.active_fg = hover_fg if active_fg == None else active_fg

        self.bd_color = bd_color
        self.bd_hover_color = bd_color if bd_hover_color == None else bd_hover_color
        self.bd_active_color = self.bd_hover_color if bd_active_color == None else bd_active_color

        self.text_normal_color = text_normal_color
        self.text_hover_color = text_normal_color if text_hover_color == None else text_hover_color
        self.text_active_color = self.text_hover_color if text_active_color == None else text_active_color

        self.lb_fg = lb_fg
        self.lb_active_fg = self.lb_fg if lb_active_fg == None else lb_active_fg

        self.lb_text_color = lb_text_color
        self.lb_active_text_color = lb_text_color if lb_active_text_color == None else lb_active_text_color
        
        self.listbox = Listbox(master, bd = lb_bd, bg = lb_fg, relief= lb_relief, font = lb_font, width = lb_width, height = lb_height, fg = lb_text_color, selectbackground = self.lb_active_fg, selectforeground = lb_active_text_color, activestyle= "none", exportselection = False, selectmode = SINGLE)
        
        for i in lb_list:
            self.listbox.insert(END, i)
        self.BindAll()

        self.isActive = False

        
    
    def BindAll(self):
        self.bind("<Enter>", self.OnHover)
        self.bind("<Leave>", self.OnLeave)
        self.configure(command = self.OnButtonClick)
        self.listbox.bind("<ButtonRelease-1>", self.Select)

    def OnHover(self, event):
        self.configure(fg_color = self.hover_fg, border_color = self.bd_hover_color, text_color = self.text_hover_color)
    
    def OnLeave(self, event):
        if not self.isActive:
            self.configure(fg_color = self.normal_fg, border_color = self.bd_color, text_color = self.text_normal_color)

    def OnButtonClick(self):
        if not self.isActive:
            self.listbox.place(in_ = self, relx = 0.5, rely = 1, anchor = "n")
            self.configure(fg_color = self.active_fg, border_color = self.bd_active_color, text_color = self.text_active_color)
            
        else:
            self.listbox.place(in_ = self, relx = -100, rely = 1, anchor = "n")
            self.configure(fg_color = self.normal_fg, border_color = self.bd_color, text_color = self.text_normal_color)
        
        self.isActive = not self.isActive
    
    def Select(self, event):
        self.OnButtonClick()
        self.configure(text = self.listbox.get(self.listbox.curselection()))
        
        
class MyButtonCtk(ctk.CTkButton):
    def __init__(self, master, bg = "white", normal_fg = "white", hover_fg = None, active_fg = None, 
    bd = 0, normal_bd_color = "white", hover_bd_color = None, active_bd_color = None, 
    text = "", normal_text_color = "black", hover_text_color = None, active_text_color = None, font = MyFont(30),
    normal_width = 200, hover_width = None, active_width = None, normal_height = 60, hover_height = None, active_height = None,
    corner_radius = 0):
        super().__init__(master = master, bg_color = bg, fg_color = normal_fg, hover_color = normal_fg if hover_fg == None else hover_fg, border_width = bd, border_color = normal_bd_color, text = text, text_color = normal_text_color, text_font = font, width = normal_width, height = normal_height, corner_radius = corner_radius)

        self.normal_fg = normal_fg
        self.On_hover_fg = normal_fg if hover_fg == None else hover_fg
        self.active_fg = self.On_hover_fg if active_fg == None else active_fg

        self.normal_bd_color = normal_bd_color
        self.hover_bd_color = normal_bd_color if hover_bd_color == None else hover_bd_color
        self.active_bd_color = self.hover_bd_color if active_bd_color == None else active_bd_color

        self.normal_text_color = normal_text_color
        self.hover_text_color = normal_text_color if hover_text_color == None else hover_text_color
        self.active_text_color = self.hover_text_color if active_text_color == None else active_text_color

        self.normal_width = normal_width
        self.hover_width = normal_width if hover_width == None else hover_width
        self.active_width = self.hover_width if active_width == None else active_width

        self.normal_height = normal_height
        self.hover_height = normal_height if hover_height == None else hover_height
        self.active_height = self.hover_height if active_height == None else active_height

        self.isActive = False

        self.BindAll()
    
    def BindAll(self):
        self.bind("<Enter>", self.OnHover)
        self.bind("<Leave>", self.OnLeave)
        self.bind("<FocusIn>", self.OnActive)
        self.bind("<FocusOut>", self.OnInactive)

    def OnHover(self, event):
        if not self.isActive:
            self.configure(border_color = self.hover_bd_color, text_color = self.hover_text_color, width = self.hover_width, height = self.hover_height)

    def OnLeave(self, event):
        if not self.isActive:
            self.configure(fg_color = self.normal_fg, border_color = self.normal_bd_color, text_color = self.normal_text_color, width = self.normal_width, height = self.normal_height)

    def OnActive(self, event):
        self.isActive = True
        self.configure(fg_color = self.active_fg, border_color = self.active_bd_color, text_color = self.active_text_color, width = self.active_width, height = self.active_height)

    def OnInactive(self, event):
        self.isActive = False
        self.configure(fg_color = self.normal_fg, border_color = self.normal_bd_color, text_color = self.normal_text_color, width = self.normal_width, height = self.normal_height)


class MyDropDownSearchFrame(Frame):
    def __init__(self, master,
    e_normal_bg = "white", e_hover_bg = None, e_active_bg = None, e_bd = 0, e_relief = FLAT, e_font = MyFont(30), e_width = 10, e_default_text = "", e_default_active = True, e_type = "normal", e_normal_fg = "white", e_hover_fg = None, e_active_fg = None,
    l_normal_img = None, l_hover_img = None, l_active_img = None, l_bd = 0, l_bg = "white", l_fg = "black", l_relief = FLAT, l_font = MyFont(30), 
    lb_bd = 0, lb_bg = "white", lb_select_bg = "white", lb_relief = FLAT, lb_font = MyFont(30), 
    lb_width = 10, lb_height = 10, lb_fg = "black", lb_select_fg = "black", lb_relx = 0.5, lb_rely = 0.5, lb_list = [], islb_list_repeat = True, lb_anchor = "n", lb_selectmode = SINGLE, lb_activestyle = "none"):
        
        super().__init__(master, width = l_normal_img.width(), height = l_normal_img.height())
        
        self.listbox_anchor = lb_anchor

        self.entry = MyEntryWidget(self, e_normal_bg = e_normal_bg, e_hover_bg = e_hover_bg, e_active_bg = e_active_bg, e_normal_fg = e_normal_fg,
        e_bd = e_bd, e_relief = e_relief, e_font = e_font, e_width = e_width, e_default_text = e_default_text, e_default_active = e_default_active, e_type = e_type, 
        l_normal_img = l_normal_img, l_hover_img = l_hover_img, l_active_img = l_active_img, l_bd = l_bd, l_bg = l_bg, l_relief = l_relief, l_font = l_font)
        
        self.listbox = Listbox(master, bd = lb_bd, bg = lb_bg, relief= lb_relief, font = lb_font, width = lb_width, height = lb_height, fg = lb_fg, selectbackground= lb_select_bg, selectforeground= lb_select_fg, activestyle = lb_activestyle, selectmode = lb_selectmode, exportselection = False)
        self.lb_relx, self.lb_rely = lb_relx, lb_rely
        
        self.listbox.delete(0, END)
        
        if not islb_list_repeat:
            temp_list = []
            for i in lb_list:
                if i not in temp_list:
                    temp_list.append(i)
            lb_list = temp_list
        self.lb_list = lb_list
        for i in self.lb_list:
            self.listbox.insert(END, i)

        self.Place()
        self.BindAll()
        
    
    

    def Place(self):
        self.entry.place(in_ = self, relx = 0, rely = 0, anchor = "nw")
        self.listbox.place(in_ = self.entry, relx = -10, rely = -10, anchor = "n")

    def BindAll(self):
        self.listbox.bind("<<ListboxSelect>>", self.Select)
        self.entry.entry.bind("<FocusIn>", self.Active)
        self.entry.entry.bind("<FocusOut>", self.Inactive)
        self.entry.entry.bind("<KeyRelease>", self.Search)
    
    
    def Active(self, event):
        self.listbox.place(in_ = self.entry, relx = self.lb_relx, rely = self.lb_rely, anchor = self.listbox_anchor)

    def Inactive(self, event):
        self.listbox.place(in_ = self.entry, relx = -10, rely = -10, anchor = self.listbox_anchor)

    def Select(self, event):
        self.entry.entry.delete(0, END)

        self.entry.entry.insert(0, self.listbox.get(self.listbox.curselection()[0]))
    
    def Search(self, event):
        typed = self.entry.entry.get()
        self.listbox.delete(0, END)
                
        for i in self.lb_list:
            if typed.lower() in i[0:len(typed)].lower():
                self.listbox.insert(END, i)

class MyDropdownSearchFrameCtk(MyEntryCtkWidget):
    def __init__(self, master, e_normal_bg = "white", e_normal_fg = "white", e_hover_fg = None, e_active_fg = None, e_text_color = "black", e_text_hover_color = None, e_text_active_color = None, e_bd = 0, e_corner_radius = 0, e_font = MyFont(30), e_width = 200, e_height = 60, e_default_text = "", e_default_active = True, e_type = "normal", e_bd_color = "black", e_bd_hover_color = None, e_bd_active_color = None,
    lb_bd = 0, lb_bg = "black", lb_relief = FLAT, lb_font = MyFont(30),lb_width = 10, lb_height = 5, lb_fg = "white", lb_select_bg = "black", lb_select_fg = "white", lb_activestyle = "none", lb_selectmode = SINGLE, 
    lb_relx = 0.5, lb_rely = 1, lb_anchor = "n", lb_full_list = [], lb_option_repeat = False):
        super().__init__(master = master, normal_bg = e_normal_bg, normal_fg = e_normal_fg, hover_fg = e_hover_fg, active_fg = e_active_fg, text_color = e_text_color, text_hover_color = e_text_hover_color, text_active_color = e_text_active_color, bd = e_bd, corner_radius = e_corner_radius, font = e_font, width = e_width, height = e_height, default_text = e_default_text, default_active = e_default_active, type = e_type, bd_color = e_bd_color, bd_hover_color = e_bd_hover_color, bd_active_color = e_bd_active_color)
        
        self.listbox = Listbox(master, bd = lb_bd, bg = lb_bg, relief = lb_relief, font = lb_font, width = lb_width, height = lb_height, fg = lb_fg, selectbackground = lb_select_bg, selectforeground= lb_select_fg, activestyle = lb_activestyle, selectmode = lb_selectmode, exportselection = False)
        self.lb_relx, self.lb_rely, self.lb_anchor = lb_relx, lb_rely, lb_anchor
        self.listbox.delete(0, END)
        
        self.lb_list = list(lb_full_list)

        if not lb_option_repeat:
            temp_list = []
            for i in lb_full_list:
                if i not in temp_list:
                    temp_list.append(i)
            self.lb_list = list(temp_list)

        for i in self.lb_list:
            self.listbox.insert(END, i)
        
        self.NewPlaceAll()
        self.NewBindAll()
    
    def NewPlaceAll(self):
        self.listbox.place(in_ = self, relx = 100, rely = self.lb_rely, anchor = self.lb_anchor)
    
    def NewBindAll(self):
        self.listbox.bind("<ButtonRelease-1>", self.Select)
        self.bind("<FocusIn>", self.NewActive)
        self.bind("<FocusOut>", self.NewInactive)
        self.bind("<KeyRelease>", self.Search)
    
    def NewActive(self, event):
        self.OnActive(event)
        self.listbox.place(in_ = self, relx = self.lb_relx, rely = self.lb_rely, anchor = self.lb_anchor)
        
    
    def NewInactive(self, event):
        self.OnInactive(event)
        self.listbox.place(in_ = self, relx = 100, rely = self.lb_rely, anchor = self.lb_anchor)
        
    
    def Select(self, event):
        self.delete(0, END)
        self.insert(0, self.listbox.get(self.listbox.curselection()))

        self.listbox.delete(0, END)

        for option in self.lb_list:
            self.listbox.insert(END, option)
        
    
    def Search(self, event):
        typed = self.get()
        self.listbox.delete(0, END)

        for option in self.lb_list:
            if typed.lower() in option[0:len(typed)].lower():
                self.listbox.insert(END, option)
        
class MyLabelCtk(ctk.CTkLabel):
    def __init__(self, master, bg_color = "black", normal_fg = "white", hover_fg = None, text_normal_color = "black", text_hover_color = None, corner_radius = 0, width = 200, height = 60, text = "", text_font = MyFont(30), anchor = CENTER):
        super().__init__(master = master, bg_color = bg_color, fg_color = normal_fg, text_color = text_normal_color, corner_radius = corner_radius, width = width, height = height, text = text, text_font = text_font, anchor = anchor)

        self.normal_fg = normal_fg
        self.hover_fg = normal_fg if hover_fg == None else hover_fg

        self.text_normal_color = text_normal_color
        self.text_hover_color = text_normal_color if text_hover_color == None else text_hover_color

        self.BindAll()
    
    def BindAll(self):
        self.bind("<Enter>", self.OnHover)
        self.bind("<Leave>", self.OnLeave)

    def OnHover(self, event):
        self.configure(fg_color = self.hover_fg, text_color = self.text_hover_color)
    
    def OnLeave(self, event):
        self.configure(fg_color = self.normal_fg, text_color = self.text_normal_color)


class MyScrollBarCtk(ctk.CTkFrame):
    def __init__(self, master, scrollable_frame, scrollable_frame_master, root, scrollframe_width = 20, scrollframe_height = 500, scrollframe_bg_color = "white", scrollframe_normal_fg = "black", scrollframe_hover_fg = None, scrollframe_normal_bd_color = "black", scrollframe_hover_bd_color = None, scrollframe_bd = 0, scrollframe_corner_radius = None,
    scrollbar_width = 15, scrollbar_height = 100, scrollbar_normal_fg = "black", scrollbar_hover_fg = None, scrollbar_corner_radius = None, scrollbar_bd = 0, scrollbar_bd_color = "black", 
    scrollableframe_total_length = 500, scrollable_frame_y_offset_from_parent = 0, scroll_speed = 3):
        super().__init__(master = master, bg_color = scrollframe_bg_color, fg_color = scrollframe_normal_fg, border_color = scrollframe_normal_bd_color, border_width = scrollframe_bd, corner_radius = scrollframe_width // 2 if scrollframe_corner_radius == None else scrollframe_corner_radius, width = scrollframe_width, height = scrollframe_height)
        
        self.root = root
        self.master = master
        self.scrollable_frame = scrollable_frame
        self.scrollable_frame_master = scrollable_frame_master
        
        self.scrollbar_width, self.scrollbar_height = scrollbar_width, scrollbar_height
        self.scrollframe_width, self.scrollframe_height = scrollframe_width, scrollframe_height

        self.scrollableframe_max_height = scrollableframe_total_length - self.scrollable_frame_master.height
        self.scrollable_frame_y_offset_from_parent = scrollable_frame_y_offset_from_parent
        
        self.scroll_speed = scroll_speed

        self.scrollframe_normal_fg = scrollframe_normal_fg
        self.scrollframe_hover_fg = scrollframe_normal_fg if scrollframe_hover_fg == None else scrollframe_hover_fg

        self.scrollframe_normal_bd_color = scrollframe_normal_bd_color
        self.scrollframe_hover_bd_color = scrollframe_normal_bd_color if scrollframe_hover_bd_color == None else scrollframe_hover_bd_color

        self.scrollbar_normal_fg = scrollbar_normal_fg
        self.scrollbar_hover_fg = scrollbar_normal_fg if scrollbar_hover_fg == None else scrollbar_hover_fg

        self.scrollbar = ctk.CTkButton(master = self, bg_color = scrollframe_normal_fg, fg_color = scrollbar_normal_fg, hover_color = scrollbar_hover_fg, border_color = scrollbar_bd_color, border_width = scrollbar_bd, text = "", text_font = MyFont(0), corner_radius = scrollbar_width // 2 if scrollbar_corner_radius == None else scrollbar_corner_radius, width = scrollbar_width, height = scrollbar_height, command = self.OnActive)
        self.scrollbar.place(in_ = self, relx = 0.5, y = 0, anchor = "n")

        self.isActive = False

        self.BindAll()

    def BindAll(self):
        self.root.bind("<Motion>", self.Scroll)
        self.root.bind("<ButtonRelease-1>", self.DeActivate)
        self.root.bind("<MouseWheel>", self.WheelScroll)
        self.scrollbar.bind("<Enter>", self.OnHover)
        self.scrollbar.bind("<Leave>", self.OnLeave)
        

    def OnActive(self):
        self.isActive = True
    
    def Activate(self, event):
        self.isActive = True
    
    def DeActivate(self, event):
        self.isActive = False

    def OnHover(self, event):
        self.configure(fg_color = self.scrollframe_hover_fg, border_color = self.scrollframe_hover_bd_color)
        self.scrollbar.configure(fg_color = self.scrollbar_hover_fg, bg_color = self.scrollframe_hover_fg)
        
    def OnLeave(self, event):
        self.configure(fg_color = self.scrollframe_normal_fg, border_color = self.scrollframe_normal_bd_color)
        self.scrollbar.configure(fg_color = self.scrollbar_normal_fg, bg_color = self.scrollframe_normal_fg)
    
    def WheelScroll(self, event):
        self.scrollbar.place(in_ = self, relx = 0.5, y = int(self.scrollbar.winfo_rooty() - self.winfo_rooty() + -1 * event.delta / 120 * self.scroll_speed))
        self.ScrollFrame()
    
    def Scroll(self, event):
                
        if self.isActive:
            self.scrollbar.place(in_ = self, relx = 0.5, y = int(event.y_root - self.winfo_rooty() - self.scrollbar_height/2), anchor = "n")
        
        self.ScrollFrame()
        
    def ScrollFrame(self):
        
        if self.CheckScroll():
            
            offset = self.scrollbar.winfo_rooty() - self.winfo_rooty()
            percentage_offset = offset / (self.scrollframe_height - self.scrollbar_height) * 100
            new_frame_pos = (percentage_offset / 100) * self.scrollableframe_max_height
            self.scrollable_frame.place(in_ = self.scrollable_frame_master, x = self.scrollable_frame.winfo_rootx() - self.scrollable_frame_master.winfo_rootx(), y = int(-new_frame_pos) + self.scrollable_frame_y_offset_from_parent, anchor = "nw")
        
    def CheckScroll(self):  
        if self.scrollbar.winfo_rooty() - self.winfo_rooty() < 0:
            self.scrollbar.place(in_ = self,  relx = 0.5, y = 0, anchor = "n")
            return False
        elif self.scrollbar.winfo_rooty() + self.scrollbar_height > self.winfo_rooty() + self.scrollframe_height:
            self.scrollbar.place(in_ = self, relx = 0.5, y = self.scrollframe_height - self.scrollbar_height)
            return False
        return True
        






























