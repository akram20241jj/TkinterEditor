import time
from tkinter import *
from tkinter import ttk
from collections import Counter
import tkinter
import tkinter.font as tkFont
import datetime
import pygame
from datetime import datetime
import re
import tkinter.scrolledtext as ScrolledText
from tkinter import messagebox
import pyautogui
import tkinter as tk
import sys
from tkinter import scrolledtext
from tkinter import filedialog
import os
from PIL import Image, ImageTk
from tkinter import colorchooser
from ttkthemes import ThemedStyle

global treeviewname
treeviewname = []
#=====================================
root=tkinter.Tk
#root = tk.Tk()

# Create a themed style object
#style = ThemedStyle(root)
# Set the theme
#style.theme_use("blue")

#=========================================
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)

        tooltip_label = tk.Label(self.tooltip, text=self.text, relief="ridge", borderwidth=1)
        tooltip_label.pack()

        tooltip_width = self.tooltip.winfo_reqwidth()
        tooltip_height = self.tooltip.winfo_reqheight()

        screen_width = self.widget.winfo_screenwidth()
        screen_height = self.widget.winfo_screenheight()

        if event.x_root + tooltip_width > screen_width:
            x = event.x_root - tooltip_width
        else:
            x = event.x_root

        if event.y_root + tooltip_height > screen_height:
            y = event.y_root - tooltip_height
        else:
            y = event.y_root

        self.tooltip.wm_geometry(f"+{x+20}+{y}")

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None


def move_and_click(x, y, perform_click=True, duration=1, message=None):
    # Enable fail-safe to move the mouse to the top-left corner of the screen
    pyautogui.FAILSAFE = True

    # Move the mouse to the target position
    pyautogui.moveTo(x, y, duration=1)

    # Pause for a moment to ensure the mouse has reached the position
    #time.sleep(1)

    # Show a message box if specified
    if message:
        root = tk.Tk()
        root.withdraw()

        # Create a label widget to display the message
        label = tk.Label(canvas1, text=message,background=bgbgbg,font=('Impact',10))
        label.place(x=x-400,y=y)
        #time.sleep(1)
        # Destroy the label after 1 second
        root.after(3000, lambda: label.destroy())
        # Run the Tkinter event loop
    # Perform a click at the current mouse position if specified
    if perform_click:
        pyautogui.click()

#----------------------------------------------------
try:
        with open("color.txt", "r") as f:
            bgbgbg = f.read()
except FileNotFoundError:
        # The file does not exist, so set the color to black.
        bgbgbg="navy"

#--------------------------------

def sound():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('C:/Users/PT/Desktop/wavs/click.wav')
    my_sound.play()
def sound1():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('C:/Users/PT/Desktop/wavs/click.wav')
    my_sound.play()

now = datetime.now()
now1=now.strftime("%I-%M-%S %p")
day=now.strftime("%A")
name11 = []
Font = "Arial",8
pady = 10
padx = 5
time1=f" D : {now.year}-{now.month}-{now.day} T : {now1}"

#root.attributes("-fullscreen", True)
#icon_path = 'C:/Users/PT/PycharmProjects/pythonProject/Imags/Editor.ico'  # Replace with the path to your icon file (should be in .ico format)
#root.iconbitmap(icon_path)



root = tk.Tk()

# Set the title of the window
root.title("Python Editor ver 1.001")
root.config(bg="Black")
Font = "Arial",8
Font1="Arial",8


#========================================================
width = 1345
height = 675
xgio = (root.winfo_screenwidth() // 2) - (width // 2)
ygio = (root.winfo_screenheight() // 2) - (height // 2)
#root.geometry('{}x{}+{}+{}'.format(width, height, xgio, ygio))
#===========================================================
root.maxsize(1345,675)
root.minsize(1345,675)
root.geometry(f'{920}x{640}+{0}+{0}')
colors="black"
root.resizable(False,False)
#"purple"
yy=1
xx=1
#====================================================================
style = ttk.Style()
style.configure('Red.TNotebook', tabmargins=[0, 0, 0, 0], tabposition='ne')  # Position tabs on the right side
style.configure('Red.TNotebook.Tab', padding=[27, 1], font=('Stencil', 8), foreground=bgbgbg, background='black')  # Set text color to red and background color to black
# Create the notebook with the custom style
notebook = ttk.Notebook(root, style='Red.TNotebook')
notebook.pack(fill='both', expand=True)
# Create the first tab
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Tools")
# Create buttons for the first tab
# Create the second tab
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Tools +")
# Create buttons for the second tab
# Select the first tab by default
notebook.select(tab1)

bg_color = 'Black'
fg_color = 'white'
active_bg_color = 'lightgray'
active_fg_color = 'blue'

#==========================================================



#================================================================
def hello():
    sound()
    move_and_click(1191, 305, perform_click=True, duration=11, message="click and choose from combo what tools u need")
    root.after(4000, lambda: move_and_click(900, 305, perform_click=True, duration=11,
                                            message="u drow your choise tool in windows "))
    root.after(8000, lambda: move_and_click(1340, 460, perform_click=True, duration=11,
                                            message="u incress the width "))
    root.after(9800, lambda: move_and_click(1340, 460, perform_click=True, duration=11,
                                            message="u incress the width "))
    root.after(11000, lambda: move_and_click(1340, 460, perform_click=True, duration=11,
                                            message="u incress the width "))
    root.after(13000, lambda: move_and_click(1340, 460, perform_click=True, duration=11,
                                            message="u incress the width "))
    root.after(15000, lambda: move_and_click(1330, 322, perform_click=True, duration=11,
                                            message="u click in combo to found the drawed tool "))
    root.after(18000, lambda: move_and_click(1330, 345, perform_click=True, duration=11,
                                             message="u choose the drawed tool "))
    root.after(23000, lambda: move_and_click(1200, 578, perform_click=True, duration=11,
                                             message="u Delete the  tool "))

    #print('Hello, world!')
menu = Menu(root, bg=bg_color, fg=fg_color, activebackground=active_bg_color, activeforeground=active_fg_color)

canvas1 = tk.Canvas(root, width=1150, height=669, background='black',cursor='hand2')
canvas1.place(x=1,y=1)

canvasSD1 = tk.Canvas(tab1, width=190, height=669, background=bgbgbg,cursor='hand2')
canvasSD1.place(x=1153,y=1)

canvasSDtab2 = tk.Canvas(tab2, width=190, height=669, background=bgbgbg,cursor='hand2')
canvasSDtab2.place(x=1153,y=1)

def deleteb():
    sound()
    button_widget.destroy()
    for i in range(0, len(buttonlst), 13):
        if buttonlst[i] == grtmum[0]:
            #print("i delet it ")
            del buttonlst[i:i+13]
            comboboxw_values = []
            comboboxw['values'] = ()
            for t in range(0, len(buttonlst), 13):
                comstr = f"{str(buttonlst[t])}  {buttonlst[t + 6]}"
                comboboxw_values.append(comstr)
                comboboxw["values"] = comboboxw_values
            try:
                comboboxw.current(0)
                on_combobox_selected(0)
            except:
                pass
            break

xxv = 1170
yyv = -50
switch=[False]
global columns
columns = ("Name", "Age", "Job", "Email", "Gender", "Mobile", "Address")
valuescombo = []
combodelt = ttk.Combobox(tab2, values=valuescombo, font=('Arial', 9), foreground=bgbgbg, background=bgbgbg, height=1, width=21, cursor='hand2')
delname=['']
def on_combobox_select(event):
    sound()
    selected_value = combodelt.get()
    #print(combodelt.get())
    button_click(combodelt.get())
    delname[0]=combodelt.get()
    # Perform actions with the selected value

combodelt.bind("<<ComboboxSelected>>", on_combobox_select)

lstsameas=[]
def UpdateTreeEntry():
    global treeviewlst
    global treeviewtools
    global buttonlst
    global treelabels
    global treeEntrys
    global buttonlistkey
    global button_widget
    global columns
    global lstsameas
    global frames

    for i in range(1, 22):
            search_item = entries[f"Col2Entry{i}"].get()
            if search_item in treeviewlst:
                #print("Item found!",search_item)
                #print("Selected value found!")
                f = f"You have this feild before:  {search_item}"
                messagebox.showinfo("Message", f)
                #break
                pass
            else:

                tkrk = entries[f"Col2Entry{i}"].get()
                if tkrk.isdigit():
                    #print(tkrk)
                    messagebox.showinfo("Message", "Entry contains only alphabetic characters")
                    entries[f"Col2Entry{i}"].delete(0,END)
                    break
                if entries[f"Col2Entry{i}"].get()=="" and entries[f"Col1Entry{i}"].get()=="" :
                    f=f"Fill Empty Entry to continue {i}"
                    #messagebox.showinfo("Message", f)
                    break
                if entries[f"Col2Entry{i}"].get() != "" :
                    lstsameas = []
                    for ifg in range(1, 22):
                        entries[f"Col2Entry{ifg}"].get()
                        if entries[f"Col2Entry{ifg}"].get()=="":
                            continue
                        else:
                            lstsameas.append(entries[f"Col2Entry{ifg}"].get())
                    counter = Counter(lstsameas)
                    duplicates = []
                    for value, count in counter.items():
                        if count > 1:
                            duplicates.append(value)
                            f = f"You repeat this feild fix it to continue :  {duplicates}"
                            messagebox.showinfo("Message", f)
                            lstsameas=[]
                            return f # Stop the loop when a duplicate is found

                    if entries[f"Col1Entry{i}"].get() == "":
#----------------------- &n اضافة جديد للقائمه------------------
                        # print("theres new item")
                        button_widget=frames[1]
                        #button_click(treeviewname[0])
                        x = button_widget.winfo_x()
                        y = button_widget.winfo_y()
                        selected_item1 = f"key{i}"
                        index = loclst1.index(selected_item1)
                        Lyao = int(loclst1[index + 1]);Lxao = int(loclst1[index + 2]);Lxdr = int(loclst1[index + 3]);Lydr = int(loclst1[index + 4]);
                        Eyao = int(loclst1[index + 5]);Exao = int(loclst1[index + 6]);Exdr = int(loclst1[index + 7]);Eydr = int(loclst1[index + 8])
                        lstnewcolm = ["", 0]

                        defult()

                        tool = "Label"
                        fx = entries[f"Col2Entry{i}"].get()
                        fxit = f"{fx}"

                        # f = f"{entries['Col1Entry' + str(i)].get()}{addlist[0] + 1}"
                        buttonnamenew[0] = fxit
                        treeviewtools.append(fxit)
                        treelabels.append(fxit)

                        # canvas1.create_window(x, y, window=tk.Label(canvas1, text="Label"))
                        button_widget = tk.Label(canvas1, text="Label", anchor="w")
                        canvas1.create_window(x + 120, Lyao, window=button_widget)

                        button_widget.config(font=("Arial", 10))
                        width_entry.delete(0, tk.END)
                        width_entry.insert(0, 10)
                        x_entry.delete(0, tk.END)
                        treeviewtools.append(Lxao)
                        treeviewtools.append(Lyao)
                        x_entry.insert(0, x + Lxdr)
                        y_entry.delete(0, tk.END)
                        y_entry.insert(0, y - Lydr)
                        text_entry.delete(0, tk.END)
                        text_entry.insert(0, fxit)
                        Bd_entry.delete(0, tk.END)
                        Bd_entry.insert(0, 0)
                        # print("=== fxit===",fxit)
                        kinds[0] = tool
                        buttonlistkey = True
                        update_button()

                        defult()
                        tool = "Entry"

                        # canvas1.create_window(x, y, window=tk.Entry(canvas1))
                        fx = entries[f"Col2Entry{i}"].get()
                        fxit = f"Entry_{fx}"
                        buttonnamenew[0] = fxit
                        treeviewtools.append(fxit)
                        treeEntrys.append(fxit)
                        button_widget = tk.Entry(canvas1)
                        canvas1.create_window(x + 192, Eyao - 1, window=button_widget)
                        button_widget.delete(0, tk.END)
                        button_widget.insert(0, fxit)
                        width_entry.delete(0, tk.END)
                        width_entry.insert(0, 18)
                        Bd_entry.delete(0, tk.END)
                        Bd_entry.insert(0, 4)
                        x_entry.delete(0, tk.END)
                        treeviewtools.append(Exao)
                        treeviewtools.append(Eyao)
                        x_entry.insert(0, x + Exdr)
                        y_entry.delete(0, tk.END)
                        y_entry.insert(0, y - Eydr)
                        kinds[0] = tool

                        text_entry.delete(0, tk.END)
                        text_entry.insert(0, fxit)
                        # print("====entry fxit===",fxit)
                        buttonlistkey = True
                        update_button()
                        entries[f"Col1Entry{i}"].configure(state="normal")
                        entries[f"Col1Entry{i}"].delete(0, END)
                        entries[f"Col1Entry{i}"].insert(0, entries[f"Col2Entry{i}"].get())
                        entries[f"Col2Entry{i}"].delete(0, END)
                        entries[f"Col1Entry{i}"].configure(state="disabled")
                        lstnewcolm[0] = entries[f"Col1Entry{i}"].get()
                        lstnewcolm[1] = i - 1
                        button_click(frames[0])
                        button_widget=treeviewname[1]
                        #button_click(treeviewname[0])
                        # ==================
                        # print(columns)
                        columns_list = list(columns)
                        index = len(columns)  # Insert at index 7 after "Address"
                        columns_list.insert(index, lstnewcolm[0])
                        columns = tuple(columns_list)
                        new_column_index = index  # Use the calculated index for the new column
                        new_column = lstnewcolm[0]
                        # print(columns)
                        # ==========================
                    # Iterate over the list and find the selected value


                    else:
                        # messagebox.showinfo("Message", "Fill Empty Entry to continue")
                        entries[f"Col1Entry{i}"].configure(state="normal")
                        entries[f"Col1Entry{i}"].delete(0, END)
                        entries[f"Col1Entry{i}"].insert(0, entries[f"Col2Entry{i}"].get())
                        entries[f"Col2Entry{i}"].delete(0, END)
                        entries[f"Col1Entry{i}"].configure(state="disabled")
    treecount = 1
    #print('trreeview', treeviewlst)
    #print("treelabels",treelabels)
    #print("tryEntry",treeEntrys)
    #print("treeviewtools",treeviewtools)
    #print("treeviewlst",treeviewlst)
    #============ يقوم بتعديل الليبل في التري تولز========
    for zz in range(len(treeviewlst)):
        # print(treeviewtools[treecount])
        search_item = (treelabels[zz])
        if search_item in treeviewtools:
            index = treeviewtools.index(search_item)
            if entries[f"Col1Entry{treecount}"].get() != "":
                treeviewtools[index] = entries[f"Col1Entry{treecount}"].get()
                #treelabels[zz]=entries[f"Col1Entry{treecount}"].get()
                # print(treeviewtools[index])
                treecount = treecount + 1
                #print("treeviewtools",treeviewtools)
                #print("treelabels",treelabels)
        else:
            pass
    # print(treeviewtools)
    #=========================== يقوم بتعديل الانتري في التري توولز==========
    treecount = 1
    for zz in range(len(treeviewlst)):
        # print(treeviewtools[treecount])
        search_item = (treeEntrys[zz])
        if search_item in treeviewtools:
            index = treeviewtools.index(search_item)
            if entries[f"Col1Entry{treecount}"].get() != "":
                fx = entries[f"Col1Entry{treecount}"].get()
                fxit = f"Entry_{fx}"
                treeviewtools[index] = fxit
                #treeEntrys[zz]=fxit
                # print(treeviewtools[index])
                treecount = treecount + 1
                #print("treeviewtools",treeviewtools)
                #print("treeEntrys",treeEntrys)

        else:
            pass
    treecount = 1
    listtest = buttonlst
    # print("=====",buttonlst)
    #----------- تعديل الانتري في بتم لست الرئيسيه , ,تعديله في لست الانتري ايضا-----------
    copytreeentry = treeEntrys
    #print("treeEntrys",treeEntrys)
    #print("buttonlst",buttonlst)
    for zz in range(len(treeviewlst)):
        # print(treeviewtools[treecount])
        search_item = (treeEntrys[zz])
        if search_item in buttonlst:
            index = buttonlst.index(search_item)
            # print(search_item,"===found it====",buttonlst[index])
            if entries[f"Col1Entry{zz + 1}"].get() != "":
                fx = entries[f"Col1Entry{zz + 1}"].get()
                fxit = f"Entry_{fx}"
                buttonlst[index] = fxit
                treeEntrys[zz] = fxit
                kinds[0] = "Entry"
                text_entry.delete(0, END)
                text_entry.insert(0, buttonlst[index])
                button_widget=buttonlst[index-5]
                #print(button_widget)
                button_widget.delete(0,END)
                button_widget.insert(0,fxit)
                button_click(fxit)
                #print("fxit",fxit)
                #print("treeEntrys", treeEntrys)
                #print("listbutton",buttonlst)
                # print("===change to ===", entries[f"Col1Entry{zz+1}"].get(), "===", buttonlst[index])
                # print(treeviewtools[index])
                treecount = treecount + 1
                #print("buttonlst",buttonlst)
                #print("treeEntrys",treeEntrys)
        else:
            pass
        #------------- تعديل الليبل في اللست بوتم الرئيسيه وفي قائمة الليبل ايضا ------------
        treecount = 1
        for zz in range(len(treeviewlst)):
            # print(treeviewtools[treecount])
            search_item = (treelabels[zz])
            if search_item in buttonlst:
                index = buttonlst.index(search_item)
                if entries[f"Col1Entry{treecount}"].get() != "":
                    buttonlst[index] = entries[f"Col1Entry{treecount}"].get()
                    treelabels[zz] = entries[f"Col1Entry{treecount}"].get()
                    kinds[0] = "Label"
                    text_entry.delete(0,END)
                    text_entry.insert(0,treelabels[zz])
                    button_click(treelabels[zz])

                    # print(treeviewtools[index])
                    treecount = treecount + 1
                    #print("buttonlst",buttonlst)
                    #print("treelabels",treelabels)
            else:
                pass
    #button_click(treeviewname[0])

    button_widget=treeviewname[1]
    #print(treeviewname)
    #print("=============button_widget",button_widget)
    button_widget["columns"] = columns
    #print(i)
    #messagebox.showinfo("Message", "Fill Empty Entry to continue")
    #global columns
    treeviewlst = []
    # messagebox.showinfo("Message", "Fill Empty Entry to continue")
    # --- بعد التعديل في اللست الرئيسيه ولست الليبل ولست الانتري قمنا بتفريغ تريفيولست وتعبئتعا من القائمه ---
    for ii in range(1, 22):
        if entries[f"Col1Entry{ii}"].get() != "":
            entries[f"Col1Entry{ii}"].configure(state="normal")
            treeviewlst.append(entries[f"Col1Entry{ii}"].get())
            entries[f"Col1Entry{ii}"].configure(state="disabled")
            #print("treeviewlst", treeviewlst)
            if entries[f"Col2Entry{ii}"].get() == "" and entries[f"Col1Entry{ii}"].get() == "":
                 #print(ii)
                 break
            else:
                 pass

    # ==== تنقيه اللست من التكرار ======
    unique_lst = []

    seen_values = set()
    for x in treeviewlst:
        if x not in seen_values:
            unique_lst.append(x)
            seen_values.add(x)
    treeviewlst = unique_lst
    #print(treeviewlst)
    # ==== تعبئه قائمة الادوات في اللست النهائي من تريفيو ======
    for iii in range(1, 22):
        entries[f"Col1Entry{iii}"].configure(state="normal")
        entries[f"Col1Entry{iii}"].delete(0, END)
        entries[f"Col1Entry{iii}"].configure(state="disabled")
    fillentry = 1
    for namex in treeviewlst:
        entries[f"Col1Entry{fillentry}"].configure(state="normal")
        entries[f"Col1Entry{fillentry}"].insert(0, namex)
        entries[f"Col1Entry{fillentry}"].configure(state="disabled")
        #print("namex",namex)
        fillentry = fillentry + 1
    # print(treeviewlst)
    # Convert the tuple to a list

    columns_list = list(columns)
    # Iterate over both lists simultaneously using zip
    for i, value in enumerate(treeviewlst):
        columns_list[i] = value
    # Convert the list back to a tuple
    columns = tuple(columns_list)
    # print("======تعديل ======",columns)


    # print(unique_lst)
    comboboxw_values = []
    comboboxw['values'] = ()
    for t in range(0, len(buttonlst), 13):
        comstr = f"{str(buttonlst[t])}  {buttonlst[t + 6]}"
        comboboxw_values.append(comstr)
        comboboxw["values"] = comboboxw_values

    combodelt_values = []
    combodelt['values'] = tuple(combodelt_values)  # Clear previous values
    for t in treeviewlst:
        combodelt_values.append(t)
    combodelt['values'] = tuple(combodelt_values)  # Update values

    #for frish in unique_lst:
        #button_click(frish)
#    for frish in copytreeentry:
    #    switch[0] = True
     #   button_click(frish)
    switch[0] = False
    #button_click(treeviewname[0])
    button_widget=treeviewname[1]
    # button_widget.destroy()
    for column in button_widget['columns']:
        button_widget.heading(column, text='')

    for io, column in enumerate(columns):
        button_widget.heading(io, text=column, anchor="w")
        button_widget.column(io, anchor="w", width=80)
    #print(treeviewlst)

def create_tab2():
    inner_frame = ttk.Frame(canvasSDtab2, width=156, height=207)
    inner_frame.grid_propagate(False)  # Disable automatic resizing of inner_frame
    canvasSDtab2.create_window((5, 70), window=inner_frame, anchor=tk.NW)

    scrollbar = ttk.Scrollbar(inner_frame, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas = tk.Canvas(inner_frame, bg=bgbgbg, width=156, height=207, yscrollcommand=scrollbar.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=canvas.yview)

    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

    inner_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

    frame_content = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_content, anchor=tk.NW)
    Col1Entry0=None
    global entries
    entries = {}  # Dictionary to store the Entry widgets

    for i in range(22):
        f = tk.Entry(frame_content, width=12,foreground="white")  # Set the width to 11
        f.grid(row=i, column=0, padx=1, pady=1, sticky="e")
        f.configure(background=bgbgbg,disabledforeground="white", disabledbackground=bgbgbg)
        entries[f"Col1Entry{i}"] = f  # Store the Entry in the dictionary
        #entries[f"Col1Entry{i}"].configure(state="disabled")

        ff = tk.Entry(frame_content, width=12,foreground="white")  # Set the width to 11
        ff.grid(row=i, column=1, padx=1, pady=1, sticky="e")  # Align to the right
        ff.configure(background=bgbgbg,disabledforeground="white", disabledbackground=bgbgbg)
        entries[f"Col2Entry{i}"] = ff  # Store the Entry in the dictionary

    # Accessing the Entry widgets by their variable names
    entries[f"Col1Entry{0}"].insert(0, "Feild")
    entries[f"Col2Entry{0}"].insert(0, "Change To")
    entries[f"Col2Entry{0}"].configure(state="disabled")
    entries[f"Col1Entry{0}"].configure(state="disabled")

    frame_content.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

    UpdateTree.place(x=495 + xxv, y=284 + yyv)
    combodelt.place(x=494 + xxv, y=310 + yyv)
    DelTree.place(x=494 + xxv, y=336 + yyv)

    combodelt_values = []
    combodelt['values'] = tuple(combodelt_values)  # Clear previous values
    for t in treeviewlst:
        combodelt_values.append(t)
    combodelt['values'] = tuple(combodelt_values)  # Update values


#create_tab2()

# إضافة القائمة
menu = tk.Menu(root, bg='blue', fg='white', activebackground='light blue', activeforeground='white')
file_menu = tk.Menu(menu, tearoff=0, bg='blue', fg='white', activebackground='light blue',
                    activeforeground='white')
file_menu.add_command(label='Open', command=hello)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)
menu.add_cascade(label='File', menu=file_menu)

help_menu = tk.Menu(menu, tearoff=0, bg='blue', fg='white', activebackground='light blue',
                    activeforeground='white')
help_menu.add_command(label='Help ?', command=hello)
menu.add_cascade(label='Help', menu=help_menu)

root.config(menu=menu)


xxvv=1149
yyvv=4
#=============================================================================

var = tk.BooleanVar()

valuescombo = []
# إضافة عناصر إلى الإطار الأحمر
#Canvas1f = tk.Canvas(right_frame, height=665, width=183, bg='purple')
#Canvas1f.pack()
xxv = 668
yyv = -0

Label2 = tk.Label(root, text="Python Editor ver 1.001", fg='white', bg=bgbgbg,
                  font=('Vladimir Script', 13), height=1, width=19)
Label2.place(x=489 + xxv, y=24 + yyv)

Label3ff = tk.Label(root, text='Time', fg='white', bg=bgbgbg, font=('Cascadia Mono SemiLight', 8),
                    height=1, width=26)
Label3ff.place(x=498 + xxv, y=46 + yyv)

ggf = "Mouse L_: ( X : 0, Y: 0)"
Label4ff = tk.Label(root, text=ggf, fg='white', bg=bgbgbg, font=('Cascadia Code SemiBold', 8),
                    height=1, width=28)
Label4ff.place(x=494 + xxv, y=58 + yyv)

Label5 = tk.Label(tab1, text='Roots', fg='white', bg=bgbgbg, font=('Vivaldi', 22), height=1, width=8)
Label5.place(x=495 + xxv, y=61 + yyv)

Label6 = tk.Label(tab1, text='RMX', fg='white', bg=bgbgbg, font=('Arial', 9), height=1, width=3)
Label6.place(x=493 + xxv, y=97 + yyv)

Label8 = tk.Label(tab1, text='RMY', fg='white', bg=bgbgbg, font=('Arial', 9), height=1, width=4)
Label8.place(x=576 + xxv, y=97 + yyv)

Label10 = tk.Label(tab1, text='Col_', fg='white', bg=bgbgbg, font=('Arial', 9), height=1, width=3)
Label10.place(x=492 + xxv, y=118 + yyv)

Label12 = tk.Label(tab1, text='Tie_', fg='white', bg=bgbgbg, font=('Arial', 9), height=1, width=3)
Label12.place(x=492 + xxv, y=143 + yyv)

Label14 = tk.Label(tab1, text='Fnt_', fg='white', bg=bgbgbg, font=('Arial', 9), height=1, width=3)
Label14.place(x=577 + xxv, y=118 + yyv)

#Label16 = tk.Label(tab1, text='Size', fg='white', bg=bgbgbg, font=('Arial', 9), height=1, width=3)
#Label16.place(x=577 + xxv, y=140 + yyv)

Label22 = tk.Label(tab1, text='Tools', fg='white', bg=bgbgbg, font=('Elephant', 12), height=1, width=7)
Label22.place(x=538 + xxv, y=224 + yyv)
#==============================================================================
#&l
loclst1=['key1', 174, 4-4, 2, 204, 176, 78-4, 76, 204, 'key2', 152, 4-4, 2, 204-22, 154, 78-4, 76, 204-22, 'key3', 130, 4-4, 2, 204-44, 132, 78-4, 76, 204-44, 'key4', 108, 4-4, 2, 204-66, 110, 78-4, 76, 204-66, 'key5', 86, 4-4, 2, 204-88, 88, 78-4, 76, 204-88, 'key6', 64, 4-4, 2, 204-110, 66, 78-4, 76, 204-110, 'key7', 42, 4-4, 2, 204-132, 44, 78-4, 76, 204-132, 'key8', 174, 210, 210, 204, 176, 284, 284, 204, 'key9', 152, 210, 208+2, 204-22, 154, 284, 282+2, 204-22, 'key10', 130, 210, 208+2, 204-44, 132, 284, 282+2, 204-44, 'key11', 108, 210, 208+2, 204-66, 110, 284, 282+2, 204-66, 'key12', 86, 210, 208+2, 204-88, 88, 284, 282+2, 204-88, 'key13', 64, 210, 208+2, 204-110, 66, 284, 282+2, 204-110, 'key14', 42, 210, 208+2, 204-132, 44, 284, 282+2, 204-132, 'key15', 174, 420, 418+2, 204, 176, 494, 492+2, 204, 'key16', 152, 420, 418+2, 204-22, 154, 494, 492+2, 204-22, 'key17', 130, 420, 418+2, 204-44, 132, 494, 492+2,  204-44, 'key18', 108, 420, 418+2, 204-66, 110, 494, 492+2, 204-66, 'key19', 86, 420, 418+2, 204-88, 88, 494, 492+2, 204-88, 'key20', 64, 420, 418+2, 204-110, 66, 494, 492+2, 204-110, 'key21', 42, 420, 418+2, 204-132, 44, 494, 492+2, 204-132]

#0 Lyao ;1 Lxao;2 Lxdr;3 Lydr
#4 Eyao ;5 Exao;6 Exdr;7 Eydr 8
#&d1
def deleteA(grtmum):
    global loclst1
    global treeviewtools
    global columns
    global button_widget
    #print(buttonlst)

    x='none'
    #print('=====',grtmum,'=====')
    if grtmum=="":
        return x
    #print(buttonlst)
    deleteb()
    #print(treeviewtools)
    f=f"Entry_{grtmum}"
    #print(f)
    selected_item = f
    button_click(f)
    deleteb()
    #print(buttonlst)
    #print("====columns====",columns)
    #======================================================
    # Assuming 'selected_column' contains the selected column to be deleted
    #fe = f"{treeviewname[0]}"
    #button_click(treeviewname[0])
    #button_widget.destroy()
    button_widget=treeviewname[1]
    for column in button_widget['columns']:
        button_widget.heading(column, text='')


    selected_column = grtmum.strip()
    # Convert the tuple to a list
    columns_list = list(columns)
    # Remove the selected column from the list
    if selected_column in columns_list:
        columns_list.remove(selected_column)
        #print("Column '{}' deleted.".format(selected_column))
    else:
        pass
        #print("Column '{}' not found.".format(selected_column))
    # Convert the list back to a tuple, if needed
    columns = tuple(columns_list)
    #print(columns)

    #=======================================================

    selected_items = grtmum
    index = treeviewlst.index(selected_items)
    # Delete selected item and its x and y values
    #print(index)
    del treeviewlst[index]

    selected_items = grtmum
    index = treelabels.index(selected_items)
    # Delete selected item and its x and y values
    del treelabels[index]

    selected_items = f"Entry_{grtmum}"
    index = treeEntrys.index(selected_items)
    # Delete selected item and its x and y values
    del treeEntrys[index]

    #print(treelabels)
    #print(treeEntrys)

    combodelt_values = []
    combodelt['values'] = tuple(combodelt_values)  # Clear previous values
    for t in treeviewlst:
        combodelt_values.append(t)
    combodelt['values'] = tuple(combodelt_values)  # Update values
    #combodelt.current(0)
    combodelt.set("")
    #button_click(combodelt.current(0))
    #print(treeviewtools)

    #=====================================================================
    for i in range(1, 22):
        if entries[f"Col2Entry{i}"].get() == "" and entries[f"Col1Entry{i}"].get() == "":
            # f = f"Fill Empty Entry to continue {i}"
             break

        selected_item = entries[f"Col1Entry{i}"].get().strip()
        #print(selected_item)
        # Find index of selected item
        # print(entries[f"Col1Entry{i}"].get())
        index = treeviewtools.index(selected_item)
        # Delete selected item and its x and y values
        del treeviewtools[index: index + 3]

        fv = f"Entry_{selected_item}"
        selected_item1 = fv.strip()
        index = treeviewtools.index(selected_item1)
        # Delete selected item and its x and y values
        del treeviewtools[index: index + 3]

    #print("==trree=>",treeviewtools)
    fillentry = 1

    for iii in range(1, 22):
        entries[f"Col1Entry{iii}"].configure(state="normal")
        entries[f"Col1Entry{iii}"].delete(0, END)
        entries[f"Col1Entry{iii}"].configure(state="disabled")

    for namex in treeviewlst:
        entries[f"Col1Entry{fillentry}"].configure(state="normal")
        entries[f"Col1Entry{fillentry}"].insert(0, namex)
        entries[f"Col1Entry{fillentry}"].configure(state="disabled")
        fillentry = fillentry + 1

    for i in range(1, 22):

                if entries[f"Col2Entry{i}"].get()=="" and entries[f"Col1Entry{i}"].get()=="" :
                    f=f"Fill Empty Entry to continue {i}"
                    #messagebox.showinfo("Message", f)
                    break
                #button_click(treeviewname[0])
                button_widget = frames[1]
                x = button_widget.winfo_x()
                y = button_widget.winfo_y()
                button_click(entries[f"Col1Entry{i}"].get())
                #=========================================

                selected_item1 = f"key{i}"
                #print(selected_item1)
                #print(i)
                index = loclst1.index(selected_item1)
                #print(index+1)
                Lyao = int(loclst1[index+1]); Lxao =int(loclst1[index+2]);Lxdr = int(loclst1[index+3]); Lydr = int(loclst1[index+4]); Eyao =int(loclst1[index+5]); Exao =int(loclst1[index+6]); Exdr =int(loclst1[index+7]);Eydr = int(loclst1[index+8])
                #loclst1

                button_click(entries[f"Col1Entry{i}"].get())
                treeviewtools.append(entries[f"Col1Entry{i}"].get())
                x_entry.delete(0, tk.END)
                treeviewtools.append(Lxao)
                treeviewtools.append(Lyao)
                x_entry.insert(0, x + Lxdr)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y - Lydr)
                update_button()

                fx = entries[f"Col1Entry{i}"].get()
                fxit = f"Entry_{fx}"

                button_click(fxit)
                treeviewtools.append(fxit)
                x_entry.delete(0, tk.END)
                treeviewtools.append(Exao)
                treeviewtools.append(Eyao)
                x_entry.insert(0, x + Exdr)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y - Eydr)
                update_button()

    #button_click(treeviewname[0])
    button_widget = treeviewname[1]
    # print(columns)
    for io, column in enumerate(columns):
        button_widget.heading(io, text=column, anchor="w")
        button_widget.column(io, anchor="w", width=80)
    #print(treeviewtools)


    #=====================================================================


    delname[0]=""


grtmum=[0]
UpdateTree = Button(tab2, text='Update Tree', bd=3, command=UpdateTreeEntry, bg=bgbgbg, fg='white', font=('Arial', 10),
                        height=1, width=20, cursor='hand2')
DelTree = Button(tab2, text='Delete Field', bd=3, command=lambda: deleteA(delname[0]), bg=bgbgbg, fg='white', font=('Arial', 10),
                height=1, width=20, cursor='hand2')


def changemenucolor(bgbgbg):
    with open("color.txt", "w") as f:
          f.write(bgbgbg)
    global comboboxw

    style.configure('Red.TNotebook.Tab', padding=[27, 1], font=('Stencil', 8), foreground=bgbgbg,
                    background='black')  # Set text color to red and background color to black

    canvasSD1.configure(bg=bgbgbg)
    canvasSDtab2.configure(bg=bgbgbg)
    Label2.configure(bg=bgbgbg)
    Label3ff.configure(bg=bgbgbg)
    Label4ff.configure(bg=bgbgbg)
    Label5.configure(bg=bgbgbg)
    Label6.configure(bg=bgbgbg)
    Label8.configure(bg=bgbgbg)
    Label10.configure(bg=bgbgbg)
    Label12.configure(bg=bgbgbg)
    Label14.configure(bg=bgbgbg)
    #Label16.configure(bg=bgbgbg)
    Label22.configure(bg=bgbgbg)
    rootmx.configure(bg=bgbgbg)
    rootmy.configure(bg=bgbgbg)
    rootcolor.configure(bg=bgbgbg)
    roottietl.configure(bg=bgbgbg)
    rootfont.configure(bg=bgbgbg)
    #rootfonts.configure(bg=bgbgbg)
    TxtRfontSample.configure(bg=bgbgbg)
    #combo_boxcol.configure(background=bgbgbg,foreground=bgbgbg)
    #Label28.configure(bg=bgbgbg)

    widgtFontff.configure(background=bgbgbg)
    Textsamplewd.configure(bg=bgbgbg)
    root.button.configure(bg=bgbgbg)
    root.buttonhhh.configure(bg=bgbgbg)
    root.buttonHH.configure(bg=bgbgbg)
    root.buttonwww.configure(bg=bgbgbg)
    root.buttonWW.configure(bg=bgbgbg)
    root.buttonxm.configure(bg=bgbgbg)
    root.buttonx.configure(bg=bgbgbg)
    root.buttony.configure(bg=bgbgbg)
    root.buttonym.configure(bg=bgbgbg)
    root.buttonexit.configure(bg=bgbgbg)
    root.buttondelet.configure(bg=bgbgbg)
    combo_boxmv1.config(background=bgbgbg)
    comboboxw.config(foreground=bgbgbg,background=bgbgbg)
    combodelt.config(foreground=bgbgbg,background=bgbgbg)
    #fnz_entry.configure(bg=bgbgbg)
    bgLabel33.configure(bg=bgbgbg)
    fgLabel35.configure(bg=bgbgbg)
    bg_entry.configure(bg=bgbgbg, disabledbackground=bgbgbg)
    fg_entry.configure(bg=bgbgbg, disabledbackground=bgbgbg)
    txtLabel37.configure(bg=bgbgbg)
    text_entry.configure(bg=bgbgbg)
    widthlabel.configure(bg=bgbgbg)
    width_entry.configure(bg=bgbgbg)
    height_entryLabel45.configure(bg=bgbgbg)
    height_entry.configure(bg=bgbgbg)
    x_entryLabel51.configure(bg=bgbgbg)
    x_entry.configure(bg=bgbgbg)
    y_entryLabel53.configure(bg=bgbgbg)
    y_entry.configure(bg=bgbgbg)
    Bd_entry.configure(bg=bgbgbg)
    Bd_entryLabel53.configure(bg=bgbgbg)
    update_button_button.configure(bg=bgbgbg)
    Fgcolorbtn.config(background=bgbgbg)
    Bgcolorbtn.config(background=bgbgbg)
    move_entry.configure(bg=bgbgbg)
    root.startcode.configure(bg=bgbgbg)
    copy_button.configure(bg=bgbgbg)
    clear_button.configure(bg=bgbgbg)
    save_button.configure(bg=bgbgbg)
    load_button.configure(bg=bgbgbg)
    buttoncolorff.configure(bg=bgbgbg)
    Menucolorff.configure(bg=bgbgbg)
    root.buttonBdD.configure(bg=bgbgbg)
    root.buttonyBdU.configure(bg=bgbgbg)
    RootFontff.configure(bg=bgbgbg)
    try:
        for i in range(22):
            entries[f"Col1Entry{i}"].configure(background=bgbgbg, disabledforeground="white", disabledbackground=bgbgbg)
            entries[f"Col2Entry{i}"].configure(background=bgbgbg, disabledforeground="white", disabledbackground=bgbgbg)
        UpdateTree.configure(background=bgbgbg)
        DelTree.configure(background=bgbgbg)
    except:
        pass
    try:
        plus1.configure(bg=bgbgbg)
        plus2.configure(bg=bgbgbg)
        plus3.configure(bg=bgbgbg)
        plus4.configure(bg=bgbgbg)
        plus5.configure(bg=bgbgbg)
        plus6.configure(bg=bgbgbg)
        plus7.configure(bg=bgbgbg)
        plus8.configure(bg=bgbgbg)
        plus9.configure(bg=bgbgbg)
        plus10.configure(bg=bgbgbg)
        plus11.configure(bg=bgbgbg)
        plus12.configure(bg=bgbgbg)
    except:
        pass

    # ==============================================================================
def print_mouse_position(event):
    x, y = event.x, event.y
    Label4ff.config(text=f"Mouse L_: ( X :{x}, Y: {y})")

# create the tkinter window
# create a canvas widget and bind the <Motion> event to the print_mouse_position function
canvas1.bind("<Motion>", print_mouse_position)


rootmx = tk.Entry(tab1,bd=3, width=6, fg='white', bg=bgbgbg, font=('Arial', 9),cursor='hand2')
rootmx.insert(0, 'RMXE')
rootmx.place(x=525 + xxv, y=97 + yyv)
ToolTip(rootmx, "RootMax windows width X ")

rootmy = tk.Entry(tab1,bd=3, width=6, fg='white', bg=bgbgbg, font=('Arial', 9),cursor='hand2')
rootmy.insert(0, 'RMYE')
rootmy.place(x=611 + xxv, y=98 + yyv)
ToolTip(rootmy, "RootMax windows Height Y ")

rootcolor = tk.Entry(tab1,bd=3, width=6, fg='white', bg=bgbgbg, font=('Arial', 9),cursor='hand2')
rootcolor.insert(0, 'COLE')
rootcolor.place(x=525 + xxv, y=119 + yyv)

roottietl = tk.Entry(tab1,bd=4, width=18, fg='white', bg=bgbgbg, font=('Arial', 9),cursor='hand2')
roottietl.insert(0, 'TieE')
roottietl.place(x=525 + xxv, y=143 + yyv)

rootfont = tk.Entry(tab1,bd=3, width=6, fg='white', bg=bgbgbg, font=('Arial', 9),cursor='hand2')
rootfont.insert(0, 'FntE')
rootfont.place(x=611 + xxv, y=120 + yyv)

#rootfonts = tk.Entry(tab1,bd=3, width=6, fg='white', bg=bgbgbg, font=('Arial', 9),cursor='hand2')
#rootfonts.insert(0, 'SizeE')
#rootfonts.place(x=611 + xxv, y=142 + yyv)

    # Set default values for the first entry box
rootfont.delete(0, tk.END)
rootfont.insert(0, "Arial")
#rootfonts.delete(0, tk.END)
#rootfonts.insert(0, "8")
rootmx.delete(0, tk.END)
rootmx.insert(0, "1146")
rootmy.delete(0, tk.END)
rootmy.insert(0, "659")
rootcolor.delete(0, tk.END)
rootcolor.insert(0, "Black")
roottietl.delete(0, tk.END)
roottietl.insert(0, "Python Editor ver 1.001")

#==================================================

global rectangle_id
rectangle_id = None

mainprogscr=["Arial",8,1146,659,"Black","Python Editor ver 1.001"]
def fillmainpro():
    global mainprogscr
    mainprogscr[0]=rootfont.get() #"Main-Font"
    mainprogscr[1] = 9#font size
    mainprogscr[2] = rootmx.get()#"Root-Min X
    mainprogscr[3] = rootmy.get()# root min y
    mainprogscr[4] = rootcolor.get()#"Root Color"
    mainprogscr[5] = roottietl.get()#Program title


#======================================================================================

#Font list roooooooooooooooooooooooooooooot

colorlst1=['black']
def open_color_dialog():
    # Create a child window for the color dialog
    dialog_window = tk.Toplevel(root)
    dialog_window.withdraw()
    # Calculate the position of the dialog window relative to the main window
    x = dialog_window.winfo_rootx() + 670  # Adjust the x-coordinate as desired
    y = dialog_window.winfo_rooty() + 170  # Adjust the y-coordinate as desired
    # Set the position of the dialog window
    dialog_window.geometry(f"+{x}+{y}")
    def select_color():
        #global hex_colors11
        color = colorchooser.askcolor(parent=dialog_window, title="Select Color")
        if color[1]:  # Check if a color is selected
            #print(color[1])
            colorlst1[0]=color[1]
            dialog_window.destroy()
        else:
            try:
                 dialog_window.destroy()
            except:
                pass
        # Close the child window
    select_color()
def update_colorroot():
    selected_color = open_color_dialog()
    rootcolor.delete(0, tk.END)
    rootcolor.insert(0, colorlst1[0])
    canvas1.configure(bg=colorlst1[0])
    draw_rectangle(colorlst1[0])
# Create a button
buttoncolorff = tk.Button(tab1,width=10,height=1,background=bgbgbg, foreground='white',cursor='hand2', text='Change Color',bd=3, command=update_colorroot,font=('Arial ',9))
buttoncolorff.place(x=97+xxvv,y=194+yyvv)
#==========================================================================
def update_colormenu(*args):
    sound()
    selected_color = open_color_dialog()
    changemenucolor(colorlst1[0])
# =============== كمبو الالوان لتغيير الواجهه الرئيسيه ==========
Menucolorff = tk.Button(tab1, width=20, height=1, background=bgbgbg, foreground='white',
                        cursor='hand2', text='Change Tools Color', bd=3, command=update_colormenu,
                        font=('Arial', 10))
Menucolorff.place(x=xxvv + 14, y=581 + yyvv)
#===========================================
#========================= من هنا تبدا الكبسه ===================

button_widget = None
# create a canvas to draw on
default_config = {"text": "Canvas",
                  "bg": "teal",
                  "fg": "white",
                  "font": ("Arial", 9),
                  "width": 9,
                  "height":1,
                  "font size":10,
                  "borderwidth":2
                  }

yy=0
xz=773
yz=228

#================================================
#Font list for widget

#--------------------------------------------------------------------------------
mainfontlst=['Arial 9 bold']
Rootfontlst=['Arial 9 bold']
def open_font_dialog(whois):
    window = tk.Tk()
    window.maxsize(550, 350)
    window.minsize(550, 350)
    window.geometry(f'{20}x{10}+{670}+{50}')
    window.withdraw()
    def font_changed(font):
        #print("========font=========", font)
        l['font'] = font

        #global button_widget
        #button_widget.config(font=font)
        #print("========l['font']=========", l['font'])
        if whois==1:
            mainfontlst[0]=font
        else:
            Rootfontlst[0]=font
        #print (mainfontlst[0])
        #q = tk.Button(canvas1,text="hello man",width=50,height=4)
        #q.place(x=100, y=100)
        #q.config(font=mainfontlst[0])
        window.destroy()
        #match = re.match(r'\{(.*?)\}\s+(\d+)(?:\s+(.*))?', font)  # Updated regular expression pattern
        #if match:
            #font_name = match.group(1)
            #font_size = match.group(2)
            #font_style = match.group(3)
            #print("Font Name:", font_name)
            #print("Font Size:", font_size)
            #print("Font Style:", font_style)
            #l['font'] = font

            #mainfontlst[0] =font_name
            #mainfontlst[1] =font_size
            #mainfontlst[2] =font_style

        #else:
            #print("Invalid font format:", font)

    dialog_window = tk.Toplevel(window)
    dialog_window.geometry('+100+100')  # Adjust the coordinates as needed
    dialog_window.focus_force()
    dialog_window.withdraw()

    l = tk.Label(window, text="Hello World", font="Helvetica 24")
    #l.pack(padx=20, pady=20)

    default_font = "Arial 9 bold"  # Set the default font
    if mainfontlst[0] =="Arial 9 bold":
        pass
    else:
        default_font=mainfontlst[0]

    dialog_window.tk.call('tk', 'fontchooser', 'configure', '-font', default_font, '-command',
                          dialog_window.register(font_changed))
    dialog_window.tk.call('tk', 'fontchooser', 'show')



#--------------------------------------------------------------------------------

Textsamplewd = tk.Text(tab1,bd=3, fg='white', bg=bgbgbg, font=('Arial', 10), height=1, width=12)
Textsamplewd.place(x=492 + xxv, y=305 + yyv)
Textsamplewd.insert(INSERT, "Font Sample")
def update_fontvwdget(event=None):
    global button_widget
    if isinstance(button_widget, tk.Canvas):
        pass
    else:
        sound()
        open_font_dialog(1)
        Textsamplewd.configure(font=mainfontlst[0])
        update_button()

widgtFontff = tk.Button(tab1,width=10,height=1,background=bgbgbg, foreground='white',cursor='hand2', text='Change Font',bd=3, command=update_fontvwdget,font=('Arial ',9))
widgtFontff .place(x=584 + xxv, y=304 + yyv)
#===================================================================================================================

#-------------geometric Fonts --------------------------------
TxtRfontSample = tk.Text(tab1,bd=3, fg='white', bg=bgbgbg, font=('Arial', 10), height=1, width=11)
TxtRfontSample.place(x=496 + xxv, y=170 + yyv)
TxtRfontSample.insert(INSERT, "Font Sample")

def update_Rootfont(event=None):
    sound()
    open_font_dialog(2)
    TxtRfontSample.configure(font=Rootfontlst[0])
    #TxtRfontSample.configure(font=(font_name1g, 9))
    rootfont.delete(0, tk.END)
    rootfont.insert(0, Rootfontlst[0])

RootFontff = tk.Button(tab1,width=10,height=1,background=bgbgbg, foreground='white',cursor='hand2', text='Change Font',bd=3, command=update_Rootfont,font=('Arial ',9))
RootFontff .place(x=578 + xxv, y=168 + yyv)


#====================================================================================================================
#==========================================
Moves=1
#==========================================

def clicks():
    sound()
    answer = messagebox.askquestion("Exit", "Do you really want to exit?")
    # if the user clicks "Yes", destroy the root window to exit the application
    if answer == "yes":
        sys.exit()
        root.destroy()


def clicksx():
    sound()
    xx=int(x_entry.get())
    if xx <= 1:
        pass
    else:
      xx=xx-int(move_entry.get())
      x_entry.delete(0, tk.END)
      x_entry.insert(0,xx)
      update_button()
def clicksxm():
    global button_widget
    width = button_widget.winfo_width()
    sound()
    xx=int(x_entry.get())
    if (xx+width)>=1150:
        pass
    else:
        xx=xx+int(move_entry.get())
        x_entry.delete(0, tk.END)
        x_entry.insert(0,xx)
        update_button()


def clicksy():
    sound()
    yy = int(y_entry.get())
    yy = yy -int(move_entry.get())
    y_entry.delete(0, tk.END)
    y_entry.insert(0, yy)
    update_button()
def clicksym():
    sound()
    yy = int(y_entry.get())
    yy = yy +int(move_entry.get())
    y_entry.delete(0, tk.END)
    y_entry.insert(0, yy)
    update_button()
def clicksbdu():
    sound()
    bd = int(Bd_entry.get())
    bd = bd + 1
    Bd_entry.delete(0, tk.END)
    Bd_entry.insert(0, bd)
    update_button()
def clicksbdd():
    sound()
    bd = int(Bd_entry.get())
    bd = bd - 1
    Bd_entry.delete(0, tk.END)
    Bd_entry.insert(0, bd)
    update_button()





root.button = Button(tab1, text='R_Update', bd=3, command=lambda: draw_rectangle(colorlst1[0]), bg=bgbgbg, fg='white', font=('Arial', 9), height=1, width=10, cursor='hand2')
root.button.place(x=496 + xxv, y=198 + yyv)

def clickwp():
    sound()
    ww = int(width_entry.get())
    ww = ww +1
    width_entry.delete(0, tk.END)
    width_entry.insert(0, ww)
    update_button()
def clickwm():
    sound()
    ww = int(width_entry.get())
    ww = ww -1
    width_entry.delete(0, tk.END)
    width_entry.insert(0, ww)
    update_button()

def clickhm():
    sound()
    ww = int(height_entry.get())
    ww = ww -1
    height_entry.delete(0, tk.END)
    height_entry.insert(0, ww)
    update_button()
def clickhp():
    sound()
    ww = int(height_entry.get())
    ww = ww +1
    height_entry.delete(0, tk.END)
    height_entry.insert(0, ww)
    update_button()


root.buttonhhh = Button(tab1,bd=3, text='H\u2193',command=clickhp, bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,cursor='hand2')
root.buttonhhh.place(x=630 + xxv, y=432 + yyv)
root.buttonHH = Button(tab1,bd=3, text='H\u2191',command=clickhm, bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,cursor='hand2')
root.buttonHH.place(x=590 + xxv, y=432 + yyv)

#buttonf = tk.Button(button_obj, text=text, fg=fg, bg=bg, font=(font, font_size))

root.buttonwww = Button(tab1,bd=3, text='W\u2192',command=clickwp, bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,cursor='hand2')
root.buttonwww.place(x=630 + xxv, y=403 + yyv)
root.buttonWW = Button(tab1,bd=3, text='W\u2190',command=clickwm, bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,cursor='hand2')
root.buttonWW.place(x=590 + xxv, y=403 + yyv)



root.buttonxm = Button(tab1, text='X\u2192',bd=3,command=clicksxm, bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,cursor='hand2')
root.buttonxm.place(x=630 + xxv, y=461 + yyv)

root.buttonx = Button(tab1, text='X\u2190',bd=3,command=clicksx, bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,cursor='hand2')
root.buttonx.place(x=590 + xxv, y=461 + yyv)

root.buttony = Button(tab1,command=clicksy,bd=3, text='Y\u2191', bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,cursor='hand2')
root.buttony.place(x=590 + xxv, y=490 + yyv)


root.buttonym = Button(tab1,command=clicksym,bd=3, text='Y\u2193', bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,cursor='hand2')
root.buttonym.place(x=629 + xxv, y=490 + yyv)

##bd yp
root.buttonyBdU = Button(tab1,command=clicksbdu,bd=3, text='B\u2191', bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,cursor='hand2')
root.buttonyBdU.place(x=590 + xxv, y=519 + yyv)

##bd down
root.buttonBdD = Button(tab1,command=clicksbdd,bd=3, text='B\u2193', bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,cursor='hand2')
root.buttonBdD.place(x=629 + xxv, y=519 + yyv)


root.buttonexit = Button(root,bd=3, text='Exit Program',command=clicks, bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=20,cursor='hand2')
root.buttonexit.place(x=496 + xxv, y=640 + yyv)

#============Main combo tools ======================='

def on_combobox_select(selection):

    defult()

tools = [ "Canvas","Button","Label","Entry","OptionMenu","Text","Combobox", "Checkbutton", "Radiobutton",   "Listbox", "ScrolledText","Treeview"]

combo_box_varmv1 = tk.StringVar(value="Canvas")
combo_boxmv1 = tk.OptionMenu(tab1, combo_box_varmv1, *tools, command=on_combobox_select)
combo_boxmv1.config(width=21,cursor='hand2')
combo_boxmv1.place(x=13+xxvv,y=245+yyvv)
combo_boxmv1.config(background=bgbgbg, foreground='white')
#=============================================

eventxy=[]
buttonlst=[]
buttoncount=1
buttonlistkey=False



comboboxw = ttk.Combobox(tab1, values=valuescombo, font=('Arial',9), foreground=bgbgbg, background=bgbgbg, height=1,
                          width=21,cursor='hand2')
comboboxw.place(x=495 + xxv, y=280 + yyv)
comboboxw_values = []

number=0

kinds=["t"]
TTcombo=13
TTcomcoMins=0
global colorjump
colorjump=False


# Load and resize the photo
photoimg = Image.open("C:/Users/PT/PycharmProjects/pythonProject/Imags/down.png")  # Replace with your photo path
photoimg = photoimg.resize((8, 15))  # Adjust the size as needed
photoimg = ImageTk.PhotoImage(photoimg)

# Create a canvas to display the photo
canvashola = tk.Canvas(root, width=8, height=15, background=bgbgbg,highlightbackground='black')

# Create the label
labelimg1 = tk.Label(canvashola, bg="white", compound=tk.CENTER, image=photoimg, background="black")

# Function to move the label
def move_label(ximg, yimg, move_distance):
    canvas_height = canvashola.winfo_height()
    label_height = labelimg1.winfo_height()

    if yimg + label_height >= canvas_height:
        yimg = canvas_height - label_height
        root.direction = -1
    elif yimg <= 0:
        yimg = 0
        root.direction = 1

    yimg += move_distance * root.direction
    labelimg1.place(x=ximg, y=yimg)

    root.after(100, move_label, ximg, yimg, move_distance)

#&
def on_combobox_selected(event):

    global button_widget
    global buttoncount
    global font_name
    global number
    global ximg,yimg
    selected_item = comboboxw.get()
    my_string = selected_item
    #print("hhhhhh  ",my_string)
    number = int(re.search(r'\d+', my_string).group())
    #print("hhhhh  ",number)
    grtmum[0]=number
    fg_entry.configure(state="normal")
    bg_entry.configure(state="normal")
    #print ("TTcombo",TTcombo)
    #print("hello")
    for i in range(0, len(buttonlst), TTcombo):
        #print("i search")
        if buttonlst[i] == number:
            #print("i foundi it in combo")
            #on_tool_click(buttonlst[i+1])
            buttoncount=number
            if TTcomcoMins==0:
                button_widget=""
                button_widget=buttonlst[i+1]

            if treeonoff[0]==True:

                    x_entry.delete(0, tk.END)
                    x_entry.insert(0, int(treeviewXY[0])+int(treeviewXY[2]))
                    y_entry.delete(0, tk.END)
                    #print(xdef)
                    y_entry.delete(0, tk.END)
                    y_entry.insert(0,int(treeviewXY[1])-int(treeviewXY[3]))

                    #button_click(treeviewname[0])


            else:
                x_entry.delete(0, tk.END)
                x_entry.insert(0, buttonlst[i+2-TTcomcoMins])
                y_entry.delete(0, tk.END)
                y_entry.insert(0, buttonlst[i+3-TTcomcoMins])

            height_entry.delete(0, tk.END)
            height_entry.insert(0, buttonlst[i+4]-TTcomcoMins)

            width_entry.delete(0, tk.END)
            width_entry.insert(0, buttonlst[i+5-TTcomcoMins])

            text_entry.delete(0, tk.END)
            text_entry.insert(0, buttonlst[i+6-TTcomcoMins])

            #show_message(buttonlst[i+6-TTcomcoMins]+"  Slected", (int(buttonlst[i+2-TTcomcoMins]))+20, (int(buttonlst[i+3-TTcomcoMins]))-60)
            fg_entry.delete(0, tk.END)
            fg_entry.insert(0,buttonlst[i+7-TTcomcoMins])

            bg_entry.delete(0, tk.END)
            bg_entry.insert(0, buttonlst[i+8-TTcomcoMins])

            mainfontlst[0] = buttonlst[i + 9-TTcomcoMins]
            #text_label7u.configure(font=(font_name, 10)
            #fnz_entry.delete(0, tk.END)
            #fnz_entry.insert(0, buttonlst[i + 10-TTcomcoMins])
            kinds[0]=buttonlst[i + 11-TTcomcoMins]

            Bd_entry.delete(0, tk.END)
            Bd_entry.insert(0, buttonlst[i + 12])
            #st2.insert(END,f"{buttonlst[i]} ==get=={number} x {buttonlst[i+2]} y {buttonlst[i+3]} hight {buttonlst[i+4]} width {buttonlst[i+5]} text {buttonlst[i+6]} Fg {buttonlst[i+7]} bg {buttonlst[i+8]} font_name {buttonlst[i + 9]} font_size {buttonlst[i + 10]}  kind {buttonlst[i + 11]} \n")
            update_button()

            button_width = button_widget.winfo_width() //2 -10
            #button_height = button_widget.winfo_height()  - 12
            rectangle = canvashola.create_rectangle(5, 5, 35, 22, fill="black")
            canvashola.place(x=int(x_entry.get())+ 3+button_width, y=int(y_entry.get()) -22)
            canvashola.configure(background=bg_entry.get(),highlightbackground=bg_entry.get())
            labelimg1.configure(background=bg_entry.get(),highlightbackground=bg_entry.get())
            move_label(0, 0, 2)
            #update_arrows(int(x_entry.get()), int(y_entry.get()))
            try:
                plus1.destroy(); plus2.destroy(); plus3.destroy(); plus4.destroy(); plus5.destroy(); plus6.destroy()
                plus7.destroy();plus8.destroy();plus9.destroy(); plus10.destroy();plus11.destroy(); plus12.destroy()
                delattr(update_arrows, "button_created")
            except:
                pass
            break
           # update_button()
    bg_entry.configure(state="disabled")
    fg_entry.configure(state="disabled")
comboboxw.bind("<<ComboboxSelected>>", on_combobox_selected)

addlist=[0]

#-----------------------------------------

getbutton=True
#======================================
plus1 = None;plus2 = None;plus3 = None;plus4 = None;plus5 = None;plus6 = None;plus7 = None;plus8 = None;plus9 = None;plus10 = None;plus11 = None;plus12 = None


destroyesno=False
def update_arrows(x, y,event):
    button = event.widget
    #print("Right-click on", button)
    global button_widget
    #print(button_widget)
    if button != button_widget :
        return button_widget

    global plus1, plus2, plus3, plus4,plus5,plus6,plus7, plus8,plus9,plus10,plus11,plus12

    if hasattr(update_arrows, "button_created") :
        # Buttons already created, destroy them
        plus1.destroy()
        plus2.destroy()
        plus3.destroy()
        plus4.destroy()
        plus5.destroy()
        plus6.destroy()
        plus7.destroy()
        plus8.destroy()
        plus9.destroy()
        plus10.destroy()
        plus11.destroy()
        plus12.destroy()
        delattr(update_arrows, "button_created")
    else:
        # Buttons not created yet, create them
        rect_width = button_widget.winfo_width()
        rect_height = button_widget.winfo_height()
        #print("rect height ",rect_width)
        #print (x,y)
        plus_x = x + rect_width // 2
        plus_y = y + rect_height+30

        # Button 1 w+
        plus5 = tk.Canvas(canvas1, height=87, width=200, bg=bgbgbg)
        plus5.place(x=plus_x, y=plus_y +25 )  # Adjusted y coordinate
        plus5_id = canvas1.create_window(plus_x, plus_y +25 , window=plus5)

        fname=f"Tools {text_entry.get()}"
        plus6 = tk.Label(canvas1, text=fname, fg='white', bg=bgbgbg, font=('Stencil', 10), height=1, width=14)
        plus6.place(x=plus_x, y=plus_y  -4)  # Adjusted y coordinate
        plus6_id = canvas1.create_window(plus_x, plus_y-4  , window=plus6)

        xpl=-18

        plus1 = Button(canvas1, text= 'W\u2192' , bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,
                       command=clickwp)
        plus1.place(x=plus_x + 54+xpl, y=plus_y+20 )  # Adjusted y coordinate
        plus1.configure(cursor='hand1')
        plus1_id = canvas1.create_window(plus_x + 54+xpl, plus_y+20 , window=plus1)
        canvas1.tag_bind(plus1_id, "<Button-1>", lambda event: clickwp())

        plus11 = Button(canvas1, text='B\u2191', bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,
                       command=clicksbdu)
        plus11.place(x=plus_x + 91+xpl, y=plus_y + 20)  # Adjusted y coordinate
        plus11.configure(cursor='hand1')
        plus11_id = canvas1.create_window(plus_x + 91+xpl, plus_y + 20, window=plus11)
        canvas1.tag_bind(plus11_id, "<Button-1>", lambda event: clickwp())

        plus12 = Button(canvas1, text='B\u2193', bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,
                        command=clicksbdd)
        plus12.place(x=plus_x + 91+xpl, y=plus_y + 51)  # Adjusted y coordinate
        plus12.configure(cursor='hand1')
        plus12_id = canvas1.create_window(plus_x + 91+xpl, plus_y + 51, window=plus12)
        canvas1.tag_bind(plus12_id, "<Button-1>", lambda event: clickwp())

        plus7 = Button(root, text='X\u2192', bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,command=clicksxm)
        plus7.place(x=plus_x + 54+xpl, y=plus_y + 51)
        plus7.configure(cursor='hand1')
        plus7_id = canvas1.create_window(plus_x + 54+xpl, plus_y + 51, window=plus7)
        canvas1.tag_bind(plus7_id, "<Button-1>", lambda event: clickwp())

        # Button 2 h+
        plus2 = Button(canvas1, text='H\u2193', bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3, command=clickhp)
        plus2.place(x=plus_x - 20+xpl, y=plus_y + 20)
        plus2.configure( cursor='hand1')
        plus2_id = canvas1.create_window(plus_x - 20+xpl, plus_y + 20, window=plus2)
        canvas1.tag_bind(plus2_id, "<Button-1>", lambda event: clickhp())

        #==== y+
        plus9 = Button(root, text='Y\u2193', bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,command=clicksym)
        plus9.place(x=plus_x - 20+xpl, y=plus_y + 51)
        plus9.configure(cursor='hand1')
        plus9_id = canvas1.create_window(plus_x - 20+xpl, plus_y + 51, window=plus9)
        canvas1.tag_bind(plus9_id, "<Button-1>", lambda event: clickwp())

        # Button 3 w-
        plus3 = Button(canvas1, text= 'W\u2190' , bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3, command=clickwm)
        plus3.place(x=plus_x+17+xpl , y=plus_y +20)
        plus3.configure(cursor='hand1')
        plus3_id = canvas1.create_window(plus_x +17+xpl, plus_y + 20, window=plus3)
        canvas1.tag_bind(plus3_id, "<Button-1>", lambda event: clickwm())

        plus8 = Button(root, text='X\u2190', bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,command=clicksx)
        plus8.place(x=plus_x+17+xpl, y=plus_y +51)
        plus8.configure(cursor='hand1')
        plus8_id = canvas1.create_window(plus_x +17+xpl, plus_y + 51, window=plus8)
        canvas1.tag_bind(plus8_id, "<Button-1>", lambda event: clickwp())

        # Button h-
        plus4 = Button(canvas1, text='H\u2191', bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,command=clickhm)
        plus4.place(x=plus_x - 56+xpl, y=plus_y +20)
        plus4.configure(cursor='hand1')
        plus4_id = canvas1.create_window(plus_x -56+xpl, plus_y + +20, window=plus4)
        canvas1.tag_bind(plus4_id, "<Button-1>", lambda event: clickhm())

        #=====y-
        plus10 = Button(root, text='Y\u2191', bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=3,command=clicksy)
        plus10.place(x=plus_x - 56+xpl, y=plus_y +1)
        plus10.configure(cursor='hand1')
        plus10_id = canvas1.create_window(plus_x -56+xpl, plus_y + 51, window=plus10)
        canvas1.tag_bind(plus10_id, "<Button-1>", lambda event: clickwp())

        setattr(update_arrows, "button_created", True)



#&u
#======================================
def update_button():

    global buttonlistkey
    global buttoncount
    global colorjump

    #text_label.configure(font=(font_name, 10))
    fg_entry.configure(state="normal")
    bg_entry.configure(state="normal")
    config = {}
    if bg_entry.get():
        if kinds[0]=="Combobox" or colorjump==True or kinds[0]=="Treeview" or kinds[0]=="Frame" or kinds[0]=="Scrollbar":
            pass
        else:
            colorjump = False
            config["bg"] = bg_entry.get()
        #print("***###**",bg_entry.get())
    #--text
    if fg_entry.get():
        if kinds[0]=="Canvas" or  kinds[0]=="Combobox" or kinds[0]=="Treeview" or kinds[0]=="Frame" or kinds[0]=="Scrollbar":
            pass
        else:
            config["fg"] = fg_entry.get()
    if text_entry.get():
        if kinds[0] == "Listbox" or kinds[0]=="Canvas" or kinds[0] == "Text" or kinds[0] == "ScrolledText" or kinds[0]=="Treeview" or kinds[0]=="Frame" or kinds[0]=="Scrollbar":
            pass
        else:
           config["text"] = text_entry.get()
    if width_entry.get():

        if kinds[0] == "Treeview" or kinds[0]=="Scrollbar":
            pass
        else:
            config["width"] = int(width_entry.get())
    if height_entry.get():
        if kinds[0] == "Entry" or kinds[0]=="Scrollbar" :
            pass
        else:
           config["height"] = int(height_entry.get())
    if x_entry.get() and y_entry.get():
        x, y = int(x_entry.get()), int(y_entry.get())

    if Bd_entry.get():
        if kinds[0].strip() == "Combobox" or kinds[0] == "Treeview" or kinds[0]=="Scrollbar":
            pass
        else:
            config["borderwidth"] = int(Bd_entry.get())
            config["relief"] ='ridge'
    # ----------------------------------------
    #print(button_widget)


    #config["font"]=font
    #print(button_widget)
    button_widget.place(x=x, y=y)
    button_widget.config(**config)
    button_widget.bind("<ButtonPress-1>", on_drag_start)
    button_widget.bind("<B1-Motion>", on_drag_motion)
    button_widget.bind("<ButtonRelease-1>", on_drag_stop)
    button_widget.bind("<Button-3>", lambda event: update_arrows(x, y,event))



        #button_widget.bind("<Button-3>", update_arrows(x,y))

    #print("i send to update arrows")
    if isinstance(button_widget, ttk.Treeview):
        button_widget.place(x=x, y=y, width=int(width_entry.get()), height=int(height_entry.get()))
        button_widget.bind("<ButtonPress-1>", on_drag_start)
        button_widget.bind("<B1-Motion>", on_drag_motion)
        button_widget.bind("<ButtonRelease-1>", on_drag_stop)
        button_widget.bind("<Button-3>", lambda event: update_arrows(x, y, event))
    # ===========================================================================
    if kinds[0].strip() == "Combobox" :
        if buttonlistkey == True:
             fg_entry.delete(0,END)
             fg_entry.insert(0,"green")
             button_widget.config(width=int(width_entry.get()))
             button_widget.config(foreground=fg_entry.get())
             button_widget.config(background=bg_entry.get())
             default_values = text_entry.get().split(',')
             default_button_value = default_values[0]
             #print("====defult combo value=====", default_button_value)
             button_widget['values'] = default_values
             button_widget.set(default_button_value)

        else:

            button_widget.config(width=int(width_entry.get()))
            button_widget.config(foreground=fg_entry.get())
            button_widget.config(background=bg_entry.get())

            default_values = text_entry.get().split(',')
            default_button_value = default_values[0]
            #print("====defult combo value=====",default_button_value)
            button_widget['values'] = default_values
            button_widget.set(default_button_value)

    if kinds[0].strip() == "Entry" and keydrag != False and switch[0]!=True:
        button_widget.delete(0, tk.END)
        button_widget.insert(0,text_entry.get())

        text_entry.delete(0, tk.END)
        text_entry.insert(0, "Entry " + str(addlist[0] + 1))
        # print("combo color")
        #button_widget.configure(foreground=fg_entry.get(), background=bg_entry.get(),width=int(width_entry.get()))
    if isinstance(button_widget, tk.Canvas) or isinstance(button_widget, ttk.Treeview) or kinds[0]=="Frame" or kinds[0]=="Treeview" or kinds[0]=="Scrollbar":
        pass
    else:
        fontst = mainfontlst[0]
        #print("====font in update===",fontst)
        button_widget.configure(font=fontst)
        button_widget.configure(font=fontst)

    if buttonlistkey==True and getbutton != False:
        #print("i add it to list :)")
               # button_widget.configure(foreground=fg_entry.get(), background=bg_entry.get())
        addlist[0]=addlist[0]+1
        #print(addlist[0],kinds[0])
        grtmum[0]=addlist[0]
        buttonlst.append(addlist[0])
        buttoncount=addlist[0]
        #print(buttoncount,"when add=================")
        buttonlst.append(button_widget)
        buttonlst.append(x)
        buttonlst.append(y)
        buttonlst.append(int(height_entry.get()))
        buttonlst.append(int(width_entry.get()))
        if kinds[0].strip() == "Canvas":
            #print("yes","Canvas" + str(addlist[0]))
            buttonlst.append("Canvas" + str(addlist[0]))
        elif kinds[0].strip() == "Text":
            f = f"Text {addlist[0]}"
            buttonlst.append(f)
        elif kinds[0].strip() == "ScrolledText":
            f = f"ScrolledText {addlist[0]}"
            buttonlst.append(f)
        else:
            buttonlst.append(text_entry.get())

        buttonlst.append(fg_entry.get())
        buttonlst.append(bg_entry.get())

        buttonlst.append(mainfontlst[0])
        buttonlst.append(9)
        tool = kinds[0]

        buttonlst.append(tool)

        buttonlst.append(int(Bd_entry.get()))

        #print('======New Button========>',addlist[0])
        #print(buttonlst)
        #`st2.insert(END,
               #    f"Code {buttonlst[addlist[0]]}==>{buttonlst[addlist[0]]} ==get=={number} x {buttonlst[i + 2]} y {buttonlst[i + 3]} hight {buttonlst[i + 4]} width {buttonlst[i + 5]} text {buttonlst[i + 6]} Fg {buttonlst[i + 7]} bg {buttonlst[i + 8]} font_name {buttonlst[i + 9]} font_size {buttonlst[i + 10]}  kind {buttonlst[i + 11]} \n")
        #print("I save it")
        #print(buttonlst)

        bg_entry.configure(state="disabled")
        fg_entry.configure(state="disabled")
        buttonlistkey = False

    else:
        if getbutton != False:
           if kinds[0].strip() == "Combobox":
               button_widget.config(width=int(width_entry.get()))
               button_widget.config(foreground=fg_entry.get())
               button_widget.config(background=bg_entry.get())
               default_values = text_entry.get().split(',')
               default_button_value = default_values[0]
               # print("====defult combo value=====",default_button_value)
               button_widget['values'] = default_values
               button_widget.set(default_button_value)

           for i in range(0, len(buttonlst), 13):
                if buttonlst[i] == buttoncount:
                   if buttonlistkey==True:
                           buttoncount=buttoncount-1
                   #print(buttonlst[i],"------Update------->",buttoncount)
                   buttonlst[i+2]=x
                   buttonlst[i+3]=y
                   buttonlst[i+4]=int(height_entry.get())
                   buttonlst[i+5]=int(width_entry.get())
                   buttonlst[i+6]=text_entry.get()
                   if switch[0] == True:
                       button_widget.delete(0,END)
                       button_widget.insert(0,text_entry.get())
                   if kinds[0].strip() == "Canvas":
                        buttonlst[i + 6]=("Canvas" + str(buttoncount))
                        text_entry.delete(0, tk.END)
                        text_entry.insert(0, ("Canvas" + str(buttoncount)))
                   elif kinds[0].strip() == "Listbox" :
                        buttonlst[i + 6] = ("Listbox " + str(buttoncount))
                        text_entry.delete(0, tk.END)
                        text_entry.insert(0, ("Listbox " + str(buttoncount)))
                   elif kinds[0].strip() == "Combobox":
                           f = f"Combo {str(buttoncount)}"
                           button_widget.delete(0, tk.END)
                           button_widget.insert(tk.END, f)

                   buttonlst[i+7]=fg_entry.get()
                   buttonlst[i+8]=bg_entry.get()
                   #print("***#modifay##**", bg_entry.get())
                   buttonlst[i+9]=mainfontlst[0]
                   buttonlst[i + 10] = 9
                   buttonlst[i+12]=int(Bd_entry.get())
                   #print(buttonlst)
                   #st2.insert(END,f"Code {buttonlst[i+0]}==>{buttonlst[i]} ==get=={number} x {buttonlst[i + 2]} y {buttonlst[i + 3]} hight {buttonlst[i + 4]} width {buttonlst[i + 5]} text {buttonlst[i + 6]} Fg {buttonlst[i + 7]} bg {buttonlst[i + 8]} font_name {buttonlst[i + 9]} font_size {buttonlst[i + 10]}  kind {buttonlst[i + 11]} \n")
                   bg_entry.configure(state="disabled")
                   fg_entry.configure(state="disabled")
                   break


    #print(buttonlst)
    #print("getbutton",getbutton)
    if getbutton!=False:
         cou=0
         comboboxw_values = []
         comboboxw['values'] = ()

         for t in range(0, len(buttonlst), 13):
               comstr=f"{str(buttonlst[t])}  {buttonlst[t+6]}"
               comboboxw_values.append(comstr)
               comboboxw["values"] = comboboxw_values



#------------------------------------------------
Fontttty = "Arial",11
#st2 = ScrolledText.ScrolledText(width=114,height=10,wrap=WORD, background="black", font=Fontttty , fg='#7fff00')
#st2.place(x=5, y=5+yy)
#===============================================================
#&d
def defult():
    global buttoncount
    global number
    global grtmum
    kinds[0]="t"
    number = 0
    grtmum = [0]
    buttoncount=0
    mainfontlst=("Arial 9 bold")
    #text_label.configure(font=(font_name))
    fg_entry.configure(state="normal")
    bg_entry.configure(state="normal")
    #x_entry = tk.Entry(entry_framev)
    x_entry.delete(0, tk.END)
    #y_entry = tk.Entry(entry_framev)
    x_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    width_entry.delete(0, tk.END)
    text_entry.delete(0, tk.END)
    fg_entry.delete(0, tk.END)
    bg_entry.delete(0, tk.END)
    #fnz_entry.delete(0, tk.END)
    Bd_entry.delete(0, tk.END)
    Bd_entry.insert(0,default_config["borderwidth"])
    #fnz_entry.insert(0, default_config["font size"])
    bg_entry.insert(0, default_config["bg"])
    fg_entry.insert(0, default_config["fg"])
    tool = kinds[0]
    if tool == "Button":
         text_entry.insert(0,"Button " +str(addlist[0]+1))
    elif tool == "Checkbutton":
        text_entry.insert(0, "Check " + str(addlist[0] + 1))
    elif tool == "Entry":
        text_entry.insert(0, "Entry " + str(addlist[0] + 1))
    elif tool == "Listbox":
        text_entry.insert(0, "Listbox " + str(addlist[0] + 1))
    elif tool == "Label":
        text_entry.insert(0, "Label " + str(addlist[0] + 1))
    elif tool == "Radiobutton":
        text_entry.insert(0, "RadioB " + str(addlist[0] + 1))
    elif tool == "ScrolledText":
        text_entry.insert(0, "ScrolledText " + str(addlist[0] + 1))
    elif tool == "Combobox":
        fg_entry.delete(0, tk.END)
        fg_entry.insert(0, 'blue')
        bg_entry.delete(0, tk.END)
        bg_entry.insert(0, 'teal')
    elif tool == "Canvas":
        text_entry.insert(0, "Canvas" + str(addlist[0] + 1))
    elif tool == "OptionMenu":
        text_entry.insert(0, "OptionM " + str(addlist[0] + 1))
    elif tool == "Text":
        text_entry.insert(0, "Text " + str(addlist[0] + 1))
    elif tool == "Treeview":
        height_entry.delete(0, tk.END)
        width_entry.delete(0, tk.END)
        height_entry.insert(0, 200)
        width_entry.insert(0, 680)


    if tool == "Combobox":
        text_entry.insert(0, "Combobox " + str(addlist[0] + 1))
        width_entry.delete(0, tk.END)
        width_entry.insert(0, 10)
        bg_entry.insert(0, "teal")
        fg_entry.insert(0, "green")
    else:
        width_entry.insert(0, default_config["width"])

    height_entry.insert(0, default_config["height"])
    #x_entry = tk.Entry(entry_framev)
    x_entry.insert(0, 50)  # Set default value
    #y_entry = tk.Entry(entry_framev)
    y_entry.insert(0, 50)  # Set default value

    bg_entry.configure(state="disabled")
    fg_entry.configure(state="disabled")

#================================================================

widgets = []
buttonnamenew=["g"]


keydrag=False
#=============================================================================
label = tk.Label(canvas1, text="Canvas 1", font=('Stencil', 14),bg="yellow",fg="black")
def show_message(message,x,y):
    label.config(text=message)
    label.place(x=x-28,y=y)
    label.after(2000, hide_message)
def hide_message():
    label.place_forget()

#==============================================================================
def button_click(button_name):

    global comboboxw
    global plus6

    comboboxw_values = []
    comboboxw['values'] = ()

    for t in range(0, len(buttonlst), 13):
        comstr = f"{str(buttonlst[t])}  {buttonlst[t + 6]}"
        comboboxw_values.append(comstr)
        comboboxw["values"] = comboboxw_values

    #print(f"Pressed: {button_name}")
    butonstr=button_name.strip()
    #print(butonstr,"هذا اهم شي")

    for h in range(len(comboboxw_values)):
        #print(comboboxw_values[h])
        text = str(comboboxw_values[h])
        new_text = text.lstrip('0123456789').strip()
        try:
            plus6.config(text="Tools " + new_text)

        except:
            pass

        if new_text==butonstr:
            #print(new_text, "===b click 1487 ===", butonstr)
            #print("I found it :)")
            comboboxw.current(h)
            on_combobox_selected(h)

            break
        #print("ffff",h)
    #comboboxw.current(button_name)
    #on_combobox_selected(button_name)


global KeyDragOnOffName
KeyDragOnOffName=["none"]
optinmaddss=[]
chkbuttonhh=[]
radiobtms=[]
treeonoff=[False]
treefx=[False]
treeviewXY=[0,0,0,0]
#&ds
def on_drag_start(event):
    sound()
    #print(event.widget)
    #print("====Events= in drag ==>",type(event.widget))
    if isinstance(event.widget, tk.Canvas):
            #print("iam canves man")
            canvas_id = event.widget.find_withtag("pointer")
            if canvas_id:
                canvas = event.widget
                canvas_tags = canvas.itemcget(canvas_id, "tags")
                if canvas_tags:
                    additional_tags = canvas_tags.split()[1:]
                    for tag in additional_tags:
                        # print("Canvas Tag:", tag)
                        KeyDragOnOffName[0] = tag
                        button_click(tag)
    elif isinstance(event.widget, tk.Button):
            button_text = event.widget.cget("text")
            KeyDragOnOffName[0] = button_text
            button_click(button_text)
            #print("its button man")
    elif isinstance(event.widget, tk.Label):
            label_text = event.widget.cget("text")
            KeyDragOnOffName[0] = label_text
            button_click(label_text)
            #print("its label man")
    elif isinstance(event.widget, tk.Entry):
            global button_widget
            selected_widget = event.widget
            # print(event)
            selected_text = selected_widget.get()
            #print("Selected Text:", selected_text)
            KeyDragOnOffName[0] = selected_text
            button_click(selected_text)
    elif isinstance(event.widget, OptionMenu):
        xmenu = 0
        for gh in optinmaddss:
            if gh == event.widget["menu"]:
                # print(event.widget["menu"], "======", gh)
                # print (optinmaddss[xmenu-2])
                KeyDragOnOffName[0] = optinmaddss[xmenu - 2]
                #print("==========1543====",optinmaddss[xmenu - 2])
                button_click(optinmaddss[xmenu - 2])
                break
            xmenu += 1
    elif isinstance(event.widget, tk.Text):
            #print("The variable is of type str")
            selected_widget = event.widget
            # print(event)
            selected_text = selected_widget.get("1.0", 'end-1c')
            # print("Selected Text:", selected_text)
            KeyDragOnOffName[0] = selected_text
            button_click(selected_text)
    elif isinstance(event.widget, ttk.Combobox):
            selected_value = event.widget.get()
            # print("Selected Value:", selected_value)
            KeyDragOnOffName[0] = selected_value
            button_click(selected_value)
    elif isinstance(event.widget, tk.Checkbutton):
            xmaxz = 0
            for xmax in chkbuttonhh:
                if xmax == event.widget:
                    # print("eeee"  ,event.widget)
                    # print (chkbuttonhh[xmaxz+1])
                    KeyDragOnOffName[0] = chkbuttonhh[xmaxz + 1]
                    button_click(chkbuttonhh[xmaxz + 1])

                    break
                xmaxz += 1

    elif isinstance(event.widget, tk.Radiobutton):
        sokokl = 0
        for xmaxr in radiobtms:
            if xmaxr == event.widget:
                # print("eeee"  ,event.widget)
                # print (chkbuttonhh[xmaxz+1])
                KeyDragOnOffName[0] = radiobtms[sokokl + 1]
                button_click(radiobtms[sokokl + 1])

                break
            sokokl += 1
    elif isinstance(event.widget, tk.Listbox):
        selected_text = event.widget.get([0])
        KeyDragOnOffName[0] = selected_text
        button_click(selected_text)
    elif isinstance(event.widget, ttk.Treeview):

        #print(event.widget)
        str =f"{event.widget}"
        split_str = str.split("!")
        result = split_str[2]
        if result.strip() == 'treeview':
            result=f"treeview1"
            button_click(result)
            # print("==1601=in drag==treeview update",treeviewXY)
            keydrag = False
            treefx[0] = True
    elif isinstance(event.widget, tk.Frame):
        button_click(frames[0])
        #print("frame")

        #print(result)
        treefx[0]=True
    elif isinstance(event.widget, ttk.Scrollbar):
        button_click(scrolls[0])




    if type(event.widget) == scrolledtext.ScrolledText:
        text = event.widget.get("1.0", tk.END)
        KeyDragOnOffName[0] = text
        button_click(text)

    global is_dragging
    is_dragging = True
    event.widget.startX = event.x
    event.widget.startY = event.y

def on_drag_motion(event):
        global keydrag
        if treefx[0] == True and isinstance(event.widget, tk.Frame):
            x = event.x
            y = event.y
            x_entry.delete(0, tk.END)
            y_entry.delete(0, tk.END)
            x_entry.insert(0, x)
            y_entry.insert(0, y)
            button_click(frames[0])
        if treefx[0] == True and isinstance(event.widget, ttk.Treeview):
            x = event.x
            y = event.y
            x_entry.delete(0, tk.END)
            y_entry.delete(0, tk.END)
            x_entry.insert(0, x)
            y_entry.insert(0, y)
            button_click(treeviewname[0])

            #print("== yes ==", event.widget,"==",x,"===",y)
        delta_x = event.x - event.widget.startX
        delta_y = event.y - event.widget.startY
        event.widget.place(x=event.widget.winfo_x() + delta_x, y=event.widget.winfo_y() + delta_y)
        x_entry.delete(0, tk.END)
        y_entry.delete(0, tk.END)
        x_entry.insert(0, event.widget.winfo_x() + delta_x)
        y_entry.insert(0, event.widget.winfo_y() + delta_y)



def on_drag_stop(event):
    xxxmm=-10
    update_button()
    button_width = button_widget.winfo_width() // 2 + xxxmm
    # button_height = button_widget.winfo_height()  - 12
    rectangle = canvashola.create_rectangle(5, 5, 35, 22, fill="black")
    canvashola.place(x=int(x_entry.get())+5 + button_width, y=int(y_entry.get()) - 22)
    canvashola.configure(background=bg_entry.get(),highlightbackground=bg_entry.get())
    labelimg1.configure(background=bg_entry.get(),highlightbackground=bg_entry.get())
    move_label(0, 0, 2)


    if treefx[0] == True:
            treeviewXY[0] = event.widget.winfo_x()
            treeviewXY[1] = event.widget.winfo_y()
            #print("====in  1642 select button treeview  =====", treeviewXY)
            treefx[0] = False
            xtreeadd=0
            for t in range(0, len(treeviewtools), 3):
                  treeviewXY[2]=int(treeviewtools[xtreeadd+1])
                  treeviewXY[3]=int(treeviewtools[xtreeadd + 2])
                  treeonoff[0] = True
                  button_click(treeviewtools[t])
                  xtreeadd=xtreeadd+3
                  # print("==1601=in drag==treeview update",treeviewXY)
            #button_click(treeviewname[0])
    treeonoff[0] = False


    #print("finish")


#root = tk.Tk()

def callrowwsupdown():
    global button_widget
    #print(type(button_widget))
    xxxmm=0
    if isinstance(button_widget, tk.Canvas):
        xxxmm=xxxmm+65
    elif isinstance(button_widget, tk.Checkbutton):
        xxxmm = xxxmm + 38
    elif isinstance(button_widget, tk.Entry):
        xxxmm = xxxmm + 52
    elif isinstance(button_widget, tk.Label):
        xxxmm = xxxmm + 13
    elif isinstance(button_widget, tk.Listbox):
        xxxmm = xxxmm + 5
    elif isinstance(button_widget, tk.Radiobutton):
        xxxmm = xxxmm + 38
    elif isinstance(button_widget, tk.Text):
        xxxmm = xxxmm + 22
    elif isinstance(button_widget, tk.OptionMenu):
        xxxmm = xxxmm + 35
    elif isinstance(button_widget, ttk.Treeview):
        xxxmm = xxxmm + 330
    if type(button_widget) == scrolledtext.ScrolledText:
        #print("ok")
        xxxmm = xxxmm + 65


    button_width = button_widget.winfo_width() // 2+xxxmm
    # button_height = button_widget.winfo_height()  - 12
    rectangle = canvashola.create_rectangle(5, 5, 35, 22, fill="black")
    canvashola.place(x=int(x_entry.get())+3 + button_width, y=int(y_entry.get()) - 22)
    canvashola.configure(background=bg_entry.get(),highlightbackground=bg_entry.get())
    labelimg1.configure(background=bg_entry.get(),highlightbackground=bg_entry.get())
    move_label(0, 0, 2)

treeviewlst=["Name", "Age", "Job", "Email", "Gender", "Mobile", "Address"]

treeviewname=[""]
treeviewtools=[]
treelabels=[]
treeEntrys=[]
frames=[]
scrolls=[]
#&dt
def draw_tool(event):
    try:
        plus1.destroy();plus2.destroy();plus3.destroy();plus4.destroy();plus5.destroy();plus6.destroy()
        plus7.destroy();plus8.destroy();plus9.destroy();plus10.destroy();plus11.destroy();plus12.destroy()
        delattr(update_arrows, "button_created")
    except:
        pass
    if keydrag!= True:
        defult()
        global buttonlistkey
        buttonlistkey = True
        eventxy = []
        sound()
        global button_widget
        tool = combo_box_varmv1.get()

        if tool:
            x, y = event.x, event.y
            if tool == "Button":
                f = f"Button {addlist[0] + 1}"
                buttonnamenew[0] = f
                button_widget = tk.Button(canvas1, text=f)
                canvas1.create_window(x, y,window=button_widget)
                button_widget.config(font="Arial 9 bold")

                eventxy.append(event.x)
                eventxy.append(event.y)
                x_entry.delete(0, tk.END)
                x_entry.insert(0, event.x)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, event.y)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                kinds[0] = tool
                #update_arrows(int(x_entry.get()), int(y_entry.get()))
                update_button()
                callrowwsupdown()

            elif tool == "Canvas":
                f = f"Canvas{addlist[0] + 1}"
                ff = f"Canvas{addlist[0]}"
                buttonnamenew[0]=f
                button_widget = tk.Canvas(canvas1)
                canvas1.create_window(x, y, window=button_widget)
                pointer_id = button_widget.create_rectangle(0, 0, 1, 1, fill="", outline="",
                                                     tags=("pointer", f))
                eventxy.append(event.x)
                eventxy.append(event.y)
                width_entry.delete(0, tk.END)
                width_entry.insert(0, 150)
                height_entry.delete(0, tk.END)
                height_entry.insert(0, 110)
                x_entry.delete(0, tk.END)
                x_entry.insert(0, event.x)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, event.y)
                kinds[0] = tool
                update_button()
                callrowwsupdown()
            elif tool == "Checkbutton":
                f = f"Checkbutton{addlist[0] + 1}"
                ff = f"Check {addlist[0] + 1}"
                buttonnamenew[0] = f
                x, y = event.x, event.y
                button_widget = tk.Checkbutton(canvas1, text="Button")
                #button_widget.bind("<Button-3>", on_checkbuttonhh_event1)
                eventxy.append(event.x)
                eventxy.append(event.y)
                x_entry.delete(0, tk.END)
                x_entry.insert(0, event.x)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, event.y)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, ff)
                kinds[0] = tool
                update_button()
                callrowwsupdown()
                #print(button_widget)
                chkbuttonhh.append(button_widget)
                chkbuttonhh.append(ff)
                #print(chkbuttonhh)
            elif tool == "Entry":
                f = f"Entry{addlist[0] + 1}"
                buttonnamenew[0] = f
                #canvas1.create_window(x, y, window=tk.Entry(canvas1))
                x, y = event.x, event.y
                f=f"Entry {addlist[0]+1}"
                tool = "Entry"
                kinds[0]=tool
                button_widget = tk.Entry(canvas1)
                canvas1.create_window(x, y, window=button_widget)
                button_widget.delete(0, tk.END)
                button_widget.insert(0, f)
                eventxy.append(event.x)
                eventxy.append(event.y)
                width_entry.delete(0, tk.END)
                width_entry.insert(0, 18)
                x_entry.delete(0, tk.END)
                x_entry.insert(0, event.x)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, event.y)
                kinds[0] = tool
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                update_button()
                callrowwsupdown()
            elif tool == "Label":
                f = f"Label{addlist[0] + 1}"
                buttonnamenew[0] = f
                #canvas1.create_window(x, y, window=tk.Label(canvas1, text="Label"))
                button_widget = tk.Label(canvas1, text="Label")
                canvas1.create_window(x, y, window=button_widget)

                button_widget.config(font=("Arial", 10))
                eventxy.append(event.x)
                eventxy.append(event.y)
                width_entry.delete(0, tk.END)
                width_entry.insert(0, 10)
                x_entry.delete(0, tk.END)
                x_entry.insert(0, event.x)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, event.y)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                kinds[0] = tool
                update_button()
                callrowwsupdown()
            elif tool == "Listbox":
                f = f"Listbox {addlist[0] + 1}"
                buttonnamenew[0] = f
                #canvas1.create_window(x, y, window=tk.Listbox(canvas1, height=3))
                button_widget = tk.Listbox(canvas1)
                canvas1.create_window(x, y, window=button_widget)

                button_widget.config(font=("Arial", 10),width=11)
                button_widget.insert(END, "Listbox " + str(addlist[0] + 1))
                width_entry.delete(0, tk.END)
                width_entry.insert(0, 15)
                height_entry.delete(0, tk.END)
                height_entry.insert(0, 11)
                eventxy.append(event.x)
                eventxy.append(event.y)
                x_entry.delete(0, tk.END)
                x_entry.insert(0, event.x)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, event.y)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                kinds[0] = tool

                update_button()
                callrowwsupdown()

            elif tool == "Menubutton":
                f = f"Menubutton{addlist[0] + 1}"
                buttonnamenew[0] = f
                menu = tk.Menu(canvas1)

                menu.add_command(label="خيار 1", command=lambda: print("تم اختيار الخيار 1"))
                menu.add_command(label="خيار 2", command=lambda: print("تم اختيار الخيار 2"))

                canvas1.create_window(x, y, window=tk.Menubutton(canvas1, text="Menu", menu=menu))
                kinds[0] = tool

            elif tool == "Radiobutton":
                f = f"Radiobutton{addlist[0] + 1}"
                ff = f"RadioB {addlist[0] + 1}"
                buttonnamenew[0] = f
                #canvas1.create_window(x, y, window=tk.Radiobutton(canvas1, text="Radiobutton", value=1))
                x, y = event.x, event.y
                button_widget = tk.Radiobutton(canvas1, text="Button")
                eventxy.append(event.x)
                eventxy.append(event.y)
                x_entry.delete(0, tk.END)
                x_entry.insert(0, event.x)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, event.y)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, ff)
                kinds[0] = tool
                #print(button_widget)

                radiobtms.append(button_widget)
                radiobtms.append(ff)
                update_button()
                callrowwsupdown()
            elif tool == "Text":
                f = f"Text{addlist[0] + 1}"
                buttonnamenew[0] = f
                #canvas1.create_window(x, y, window=tk.Text(canvas1, height=3, width=20))
                x, y = event.x, event.y
                button_widget = tk.Text(canvas1)

                #button_widget.bind("<Button-3>", on_text_click)

                f = f"Text {addlist[0] + 1}"

                button_widget.insert(tk.END, f)
                eventxy.append(event.x)
                eventxy.append(event.y)
                x_entry.delete(0, tk.END)
                x_entry.insert(0, event.x)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, event.y)
                kinds[0] = tool
                update_button()
                callrowwsupdown()

            elif tool == "ScrolledText":
                f = f"ScrolledText{addlist[0] + 1}"
                buttonnamenew[0] = f
                x, y = event.x, event.y
                button_widget = scrolledtext.ScrolledText(canvas1, width=25, height=15)
                #button_widget.create_window(x, y, window=button_widget)

                button_widget.place(x=x, y=y)

                #button_widget = tk.ScrolledText(canvas1)
                f = f"ScrolledText {addlist[0] + 1}"
                button_widget.insert(tk.END, f)
                width_entry.delete(0, tk.END)
                width_entry.insert(0, 25)
                height_entry.delete(0, tk.END)
                height_entry.insert(0, 6)
                eventxy.append(event.x)
                eventxy.append(event.y)
                x_entry.delete(0, tk.END)
                x_entry.insert(0, event.x)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, event.y)
                kinds[0] = tool
                update_button()
                callrowwsupdown()

            elif tool == "Combobox":
                f = f"Combobox{addlist[0] + 1}"
                buttonnamenew[0] = f
                addlist.append(len(addlist))
                x, y = event.x, event.y
                f = f"Combo {addlist[0] + 1}"
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                #values = text_entry.get()
                #button_widget = ttk.Button(root, text='Add Value', command=add_value)
                default_values = text_entry.get().split(',')# Provide default values here
                button_widget = ttk.Combobox(canvas1, values=default_values, width=15)
                button_widget.place(x=x, y=y)


                #button_widget.bind("<Button-3>", on_combobox_right_click)
                button_widget.set(default_values[0])
                width_entry.delete(0, tk.END)
                width_entry.insert(0, 15)
                bg_entry.delete(0, tk.END)
                bg_entry.insert(0, 'teal')
                fg_entry.delete(0, tk.END)
                fg_entry.insert(0, 'green')
                eventxy.append(event.x)
                eventxy.append(event.y)
                x_entry.delete(0, tk.END)
                x_entry.insert(0, event.x)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, event.y)
                kinds[0] = tool
                update_button()
            elif tool == "OptionMenu":

                global option
                global variable
                f = f"OptionMenu{addlist[0] + 1}"
                buttonnamenew[0] = f
                options = ["Option 1", "Option 2", "Option 3"]
                variable = tk.StringVar(canvas1)
                variable.set(options[0])
                button_widget = tk.OptionMenu(canvas1, variable, *options)
                button_widget.configure(width=7, foreground="white", background="teal")
                button_widget.place(x=x, y=y)
                width_entry.delete(0, tk.END)
                width_entry.insert(0, 7)
                fg_entry.configure(state="normal")
                bg_entry.configure(state="normal")
                bg_entry.delete(0, tk.END)
                bg_entry.insert(0, 'teal')
                fg_entry.delete(0, tk.END)
                fg_entry.insert(0, 'white')
                bg_entry.configure(state="disabled")
                fg_entry.configure(state="disabled")
                x_entry.delete(0, tk.END)
                x_entry.insert(0, event.x)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, event.y)
                f = f"OptionM{addlist[0] + 1}"
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                button_widget["menu"].delete("0", "end")
                options = []
                new_option = f
                kinds[0] = tool
                options.append(new_option)
                variable.set(options[0])  # reset the selected value to the first option
                button_widget["menu"].delete(0, "end")  # delete the existing menu items
                for option in options:
                    button_widget["menu"].add_command(label=option, command=tk._setit(variable, option))
                    #print(option,variable)
                    optinmaddss.append(option)
                    optinmaddss.append(variable)
                    optinmaddss.append(button_widget["menu"])
                update_button()
                callrowwsupdown()

            elif tool == "Treeview":
                f="sh"
                if treeviewname[0] != "":
                    return f

                tool = "Canvas"
                f = f"Canvas{addlist[0] + 1}"
                ff = f"Canvas{addlist[0]}"
                treeviewtools.append(f)
                #buttonnamenew[0] = f
                button_widget = tk.Canvas(canvas1)
                canvas1.create_window(x, y-179, window=button_widget)
                pointer_id = button_widget.create_rectangle(0, 0, 1, 1, fill="", outline="",
                                                       tags=("pointer", f))
                button_widget.lower(pointer_id)
                text_entry.delete(0,tk.END)
                text_entry.insert(0,f)
                width_entry.delete(0, tk.END)
                width_entry.insert(0,688)
                height_entry.delete(0, tk.END)
                height_entry.insert(0, 385)
                x_entry.delete(0, tk.END)
                treeviewtools.append(-8)
                treeviewtools.append(184)
                x_entry.insert(0, x-8)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y-186)
                kinds[0] = tool

                buttonlistkey = True
                update_button()

                #&f--------------------------------------------------------------
                tool = "Frame"
                f = f"Frame{addlist[0] + 1}"
                frames.append(f)
                treeviewtools.append(f)
                # buttonnamenew[0] = f
                button_widget =  tk.Frame(canvas1, width=684, height=173)
                frames.append(button_widget)
                #button_widget.place(x=235, y=300)
                button_widget.place(x=x, y=y)
                button_widget.pack_propagate(0)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                width_entry.delete(0, tk.END)
                width_entry.insert(0, 684)
                height_entry.delete(0, tk.END)
                height_entry.insert(0, 173)
                x_entry.delete(0, tk.END)
                treeviewtools.append(-2)
                treeviewtools.append(-30)
                x_entry.insert(0, x - 2)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y+28 )
                kinds[0] = tool
                buttonlistkey = True
                update_button()
                #return tool
                #----------------------------------------------------------------------

                tool = "Treeview"
                f = f"treeview{addlist[0] + 1}"

                treeviewname[0]=f
                style = ttk.Style()
                #style.configure("Custom.Treeview", rowheight=17, font=("Arial", 9), borderwidth=2, relief="ridge",
                                #foreground="black", background="teal")
                frame=frames[1]
                frame.configure(width=684, height=173)
                style.configure("Custom.Treeview", rowheight=17, font=("Arial", 9), borderwidth=2, relief="ridge",
                                foreground="black", background="teal")
                button_widget.treeview = ttk.Treeview(frame, columns=(
                    "Student", "Number", "Mat", "Aloom", "Fan", "Feezia", "Ayashy", "Londa", "Akram", "Saad", "Saja",
                    "Motaz",
                    "Fahad", "Royd", "Ana", "Paris", "Sokowawa", "Batkh", "Jorgea", "Balata", "Mosco"),
                                             style="Custom.Treeview",
                                             cursor="hand2", height=10)
                button_widget.treeview.heading("#0", text="ID", anchor="center")
                button_widget.treeview.column("#0", width=50)

                button_widget.treeview.heading("Student", text="Student", anchor="w")
                button_widget.treeview.column("Student", width=75)
                button_widget.treeview.heading("Number", text="Number", anchor="w")
                button_widget.treeview.column("Number", width=75)
                button_widget.treeview.heading("Mat", text="Mat", anchor="w")
                button_widget.treeview.column("Mat", width=75)
                button_widget.treeview.heading("Aloom", text="Aloom", anchor="w")
                button_widget.treeview.column("Aloom", width=75)
                button_widget.treeview.heading("Fan", text="Fan", anchor="w")
                button_widget.treeview.column("Fan", width=75)
                button_widget.treeview.heading("Feezia", text="Feezia", anchor="w")
                button_widget.treeview.column("Feezia", width=75)
                button_widget.treeview.heading("Ayashy", text="Ayashy", anchor="w")

                button_widget.treeview.pack()
                # Insert some data into the Treeview
                button_widget.treeview.insert("", "end", text="1",values=("John Doe", 25, "Manager", "mail@gmail.com", "Male", "055-000000", "Usa"))
                button_widget.treeview.insert("", "end", text="2",values=("Jane Smith", 30, "Doctor", "doc@hotmail.com", "Female", "055-000000", "Pls"))

                # Pack the Treeview widget
                #button_widget.place(x=x, y=y, width=680, height=200)

                x_entry.delete(0, tk.END)
                x_entry.insert(0, event.x)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, event.y)
                height_entry.delete(0, tk.END)
                width_entry.delete(0, tk.END)
                height_entry.insert(0, 200)
                width_entry.insert(0, 680)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                kinds[0] = tool
                buttonlistkey = True
                update_button()
                #callrowwsupdown()
                #print("====in drow button_widget",button_widget.treeview)
                treeviewname.append(button_widget.treeview)
                create_tab2()
                button_click(frames[0])
                #return tool

                entno = 1
                for kj in treeviewlst:
                    entries[f"Col1Entry{entno}"].insert(0, kj)
                    entries[f"Col1Entry{entno}"].configure(state="disabled")
                    entno = entno + 1
                notebook.select(tab2)
                for i in range(1, 22):
                    entries[f"Col1Entry{i}"].configure(state="disabled")

                #=================================
                tool = "Button"
                defult()
                tool = "Button"

                #print ("hello i try to make button",tool)
                f = f"Exit {addlist[0] + 1}"
                treeviewtools.append(f)
                buttonnamenew[0] = f
                button_widget = tk.Button(canvas1, text=f)
                canvas1.create_window(x+608, y-15, window=button_widget)
                button_widget.config(font="Arial 9 bold")
                x_entry.delete(0, tk.END)
                treeviewtools.append(608)
                treeviewtools.append(15)
                x_entry.insert(0, x+608)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y-15)
                text_entry.delete(0,tk.END)
                text_entry.insert(0,f)
                Bd_entry.delete(0, tk.END)
                Bd_entry.insert(0, 1)
                kinds[0] = tool
                # update_arrows(int(x_entry.get()), int(y_entry.get()))
                buttonlistkey = True
                update_button()
                #callrowwsupdown()

                defult()
                tool = "Button"

                #print("hello i try to make button", tool)
                f = f"Refresh {addlist[0] + 1}"
                treeviewtools.append(f)
                buttonnamenew[0] = f
                button_widget = tk.Button(canvas1, text=f)
                canvas1.create_window(x + 535, y - 15, window=button_widget)
                button_widget.config(font="Arial 9 bold")
                x_entry.delete(0, tk.END)
                treeviewtools.append(535)
                treeviewtools.append(15)
                x_entry.insert(0, x + 535)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y - 15)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                Bd_entry.delete(0, tk.END)
                Bd_entry.insert(0, 1)
                kinds[0] = tool
                # update_arrows(int(x_entry.get()), int(y_entry.get()))
                buttonlistkey = True
                update_button()
                # callrowwsupdown()

                defult()
                tool = "Button"
                #print("hello i try to make button", tool)
                f = f"Search {addlist[0] + 1}"
                treeviewtools.append(f)
                buttonnamenew[0] = f
                button_widget = tk.Button(canvas1, text=f)
                canvas1.create_window(x + 462, y - 15, window=button_widget)
                button_widget.config(font="Arial 9 bold")
                x_entry.delete(0, tk.END)
                treeviewtools.append(462)
                treeviewtools.append(15)
                x_entry.insert(0, x + 462)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y - 15)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                Bd_entry.delete(0, tk.END)
                Bd_entry.insert(0, 1)
                kinds[0] = tool
                # update_arrows(int(x_entry.get()), int(y_entry.get()))
                buttonlistkey = True
                update_button()
                # callrowwsupdown()

                defult()
                tool = "Entry"
                f = f"Entry{addlist[0] + 1}"
                buttonnamenew[0] = f
                # canvas1.create_window(x, y, window=tk.Entry(canvas1))
                x, y = event.x, event.y
                f = f"S-Entry {addlist[0] + 1}"
                treeviewtools.append(f)
                button_widget = tk.Entry(canvas1)
                canvas1.create_window(x + 326, y - 15,  window=button_widget)
                button_widget.delete(0, tk.END)
                button_widget.insert(0, f)
                width_entry.delete(0, tk.END)
                width_entry.insert(0, 18)
                Bd_entry.delete(0, tk.END)
                Bd_entry.insert(0, 4)
                x_entry.delete(0, tk.END)
                treeviewtools.append(327)
                treeviewtools.append(14)
                x_entry.insert(0, x + 327)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y - 14)
                Bd_entry.delete(0, tk.END)
                Bd_entry.insert(0, 2)
                kinds[0] = tool
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                buttonlistkey = True
                update_button()
                #callrowwsupdown()
                #==============================================
                defult()
                tool = "OptionMenu"
                f = f"Search By {addlist[0] + 1}"

                buttonnamenew[0] = f
                options = ["Option 1", "Option 2", "Option 3"]
                variable = tk.StringVar(canvas1)
                variable.set(options[0])
                button_widget = tk.OptionMenu(canvas1, variable, *options)
                button_widget.configure(width=10, foreground="white", background="teal")
                button_widget.place(x=x + 215, y=y - 26)
                x_entry.delete(0, tk.END)
                x_entry.insert(0, x + 100)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y + 26)

                width_entry.delete(0, tk.END)
                width_entry.insert(0, 10)
                Bd_entry.delete(0, tk.END)
                Bd_entry.insert(0, 1)
                fg_entry.configure(state="normal")
                bg_entry.configure(state="normal")
                bg_entry.delete(0, tk.END)
                bg_entry.insert(0, 'teal')
                fg_entry.delete(0, tk.END)
                fg_entry.insert(0, 'white')
                bg_entry.configure(state="disabled")
                fg_entry.configure(state="disabled")
                x_entry.delete(0, tk.END)

                x_entry.insert(0, x + 215)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y - 16)
                f = f"OptionM{addlist[0] + 1}"
                treeviewtools.append(f)
                treeviewtools.append(215)
                treeviewtools.append(+16)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                Bd_entry.delete(0, tk.END)
                Bd_entry.insert(0, 1)
                button_widget["menu"].delete("0", "end")
                options = []
                new_option = f
                kinds[0] = tool
                options.append(new_option)
                variable.set(options[0])  # reset the selected value to the first option
                button_widget["menu"].delete(0, "end")  # delete the existing menu items
                for option in options:
                    button_widget["menu"].add_command(label=option, command=tk._setit(variable, option))
                    # print(option,variable)

                    optinmaddss.append(option)
                    optinmaddss.append(variable)
                    optinmaddss.append(button_widget["menu"])
                buttonlistkey = True
                update_button()
                #callrowwsupdown()

                #===========================================
                defult()
                tool = "Button"
                # print("hello i try to make button", tool)
                f = f"Delete {addlist[0] + 1}"
                treeviewtools.append(f)
                buttonnamenew[0] = f
                button_widget = tk.Button(canvas1, text=f)
                canvas1.create_window(x + 144, y - 15, window=button_widget)
                button_widget.config(font="Arial 9 bold")
                x_entry.delete(0, tk.END)
                treeviewtools.append(144)
                treeviewtools.append(15)
                x_entry.insert(0, x + 144)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y - 15)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                Bd_entry.delete(0, tk.END)
                Bd_entry.insert(0, 1)
                kinds[0] = tool
                # update_arrows(int(x_entry.get()), int(y_entry.get()))
                buttonlistkey = True
                update_button()
                # callrowwsupdown()
                defult()
                tool = "Button"
                # print("hello i try to make button", tool)
                f = f"UpDate {addlist[0] + 1}"
                treeviewtools.append(f)
                buttonnamenew[0] = f
                button_widget = tk.Button(canvas1, text=f)
                canvas1.create_window(x + 71, y - 15, window=button_widget)
                button_widget.config(font="Arial 9 bold")
                x_entry.delete(0, tk.END)
                treeviewtools.append(71)
                treeviewtools.append(15)
                x_entry.insert(0, x + 71)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y - 15)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                Bd_entry.delete(0, tk.END)
                Bd_entry.insert(0, 1)
                kinds[0] = tool
                # update_arrows(int(x_entry.get()), int(y_entry.get()))
                buttonlistkey = True
                update_button()
                # callrowwsupdown()
                defult()
                tool = "Button"
                # print("hello i try to make button", tool)
                f = f"Add New  {addlist[0] + 1}"
                treeviewtools.append(f)
                buttonnamenew[0] = f
                button_widget = tk.Button(canvas1, text=f)
                canvas1.create_window(x , y - 15, window=button_widget)
                button_widget.config(font="Arial 9 bold")
                x_entry.delete(0, tk.END)
                treeviewtools.append(0)
                treeviewtools.append(15)
                x_entry.insert(0, x)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y - 15)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                Bd_entry.delete(0, tk.END)
                Bd_entry.insert(0, 1)
                kinds[0] = tool
                # update_arrows(int(x_entry.get()), int(y_entry.get()))
                buttonlistkey = True
                update_button()

                # callrowwsupdown()
                yao=y
                yao=yao-178
                defult()
                for treedrows in treeviewlst:
                    defult()
                    tool = "Label"
                    f = f"{treedrows}"
                    buttonnamenew[0] = f
                    treeviewtools.append(f)
                    treelabels.append(f)


                    # canvas1.create_window(x, y, window=tk.Label(canvas1, text="Label"))
                    button_widget = tk.Label(canvas1, text="Label" ,anchor="w")
                    canvas1.create_window(x+2, yao, window=button_widget)

                    button_widget.config(font=("Arial", 10))
                    width_entry.delete(0, tk.END)
                    width_entry.insert(0, 10)
                    x_entry.delete(0, tk.END)
                    treeviewtools.append(2)
                    treeviewtools.append(y-yao-3)
                    x_entry.insert(0, x+2)
                    y_entry.delete(0, tk.END)
                    y_entry.insert(0, yao)
                    Bd_entry.delete(0, tk.END)
                    Bd_entry.insert(0, 0)
                    text_entry.delete(0, tk.END)
                    text_entry.insert(0, f)
                    kinds[0] = tool
                    buttonlistkey = True
                    update_button()

                    defult()
                    tool = "Entry"
                    f = f"Entry{addlist[0] + 1}"
                    buttonnamenew[0] = f
                    # canvas1.create_window(x, y, window=tk.Entry(canvas1))

                    f = f"Entry_{treedrows}"
                    treeviewtools.append(f)
                    treeEntrys.append(f)


                    button_widget = tk.Entry(canvas1)
                    canvas1.create_window(x+72, yao-1 , window=button_widget)
                    button_widget.delete(0, tk.END)
                    button_widget.insert(0, f)
                    width_entry.delete(0, tk.END)
                    width_entry.insert(0, 18)
                    Bd_entry.delete(0, tk.END)
                    Bd_entry.insert(0, 4)
                    x_entry.delete(0, tk.END)
                    treeviewtools.append(72)
                    treeviewtools.append(y - yao - 1)
                    x_entry.insert(0, x+72 )
                    y_entry.delete(0, tk.END)
                    y_entry.insert(0, yao-1)
                    kinds[0] = tool
                    text_entry.delete(0, tk.END)
                    text_entry.insert(0, f)
                    buttonlistkey = True
                    update_button()
                    yao=yao+22
                # &s--------------------------------------------------------------
                tool = "Scrollbar"
                f = f"Scrollbar{addlist[0] + 1}"
                scrolls.append(f)
                treeviewtools.append(f)
                # buttonnamenew[0] = f
                #print("===", treeviewname)
                #print("--", frames)
                import tkinter
                #print(tkinter.TkVersion)
                button_widget = ttk.Scrollbar(canvas1, orient="horizontal")
                button_widget.place(x=240, y=455, width=682)
                button_widget['command'] = treeviewname[1].xview
                # button_widget.place(x=235, y=300)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                width_entry.delete(0, tk.END)
                width_entry.insert(0, 682)
                height_entry.delete(0, tk.END)
                height_entry.insert(0, 1)
                x_entry.delete(0, tk.END)
                treeviewtools.append(-2)
                treeviewtools.append(-183)
                x_entry.insert(0, x - 2)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y + 183)
                kinds[0] = tool
                buttonlistkey = True
                update_button()
                # return tool
                # ----------------
                # &s--------------------------------------------------------------
                tool = "Scrollbar"
                f = f"Scrollbar{addlist[0] + 1}"
                scrolls.append(f)
                treeviewtools.append(f)
                # buttonnamenew[0] = f
                # print("===", treeviewname)
                # print("--", frames)
                import tkinter
                # print(tkinter.TkVersion)

                button_widget = ttk.Scrollbar(canvas1, orient="vertical")
                button_widget.place(x=902, y=301, height=153)
                button_widget['command'] = treeviewname[1].yview

                # button_widget.place(x=235, y=300)
                text_entry.delete(0, tk.END)
                text_entry.insert(0, f)
                width_entry.delete(0, tk.END)
                width_entry.insert(0, 682)
                height_entry.delete(0, tk.END)
                height_entry.insert(0, 153)
                x_entry.delete(0, tk.END)
                treeviewtools.append(663)
                treeviewtools.append(-34)
                x_entry.insert(0, x + 663)
                y_entry.delete(0, tk.END)
                y_entry.insert(0, y + 34)
                kinds[0] = tool
                buttonlistkey = True
                update_button()


                #print(treeviewtools)
                #print(buttonlst)
                #treeviewname = []
                #treeviewtools = []












# bind the function to the canvas
canvas1.bind("<Button-1>", draw_tool)

# Create entry window

#fnz_entry = tk.Entry(tab1, width=10,bd=3, fg='white', bg=bgbgbg, font=('Arial', 9),cursor='hand2')
#fnz_entry.insert(0, default_config["font size"])
#fnz_entry.place(x=587 + xxv, y=316 + yyv)
#----------------
bgLabel33 = tk.Label(tab1, text='Bg_', fg='white', bg=bgbgbg, font=('Arial', 9), height=1, width=3)
bgLabel33.place(x=494 + xxv, y=343 + yyv)

fgLabel35 = tk.Label(tab1, text='Fg_', fg='white', bg=bgbgbg, font=('Arial',9), height=1, width=3)
fgLabel35.place(x=494 + xxv, y=368 + yyv)

bg_entry = tk.Entry(tab1,bd=3,disabledforeground="white", disabledbackground=bgbgbg, width=9, fg='white', bg=bgbgbg, font=('Arial', 8))
bg_entry.insert(0, default_config["bg"])
bg_entry.place(x=524 + xxv, y=341 + yyv)
bg_entry.configure(state="disabled")

fg_entry = tk.Entry(tab1,bd=3,disabledforeground="white",disabledbackground=bgbgbg, width=9, fg='white', bg=bgbgbg, font=('Arial', 8))
fg_entry.insert(0, default_config["fg"])
fg_entry.place(x=524 + xxv, y=368 + yyv)
fg_entry.configure(state="disabled")
#-----------------------


txtLabel37 = tk.Label(tab1, text='Text', fg='white', bg=bgbgbg, font=('Arial', 9), height=1, width=3)
txtLabel37.place(x=494 + xxv, y=395 + yyv)

text_entry = tk.Entry(tab1,bd=3, width=9, fg='white', bg=bgbgbg, font=('Arial',8),cursor='hand2')
text_entry.insert(0, default_config["text"])
text_entry.place(x=524 + xxv, y=395 + yyv)

widthlabel = tk.Label(tab1, text='Wid_', fg='white', bg=bgbgbg, font=('Arial', 9), height=1, width=3,cursor='hand2')
widthlabel.place(x=497 + xxv, y=420 + yyv)

width_entry = tk.Entry(tab1,bd=3, width=9, fg='white', bg=bgbgbg, font=('Arial',8),cursor='hand2')
width_entry.insert(0, default_config["width"])
width_entry.place(x=524 + xxv, y=420 + yyv)
#width_entry = tk.Entry(entry_framev,width=7, bg='yellow')

height_entryLabel45 = tk.Label(tab1,bd=3, text='Hei_', fg='white', bg=bgbgbg, font=('Arial',9), height=1, width=3,cursor='hand2')
height_entryLabel45.place(x=497 + xxv, y=443 + yyv)

height_entry = tk.Entry(tab1,bd=3, width=9, fg='white', bg=bgbgbg, font=('Arial', 8),cursor='hand2')
height_entry.insert(0, default_config["height"])
height_entry.place(x=524 + xxv, y=443 + yyv)


x_entryLabel51 = tk.Label(tab1,bd=3, text='X-P', fg='white', bg=bgbgbg, font=('Arial', 8), height=1, width=3,cursor='hand2')
x_entryLabel51.place(x=496 + xxv, y=467 + yyv)
x_entry = tk.Entry(tab1,bd=3, width=9, fg='white', bg=bgbgbg, font=('Arial', 8),cursor='hand2')
x_entry.insert(0, 50)
x_entry.place(x=525 + xxv, y=467 + yyv)

y_entryLabel53 = tk.Label(tab1, text='Y-P', fg='white', bg=bgbgbg, font=('Arial', 9), height=1, width=3,cursor='hand2')
y_entryLabel53.place(x=496 + xxv, y=497 + yyv)
y_entry = tk.Entry(tab1,bd=3, width=5, fg='white', bg=bgbgbg, font=('Arial', 8),cursor='hand2')
y_entry.insert(0, 50)
y_entry.place(x=524 + xxv, y=497 + yyv)

Bd_entryLabel53 = tk.Label(tab1, text='Bd_', fg='white', bg=bgbgbg, font=('Arial', 9), height=1, width=3,cursor='hand2')
Bd_entryLabel53.place(x=500 + xxv, y=523 + yyv)

Bd_entry = tk.Entry(tab1,bd=3, width=9, fg='white', bg=bgbgbg, font=('Arial', 8),cursor='hand2')
Bd_entry.insert(0, 2)
Bd_entry.place(x=524 + xxv, y=523 + yyv)



update_button_button = Button(tab1, text='UpDate',bd=3,command=update_button, bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=9,cursor='hand2')
update_button_button.place(x=581 + xxv, y=554 + yyv)
root.buttondelet = Button(tab1, text='Delete',bd=3,command=deleteb, bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=9,cursor='hand2')
root.buttondelet.place(x=495 + xxv, y=554 + yyv)

#entry_window = entry_frame
#===========================================================
#===================================================


# Define some additional colors

#================ to change bg color
Bgcolorlst=['gray']
def update_color3Bg(*args):
    sound()
    selected_color = open_color_dialog()
    Bgcolorlst[0] = colorlst1[0]
    canvashola.configure(background=Bgcolorlst[0],highlightbackground=Bgcolorlst[0])
    labelimg1.configure(background=Bgcolorlst[0],highlightbackground=Bgcolorlst[0])
    #color_square.configure(bg=hex_color)
    bg_entry.configure(state="normal")
    bg_entry.delete(0, tk.END)
    bg_entry.insert(0, Bgcolorlst[0])
    bg_entry.configure(state="disabled")
    if grtmum[0] != 0:
        update_button_button.invoke()
fgcolorlst=['gray']
def update_color1Fg(*args):
    sound()
    selected_color = open_color_dialog()
    fgcolorlst[0] = colorlst1[0]
    fg_entry.configure(state="normal")
    fg_entry.delete(0, tk.END)
    fg_entry.insert(0, fgcolorlst[0])
    fg_entry.configure(state="disabled")
    if grtmum[0] !=0:
         update_button_button.invoke()
# Create a frame to hold the combobox and color display

Bgcolorbtn = tk.Button(tab1,width=8,height=1,background=bgbgbg, foreground='white',cursor='hand2', text='Bg Color',bd=3, command=update_color3Bg,font=('Arial ',10))
Bgcolorbtn.place(x=590 + xxv, y=338 + yyv)

Fgcolorbtn = tk.Button(tab1,width=8,height=1,background=bgbgbg, foreground='white',cursor='hand2', text='Fg Color',bd=3, command=update_color1Fg,font=('Arial ',10))
Fgcolorbtn.place(x=590 + xxv, y=365 + yyv)


# Create the color square labels
# Pack the widgets into the frame
# Call the update_color function to set the initial color square color
#update_color3()
#====================

def make_widgets_invisible():
    #text_label7u.place_forget()

    comboboxw.place_forget()

#make_widgets_invisible()
def make_widgets_visible():
    #text_label7u.place(x=484 + xz, y=135 + yz)

    comboboxw.place(x=479 + xz, y=172 + yz, anchor="center")

#====================================================
def create_buttons11(buttonlst):
    if treeviewname[0] == "":
            xxv = 0
            yyv = 0
            xxxg = int(((((1360 - 1146) + int(mainprogscr[2])) - 1360) / 2)-3)
            yyyg = int(((((768 - 659) + int(mainprogscr[3])) - 768) / 2)-4)
            #print("xx:",xxxg,"yy:",yyyg)
            #print(buttonlst)
            #print("======hello==============")
            global textallbutton
#&2
            butoomlsttext=["import tkinter as tk\nfrom tkinter import *\nfrom tkinter import ttk\nimport tkinter as tk\nimport tkinter.font as tkFont\n" \
                   "import datetime\nimport time\nimport pygame\nfrom datetime import datetime\nimport re\nimport requests\nimport tkinter.scrolledtext as ScrolledText\n" \
                   f"from tkinter import messagebox\nimport webcolors\nimport sqlite3\nfrom PIL import Image, ImageTk\nfrom tkinter import scrolledtext\nroot=Tk()\nxxv={xxxg}\nyyv={yyyg}\n" ]
            butoomlsttext.append(f"\nroot.title('{roottietl.get()}')\nroot.geometry('{int(rootmx.get())+3}x{int(rootmy.get())+3}')\n"\
                    f"root.configure(bg='{rootcolor.get()}')\nroot.option_add('*Font', '{rootfont.get()} 9' )\n"\
                    f"screen_width = root.winfo_screenwidth()\nscreen_height = root.winfo_screenheight()\nx = (screen_width - {rootmx.get()})//2\n"\
                    f"y = (screen_height - {rootmy.get()})//2\nroot.maxsize({rootmx.get()},{rootmy.get()})\nroot.minsize({int(rootmx.get())+3},{int(rootmy.get())+3})\nroot.geometry(\"+{{}}+{{}}\".format(x, y))"
        )
            butoomlsttext.append(f"\ndef hello():\n\t\tprint('Hello, world!')\nbg_color = '{rootcolor.get()}'\nfg_color = 'white'\nactive_bg_color = 'lightgray'\nactive_fg_color = 'blue'\nmenu = Menu(root, bg=bg_color, fg=fg_color, activebackground=active_bg_color, activeforeground=active_fg_color)\n" \
                "\nroot.config(menu=menu)\nfile_menu = Menu(menu, tearoff=0, bg=bg_color, fg=fg_color, activebackground=active_bg_color, activeforeground=active_fg_color)\nfile_menu.add_command(label='Open', command=hello)\nfile_menu.add_separator()\nfile_menu.add_command(label='Exit', command=root.quit)\n" \
                "\nhelp_menu = Menu(menu, tearoff=0, bg=bg_color, fg=fg_color, activebackground=active_bg_color, activeforeground=active_fg_color)\nhelp_menu.add_command(label='Test', command=hello)\nmenu.add_cascade(label='File', menu=file_menu)\nmenu.add_cascade(label='Help', menu=help_menu)\n")
            butoomlsttext.append(f"\nvar = tk.BooleanVar()\n")
            butoomlsttext.append(f"\nvaluescombo = ['Option 1', 'Option 2', 'Option 3']")
    if treeviewname[0] != "":
        print(treeviewname)
        butoomlsttext=[]
        butoomlsttext.append("import tkinter as tk\nfrom tkinter import ttk\nfrom tkinter import messagebox\nimport sqlite3\nimport pygame\nimport os\npygame.mixer.init()\ncurrent_dir = os.getcwd()\nsound_file_path = os.path.join(current_dir, 'click1.wav')\nmy_sound = pygame.mixer.Sound(sound_file_path)\nxxv = -3\nyyv = -4\n")

        # buttonf = f"button{str(button_num)}"
        butooncreat1 = f"\nclass Database:\n\tdef __init__(self, db):\n\t\tself.con = sqlite3.connect(db)\n\t\tself.cur = self.con.cursor()\n\t\tsql = \"\"\"\n\t\t\tCREATE TABLE IF NOT EXISTS employees (\n" \
                       f"\t\t\t\tid INTEGER PRIMARY KEY,\n"

        str1 = ""
        str3 = ""
        alltxtputnow=""
        nameslst1=""
        acherlst=""
        qustionmark=""
        last_item = treeviewlst[-1]
        for tsql in treeviewlst:
            qas=f", ?"
            qustionmark+=qas
            #print(qustionmark)
            if last_item != tsql:
                butooncreat = f"\t\t\t\t{tsql} TEXT,\n"
                str1 += butooncreat
            else:
                butooncreat = f"\t\t\t\t{tsql} TEXT\n"
                str1 += butooncreat

            str2=f"{tsql}=?,"
            str3 += str2
            txtputnow=f"\tPlaceholderEntry.put_placeholder(self.{tsql}_entry)\n"
            alltxtputnow+=txtputnow
            nams=f"\"{tsql}\","
            nameslst1 += nams
            achr=f"\n\t\t\tself.treeview.heading(\"{tsql}\", text=\"{tsql}\", anchor=\"w\")\n\t\t\tself.treeview.column(\"{tsql}\", width=75)"
            acherlst += achr
        nameslst1=nameslst1[:-1]
        #print(acherlst)
        str3 = str3[:-1]
        butooncreat2 = str1

        butooncreat3 = f"\t\t\t)\n\t\t\"\"\"\n\t\tself.cur.execute(sql)\n" \
                       f"\t\tself.con.commit()\n"
        result = ", ".join(treeviewlst)
        butooncreat4 = f"\tdef insert(self,{result}):" \
                       f"\n\t\tself.cur.execute(\"INSERT INTO employees VALUES (NULL{qustionmark})\",\n" \
                       f"\t\t\t\t\t({result}))\n\t\tself.con.commit()\n"
        butooncreat5=f"\n\tdef fetch(self):\n\t\tself.cur.execute(\"SELECT * FROM employees\")\n"\
                     f"\t\trows = self.cur.fetchall()\n\t\treturn rows\n"\
                     f"\tdef remove(self, id):\n\t\tself.cur.execute(\"DELETE FROM employees WHERE id=?\", (id,))\n"\
                     f"\t\tself.con.commit()\n"\
                     f"\tdef update(self, id,{result}):\n"\
                     f"\t\tself.cur.execute(\"UPDATE employees SET {str3}WHERE id=?\",\n"\
                     f"\t\t\t\t\t\t({result}, id))\n\t\tself.con.commit()\n"
        nmnm=""
        for index, tsql in enumerate(treeviewlst):
            if index != 0:
                tsgls = f"\t\telif field == \"{tsql}\":\n\t\t\tquery = f\"SELECT * FROM employees WHERE {tsql} LIKE '%{{term}}%'\"\n"
            else:
                tsgls = f"\t\tif field == \"{tsql}\":\n\t\t\tquery = f\"SELECT * FROM employees WHERE {tsql} LIKE '%{{term}}%'\"\n"
            nmnm += tsgls

        #print(nmnm)

        butooncreat6=f"\tdef search(self, field, term):\n"\
                     f"\n{nmnm}\n\t\telse:\n\t\t\treturn []\n\t\tself.cur.execute(query)\n"\
                     f"\t\trows = self.cur.fetchall()\n\t\treturn rows\n"

        butooncreat7=f"class PlaceholderEntry(tk.Entry):\n\tdef __init__(self, db):\n\t\tsuper().__init__()\n\t\tself.db = db\n\t\txxx=0\n\t\tyyy=0\n"
        labtxt1=""
        canv = ""
        #print(buttonlst)
        for lab in treelabels:
            selected_item1 = lab
            if selected_item1 in buttonlst:
                index = buttonlst.index(selected_item1)
                x=buttonlst[index-4]
                y=buttonlst[index-3]
                labtxt=buttonlst[index]
                fg=buttonlst[index+1]
                bg=buttonlst[index+2]
                height=buttonlst[index-2]
                width=buttonlst[index-1]
                bd=buttonlst[index+6]
                #print(selected_item1,x,y," text ",labtxt,bg,fg,height,width)
                butooncreatx=f"\n\t\t\tself.{lab}_label=tk.Label(self,text='{labtxt}',bg='{bg}',fg='{fg}',relief=\"ridge\",borderwidth={bd},width={width},height={height},anchor=\"w\")\n"\
                             f"\t\t\tself.{lab}_label.place(x={x}+xxx,y={y}+yyy)\n"
                #print(butooncreatx)
                labtxt1 += butooncreatx
        #=======================================================================
        Enttxt1 = ""
        # print(buttonlst)
        alldefclear=""
        defclerdel=""
        for indexEnt, Ent in enumerate(treeEntrys):

            selected_item1 = Ent
            if selected_item1 in buttonlst:
                #print(treelabels[indexEnt],"---",Ent)
                index = buttonlst.index(selected_item1)
                #print(index)
                #print(treelabels[index])
                x = buttonlst[index - 4]
                y = buttonlst[index - 3]
                Enttxt = buttonlst[index]
                fg = buttonlst[index + 1]
                bg = buttonlst[index + 2]
                height = buttonlst[index - 2]
                width = buttonlst[index - 1]
                bd = buttonlst[index + 6]
                # print(selected_item1,x,y," text ",labtxt,bg,fg,height,width)

                butooncreate = f"\n\t\t\tself.{treelabels[indexEnt]}_entry=PlaceholderEntry(self,placeholder=\"{treelabels[indexEnt]}\")\n"\
                               f"\n\t\t\tself.{treelabels[indexEnt]}_entry.configure(background='{bg}',foreground='{fg}',relief=\"ridge\",borderwidth={bd},width={width})\n"\
                               f"\t\t\tself.{treelabels[indexEnt]}_entry.place(x={x}+xxx,y={y}+yyy)\n"
                # print(butooncreatx)
                Enttxt1 += butooncreate
                dfclearen=f"\n\t\tself.{treelabels[indexEnt]}_entry.remove_placeholder()"
                alldefclear +=dfclearen
                dfcldel=f"\n\t\tself.{treelabels[indexEnt]}_entry.delete(0, tk.END)"
                defclerdel+=dfcldel
        treepl=""
        xnew=0
        ynew=0
        widthnew=0
        selected_item1 = treeviewname[0]
        if selected_item1 in buttonlst:
            index = buttonlst.index(selected_item1)
            x = buttonlst[index - 4]
            xnew=x
            y = buttonlst[index - 3]
            ynew=y
            Enttxt = buttonlst[index]
            fg = buttonlst[index + 1]
            bg = buttonlst[index + 2]
            height = buttonlst[index - 2]
            width = buttonlst[index - 1]
            widthnew=width
            bd = buttonlst[index + 6]
#&8
            treepl=f"\n\t\t\txox={x}\n\t\t\tyoy={y}\n\t\t\thhh={height}\n\t\t\twww={width}\n"
            #print(height,width)
        #print(Enttxt1)
        #=========================================================================
        #print(labtxt)
        butooncreat7=labtxt1

        butooncreat8=f"class PlaceholderEntry(tk.Entry):\n\tdef __init__(self, master=None, placeholder=\"\"):\n\t\tsuper().__init__(master)\n"\
                     f"\n\t\tself.placeholder = placeholder\n\t\tself.placeholder_color = \"gray\"\n\t\tself.default_color = self[\"fg\"]\n"\
                     f"\n\t\tself.bind(\"<FocusIn>\", self.on_entry_focus_in)\n\t\tself.bind(\"<FocusOut>\", self.on_entry_focus_out)\n"\
                     f"\t\tself.put_placeholder()\n"\
                     f"\tdef put_placeholder(self):\n\t\tself.insert(0, self.placeholder)\n\t\tself[\"fg\"] = self.placeholder_color\n"\
                     f"\tdef remove_placeholder(self):\n\t\tself.delete(0, tk.END)\n\t\tself[\"fg\"] = self.default_color\n"\
                     f"\tdef on_entry_focus_in(self, event):\n\t\tif self[\"fg\"] == self.placeholder_color:\n\t\t\tself.delete(0, tk.END)\n\t\t\tself[\"fg\"] = self.default_color\n"\
                     f"\n\tdef on_entry_focus_out(self, event):\n\t\tif not self.get():\n\t\t\tself.put_placeholder()\n"\
                     f"\ndef putnow(self):\n{alltxtputnow}\nidlist=[0]\nxxx=0\nyyy=0\n"\
                     f"class Application(tk.Tk):\n\tdef __init__(self, db):\n\t\t\tsuper().__init__()\n\t\t\tself.db = db\n\t\t\tpygame.mixer.init()\n"
        selected_item1 = frames[0]
        if selected_item1 in buttonlst:
            index = buttonlst.index(selected_item1)
            x = buttonlst[index - 4]
            xnew = x
            y = buttonlst[index - 3]
            ynew = y
            Enttxt = buttonlst[index]
            fg = buttonlst[index + 1]
            bg = buttonlst[index + 2]
            height = buttonlst[index - 2]
            width = buttonlst[index - 1]
            widthnew = width
            bd = buttonlst[index + 6]
        #&0
        butooncreat9=f"\n\t\t\tstyle = ttk.Style()\n\t\t\tstyle.configure(\"Custom.Treeview\", rowheight=17, font=(\"Arial\", 9), borderwidth=2, relief=\"ridge\",foreground=\"Black\", background=\"teal\")\n"\
                     f"\n\t\t\tframe = tk.Frame(self, width={width-4}, height={height})\n"\
                     f"\n\t\t\tframe.place(x={x}+xxx,y={y}+yyy)"\
                     f"\n\t\t\tframe.pack_propagate(0)\n"\
                     f""\
                     f"\t\t\tself.treeview = ttk.Treeview(frame, columns=({nameslst1}),style=\"Custom.Treeview\",cursor=\"hand2\",height=10)\n"\
                     f"\t\t\tself.treeview.heading(\"#0\", text=\"ID\", anchor=\"center\")\n\t\t\tself.treeview.column(\"#0\", width=50)\n"\
                     f"{acherlst}{treepl}\n\t\t\tself.treeview.pack()\n"

        #&5
        #print("*****",scrolls)
        selected_item1 = scrolls[1]
        if selected_item1 in buttonlst:
            index = buttonlst.index(selected_item1)
            x = buttonlst[index - 4]
            xnew = x
            y = buttonlst[index - 3]
            ynew = y
            Enttxt = buttonlst[index]
            fg = buttonlst[index + 1]
            bg = buttonlst[index + 2]
            height = buttonlst[index - 2]
            width = buttonlst[index - 1]
            widthnew = width
            bd = buttonlst[index + 6]

        Scrools = f"\t\t\tvscrollbar = ttk.Scrollbar(self, orient=\"vertical\", command=self.treeview.yview)\n" \
                  f"\t\t\tvscrollbar.place(x={x}+xxx, y={y-5}+yyy, height={height+1})\n" \
                  f"\t\t\tself.treeview.configure(yscrollcommand=vscrollbar.set)\n" \
                  f"\t\t\tself.treeview.bind(\"<<TreeviewSelect>>\", self.on_data_sheet_selection)\n"

        selected_item1 = scrolls[0]
        if selected_item1 in buttonlst:
            index = buttonlst.index(selected_item1)
            x = buttonlst[index - 4]
            xnew = x
            y = buttonlst[index - 3]
            ynew = y
            Enttxt = buttonlst[index]
            fg = buttonlst[index + 1]
            bg = buttonlst[index + 2]
            height = buttonlst[index - 2]
            width = buttonlst[index - 1]
            widthnew = width
            bd = buttonlst[index + 6]
        scrollh=f"\n\t\t\thscrollbar = ttk.Scrollbar(self, orient=\"horizontal\", command=self.treeview.xview)"\
                f"\n\t\t\thscrollbar.place(x={x}+xxx, y={y}+yyy, width={width})"\
                f"\n\t\t\tself.treeview.configure(xscrollcommand=hscrollbar.set)"

        #print(treeviewtools)
        #print(treeEntrys)
        #print(treelabels)
        # حذف الليبلز من لست الادوات
        new_list1 = []
        new_list4=[]
        index = 0
        while index < len(treeviewtools):
            item = treeviewtools[index]
            if item in treelabels:
                index += 3
            else:
                new_list1.append(item)
                index += 1
        #print(new_list1)
        # حذف الانتري من لست الادوات
        new_list2 = []
        index = 0
        while index < len(new_list1):
            item = new_list1[index]
            if item in treeEntrys:
                index += 3
            else:
                new_list2.append(item)
                index += 1

        # ازاله قيمة اكس و واي من اللست
        new_list3 = []
        for i in range(0, len(new_list2), 3):
            new_list3.append(new_list2[i])

        #ازاله الفراغات من الاسماء التي في اللست
        new_list4 = [item.replace(' ', '') for item in new_list3]

        #print(new_list4)
        #print(new_list3)
        #print(new_list2)
        #print(buttonlst)
        #-------------------------------------------

        btns=""
        Ent1=""
        menu=""
        for BtmEnOp in new_list3:
            selected_item1 = BtmEnOp
            if selected_item1 in buttonlst:
                index = buttonlst.index(selected_item1)
                x = buttonlst[index - 4]
                y = buttonlst[index - 3]
                Enttxt = buttonlst[index]
                fg = buttonlst[index + 1]
                bg = buttonlst[index + 2]
                height = buttonlst[index - 2]
                width = buttonlst[index - 1]
                bd = buttonlst[index + 6]
                btmkind=buttonlst[index + 5]
                txtn=Enttxt.replace(" ", "")
                new_text = txtn.rstrip('0123456789').strip()
                #&p
                #print(new_text)
                if btmkind=="Canvas":
                    can1=f"\n\t\t\tself.{txtn}=tk.Canvas(self,width={width},height={height})\n\t\t\tself.{txtn}.configure(borderwidth={bd},relief=\"ridge\",background='{bg}')"\
                         f"\n\t\t\tself.{txtn}.create_text(0, 0, text='',fill='{fg}')"\
                         f"\n\t\t\tself.{txtn}.itemconfigure(tk.ALL, fill='{fg}')"\
                         f"\n\t\t\tself.{txtn}.place(x={x}+xxx,y={y}+yyy)\n"
                    canv +=can1
                elif btmkind=="Button":
                     if new_text=="AddNew":
                         btn=f"\n\t\t\tself.{txtn}=tk.Button(self,text='{new_text}',command=self.insert_employee,cursor=\"hand2\",bg='{bg}',fg='{fg}',relief=\"ridge\",bd={bd},width={width},height={height})\n"\
                             f"\t\t\tself.{txtn}.place(x={x}+xxx,y={y}+yyy)\n"
                         btns +=btn
                     elif new_text == "UpDate":
                         btn = f"\n\t\t\tself.{txtn}=tk.Button(self,text='{new_text}',command=self.update_employee,cursor=\"hand2\",bg='{bg}',fg='{fg}',relief=\"ridge\",bd={bd},width={width},height={height})\n"\
                               f"\t\t\tself.{txtn}.place(x={x}+xxx,y={y}+yyy)\n"
                         btns += btn
                     elif new_text == "Delete":
                         btn = f"\n\t\t\tself.{txtn}=tk.Button(self,text='{new_text}',command=self.delete_employee,cursor=\"hand2\",bg='{bg}',fg='{fg}',relief=\"ridge\",bd={bd},width={width},height={height})\n"\
                               f"\t\t\tself.{txtn}.place(x={x}+xxx,y={y}+yyy)\n"
                         btns += btn
                     elif new_text == "Search":
                         btn = f"\n\t\t\tself.{txtn}=tk.Button(self,text='{new_text}',command=self.search_employee,cursor=\"hand2\",bg='{bg}',fg='{fg}',relief=\"ridge\",bd={bd},width={width},height={height})\n"\
                               f"\t\t\tself.{txtn}.place(x={x}+xxx,y={y}+yyy)\n"
                         btns += btn
                     elif new_text == "Refresh":
                         btn = f"\n\t\t\tself.{txtn}=tk.Button(self,text='{new_text}',command=self.show_data,cursor=\"hand2\",bg='{bg}',fg='{fg}',relief=\"ridge\",bd={bd},width={width},height={height})\n"\
                               f"\t\t\tself.{txtn}.place(x={x}+xxx,y={y}+yyy)\n"
                         btns += btn
                     elif new_text == "Exit":
                         btn = f"\n\t\t\tself.{txtn}=tk.Button(self,text='{new_text}',command=self.exit_program,cursor=\"hand2\",bg='{bg}',fg='{fg}',relief=\"ridge\",bd={bd},width={width},height={height})\n"\
                               f"\t\t\tself.{txtn}.place(x={x}+xxx,y={y}+yyy)\n"
                         btns += btn
                elif btmkind == "Entry":
                         Ent1=f"\n\t\t\tself.search_entry=tk.Entry(self,background='{bg}',foreground='{fg}',relief=\"ridge\",borderwidth={bd},width={width})\n"\
                              f"\t\t\tself.search_entry.place(x={x}+xxx,y={y}+yyy)\n"
                elif btmkind == "OptionMenu":
                    menu = f"\n\t\t\tfields = [{nameslst1}]\n"\
                           f"\t\t\tself.search_field = tk.StringVar()\n"\
                           f"\t\t\tself.search_field.set(fields[0])\n"\
                           f"\t\t\tsearch_field_menu = tk.OptionMenu(self, self.search_field, *fields)\n"\
                           f"\t\t\tsearch_field_menu.configure(background='teal', foreground='white', relief='ridge', borderwidth=1, width=10)\n"\
                           f"\t\t\tsearch_field_menu.place(x={x}+xxx, y={y}+yyy)\n"\
                           f"\t\t\tself.show_data()\n"\
                           f"\t\t\tself.clear_entries()\n"\
                           f"\t\t\tputnow(self)\n"\
                           f"\t\t\tself.mainloop()\n"\
                           f"\t\tdef sound(self):\n"\
                           f"\t\t\tmy_sound = pygame.mixer.Sound(sound_file_path)\n"\
                           f"\t\t\tmy_sound.play()\n"\
                           f"\t\tdef exit_program(self):\n"\
                           f"\t\t\tself.destroy()\n"
                    #&h

        defondata = f"\n\tdef on_data_sheet_selection(self, event):\n\t\tself.sound()\n\t\ttry:\n\t\t\tselected_item = self.treeview.focus()\n\n\t\t\tif selected_item:\n"\
                    f"\t\t\t\t\tvalues = self.treeview.item(selected_item)['values']\n\t\t\t\t\tid_value = self.treeview.item(selected_item)['text']\n\t\t\t\t\tidlist[0]=id_value\n"
        defondats=""
        deldef=""
        insdef=""
        tktko=0
        insertnew=""
        ornots=""
        newro=""
        new_ro=""
        for tsqls in treeviewlst:
            defs=f"\t\t\t\t\tself.{tsqls}_entry.remove_placeholder()\n"
            defondats+=defs
            deld=f"\t\t\t\t\tself.{tsqls}_entry.delete(0, tk.END)\n"
            deldef +=deld
            insrd=f"\t\t\t\t\tself.{tsqls}_entry.insert(0, values[{tktko}])\n"
            insdef +=insrd
            tktko+=1
            instn=f"\n\t\tnew_{tsqls} = self.{tsqls}_entry.get().strip()\n"
            insertnew +=instn
            ornot=f" new_{tsqls} or not"
            ornots+=ornot
            parts = ornots.rsplit(" or not", 1)
            new_string = parts[0] + parts[1]
            newr=f" new_{tsqls},"
            newro+=newr
            new_ro = newro.rstrip(",")
        exopts = f"\n\t\texcept Exception as e:\n\t\t\tpass\n"
        defshodta = f"\tdef show_data(self):\n\t\tself.sound()\n\t\tself.treeview.delete(*self.treeview.get_children())\n\t\trows = self.db.fetch()\n\t\tfor row in rows:\n\t\t\tself.treeview.insert('', tk.END, text=row[0], values=row[1:])\n"
        defdisply = f"\tdef display_employee_data(self, rows):\n\t\tself.treeview.insert('', tk.END, text=rows[0], values=rows[1:], anchor='w')\n\t\tself.treeview.heading('#0', text='ID', anchor='e')\n\t\tself.treeview.delete(*self.treeview.get_children())\n\t\tfor row in rows:\n\t\t\tself.treeview.insert('', tk.END, text=row[0], values=row[1:])\n\n"
        defemp = f"\tdef insert_employee(self):\n\t\tself.sound()\n{insertnew}\n\t\tif not {new_string}:\n\t\t\tmessagebox.showwarning('Incomplete Data', 'Please fill in all fields.')\n\t\t\treturn\t\n"
        defcont = f"\n\t\tself.db.insert({new_ro})\n\t\tself.show_data()\n\t\tself.clear_entries()\n\t\tputnow(self)\n"

        defupdatef=f"\n\tdef update_employee(self):\n\t\tself.sound()\n\t\tselected_item = self.treeview.focus()\n\t\tif not selected_item:\n\t\t\tmessagebox.showinfo(\"No Selection\", \"Please select a row to update.\")\n\t\t\treturn"\
                  f"\n\t\tvalues = self.treeview.item(selected_item)['values']\n\t\tif idlist[0] == 0:\n\t\t\tmessagebox.showwarning(\"Invalid Selection\", \"Please select a valid row to update.\")\n\t\t\treturn"\
                  f"\n\t\tid = idlist[0]\n{insertnew}"\
                  f"\n\t\tif not {new_string} :\n\t\t\tmessagebox.showwarning(\"Incomplete Data\", \"Please fill in all fields.\")\n\t\t\treturn"\
                  f"\n\t\tself.db.update(id,{new_ro})\n\t\tself.show_data()\n\t\tself.clear_entries()\n\t\tputnow(self)\n"

        defdeleteemp=f"\n\tdef delete_employee(self):\n\t\tself.sound()\n\t\tselected_item = self.treeview.focus()\n\t\tif not selected_item:\n\t\t\tmessagebox.showinfo(\"No Selection\", \"Please select a row to delete.\")\n\t\t\treturn\n"\
                     f"\n\t\tvalues = self.treeview.item(selected_item)['values']\n\t\tif not values:\n\t\t\tmessagebox.showwarning(\"Invalid Selection\", \"Please select a valid row to delete.\")\n\t\t\treturn\n\t\tid = idlist[0]\n"\
                     f"\n\t\tresult = messagebox.askyesno(\"Confirm Deletion\", \"Are you sure you want to delete this record?\")\n\t\tif result:\n\t\t\tself.db.remove(id)\n\t\t\tself.show_data()\n\t\t\tself.clear_entries()\n\t\t\tputnow(self)\n"

        defserchemp="\n\tdef search_employee(self):\n\t\tself.sound()\n\t\tterm = self.search_entry.get().strip()\n\t\tfield = self.search_field.get()\n\n\t\tif term:\n\t\t\trows = self.db.search(field, term)\n\t\t\tself.treeview.delete(*self.treeview.get_children())\n\t\t\tfor row in rows:\n\t\t\t\tself.treeview.insert(\"\", tk.END, text=row[0], values=row[1:])\n\t\telse:\n\t\t\tself.show_data()\n"

        defclerent=f"\tdef clear_entries(self):\n{alldefclear}\n{defclerdel}"
    # &1
        mainwind=f"\n\t\t\tself.title('{roottietl.get()}')\n\t\t\tself.geometry('{int(rootmx.get())+3}x{int(rootmy.get())+3}')\n"\
                 f"\t\t\tself.configure(bg='{rootcolor.get()}')\n\t\t\tself.option_add('*Font', 'Arial 9')\n"\
                 f"\t\t\tscreen_width = self.winfo_screenwidth()\n"\
                 f"\t\t\tscreen_height = self.winfo_screenheight()\n\t\t\tx = (screen_width - {rootmx.get()})//2\n"\
                 f"\t\t\ty = (screen_height - {rootmy.get()})//2\n\t\t\tself.maxsize({rootmx.get()},{rootmy.get()})\n\t\t\tself.minsize({int(rootmx.get())+3},{int(rootmy.get())+3})\n\t\t\tself.geometry(\"+{{}}+{{}}\".format(x, y))\n"
        menufiles = (
            f"\t\t\tdef hello():\n"
            f"\t\t\tprint('Hello, world!')\n\n"
            f"\n\t\t\tmenu = tk.Menu(self)\n"
            f"\t\t\tself.config(menu=menu)\n"
            f"\t\t\tfile_menu = tk.Menu(menu, tearoff=0)\n"
            f"\t\t\tfile_menu.add_command(label='Open', command=hello)\n"
            f"\t\t\tfile_menu.add_separator()\n"
            f"\t\t\tfile_menu.add_command(label='Exit', command=self.quit)\n"
            f"\t\t\thelp_menu = tk.Menu(menu, tearoff=0)\n"
            f"\t\t\thelp_menu.add_command(label='Test', command=hello)\n"
            f"\t\t\tmenu.add_cascade(label='File', menu=file_menu)\n"
            f"\t\t\tmenu.add_cascade(label='Help', menu=help_menu)\n"
            f"\t\t\txxx = -3\n"
            f"\t\t\tyyy = -4\n"
        )
        #&w
        print(buttonlst)
        #print(treeviewtools)
        new_list3=treeviewtools
        #print("---3658---buttonlst",buttonlst)
        new_list3.append(treeviewname[0])
        new_list3.append(1)
        new_list3.append(2)
        menus=""
        #print("---3658---new_list3", new_list3)
        #------ لبرمجه باقي الادوات مع سكيول وتنقيه الغير موجودفي تري توولز للاضافه الجديد-----
        for i in range(0, len(buttonlst), 13):
            selected_item1 = buttonlst[i + 6]

            #print(buttonlst[i + 6])
            if selected_item1 in new_list3:
                continue
                index = buttonlst.index(selected_item1)
            else:
                index = buttonlst.index(selected_item1)
                x = buttonlst[index - 4]
                y = buttonlst[index - 3]
                Enttxt = buttonlst[index].strip()
                fg = buttonlst[index + 1]
                bg = buttonlst[index + 2]
                height = buttonlst[index - 2]
                width = buttonlst[index - 1]
                bd = buttonlst[index + 6]
                font=buttonlst[index + 3]
                txtn = Enttxt.replace(" ", "")
                new_text = txtn.rstrip('0123456789').strip()

                #print("no no no")
                #print(selected_item1, "---",buttonlst[i + 11] )
                if buttonlst[i + 11] =="Button":
                    #print("ohhh its buttton")
                    #btns
                    btn = f"\n\t\t\tself.{txtn}=tk.Button(self,text='{new_text}',command=hello,cursor=\"hand2\",bg='{bg}',fg='{fg}',relief=\"ridge\",bd={bd},width={width},height={height},font='{font}')\n" \
                          f"\t\t\tself.{txtn}.place(x={x}+xxx,y={y}+yyy)\n"
                    #print(btn)
                    btns+=btn
                    #print(btns)
                elif buttonlst[i + 11] =="Canvas":
                    can1 = f"\n\t\t\tself.{Enttxt}=tk.Canvas(self,width={width},height={height})\n\t\t\tself.{txtn}.configure(borderwidth={bd},relief=\"ridge\",background='{bg}')" \
                           f"\n\t\t\tself.{Enttxt}.create_text(0, 0, text='',fill='{fg}')" \
                           f"\n\t\t\tself.{Enttxt}.itemconfigure(tk.ALL, fill='{fg}')" \
                           f"\n\t\t\tself.{Enttxt}.place(x={x}+xxx,y={y}+yyy)\n"
                    #print(can1)
                    canv += can1
                    #print(canv)
                elif buttonlst[i + 11] == "OptionMenu":
                    menu1 =f"\n\t\t\tfields = ['{txtn}']\n"\
                           f"\t\t\tself.search_field = tk.StringVar()\n"\
                           f"\t\t\tself.search_field.set(fields[0])\n"\
                           f"\t\t\tsearch_field_menu = tk.OptionMenu(self, self.search_field, *fields)\n"\
                           f"\t\t\tsearch_field_menu.configure(background='{bg}', foreground='{fg}', relief='ridge', borderwidth={bd}, width={width},font='{font}')\n"\
                           f"\t\t\tsearch_field_menu.place(x={x}+xxx, y={y}+yyy)\n"
                    canv+=menu1
                    #print(canv)
                elif buttonlst[i + 11] =="Label":
                    #print("ohhh its buttton")
                    #btns
                    btn = f"\n\t\t\tself.{txtn}=tk.Label(self,text='{new_text}',cursor=\"hand2\",bg='{bg}',fg='{fg}',relief=\"ridge\",bd={bd},width={width},height={height},anchor=\"w\",font='{font}')\n" \
                          f"\t\t\tself.{txtn}.place(x={x}+xxx,y={y}+yyy)\n"
                    #print(btn)
                    btns+=btn
                elif buttonlst[i + 11] =="Checkbutton":
                    #print("ohhh its buttton")
                    #btns
                    btn = f"\n\t\t\tself.{txtn}=tk.Checkbutton(self,text='{new_text}',cursor=\"hand2\",bg='{bg}',fg='{fg}',relief=\"ridge\",bd={bd},width={width},height={height},anchor=\"w\",font='{font}')\n" \
                          f"\t\t\tself.{txtn}.place(x={x}+xxx,y={y}+yyy)\n"
                    #print(btn)
                    btns+=btn
                elif buttonlst[i + 11] =="Entry":
                    #print("ohhh its buttton")
                    #btns
                    btn = f"\n\t\t\tself.{txtn}=tk.Entry(self,cursor=\"hand2\",bg='{bg}',fg='{fg}',relief=\"ridge\",bd={bd},width={width},font='{font}')\n" \
                          f"\n\t\t\tself.{txtn}.insert(0,'{txtn}')\n"\
                          f"\t\t\tself.{txtn}.place(x={x}+xxx,y={y}+yyy)\n"
                    #print(btn)
                    btns+=btn
                elif buttonlst[i + 11] =="Listbox":
                    #print("ohhh its buttton")
                    #btns
                    btn = f"\n\t\t\tself.{txtn}=tk.Listbox(self,cursor=\"hand2\",bg='{bg}',fg='{fg}',relief=\"ridge\",bd={bd},width={width},height={height},font='{font}')\n" \
                          f"\n\t\t\tself.{txtn}.insert(tk.END, '{txtn}')\n"\
                          f"\t\t\tself.{txtn}.place(x={x}+xxx,y={y}+yyy)\n"
                    #print(btn)
                    btns+=btn





        # print("==",butooncreat)
        final_string = butooncreat1 + butooncreat2 + butooncreat3 + butooncreat4 +butooncreat5+butooncreat6+butooncreat8+mainwind+menufiles+canv+butooncreat7+Enttxt1+butooncreat9+Scrools+scrollh+btns+Ent1\
                       +menu+defondata+defondats+deldef+insdef+exopts+defshodta+defdisply+defemp+defcont+defupdatef+defdeleteemp+defserchemp+defclerent



        butoomlsttext.append(final_string)

    #text=f"\ndef hello():\n\t\tprint('Hello, world!')\nbg_color = '{entry_list[3].get()}'\nfg_color = 'white'\nactive_bg_color = 'lightgray'\nactive_fg_color = 'blue'\nmenu = Menu(root, bg=bg_color, fg=fg_color, activebackground=active_bg_color, activeforeground=active_fg_color)\n"\
    #      "\nroot.config(menu=menu)\nfile_menu = Menu(menu, tearoff=0, bg=bg_color, fg=fg_color, activebackground=active_bg_color, activeforeground=active_fg_color)\nfile_menu.add_command(label='Open', command=hello)\nfile_menu.add_separator()\nfile_menu.add_command(label='Exit', command=root.quit)\n"\
    #      "\nhelp_menu = Menu(menu, tearoff=0, bg=bg_color, fg=fg_color, activebackground=active_bg_color, activeforeground=active_fg_color)\nhelp_menu.add_command(label='Test', command=hello)\nmenu.add_cascade(label='File', menu=file_menu)\nmenu.add_cascade(label='Help', menu=help_menu)\n"
    for i in range(0, len(buttonlst), 13):
            if treeviewname[0]!="":
                break

            button_num = buttonlst[i]
            x = buttonlst[i + 2]
            y = buttonlst[i + 3]
            height = buttonlst[i + 4]
            width = buttonlst[i + 5]
            text = buttonlst[i + 6]
            fg = buttonlst[i + 7]
            bg = buttonlst[i + 8]
            font = buttonlst[i + 9]
            font_size = buttonlst[i + 10]
            borderwidth=buttonlst[i + 12]
            selected_item1 = buttonlst[i + 6]
            if selected_item1 in treeviewtools:
                index = treeviewtools.index(selected_item1)
                #print(f"Item '{selected_item1}' found at index {index}")

                continue
            else:
                if buttonlst[i+11] == 'Button':
                    #print("======i found it============")
                    buttonf=f"button{str(button_num)}"
                    butooncreat=f"\n{buttonf}=Button(root,text='{text}',relief=\'raised\',borderwidth={borderwidth},bg='{bg}',fg='{fg}',font=('{font}',{font_size}),height={height},width={width})\n{buttonf}.place(x={x}+xxv,y={y}+yyv)\n"
                    #print("==",butooncreat)
                    butoomlsttext.append(butooncreat)
                elif buttonlst[i + 11] == 'Canvas':
                    canvasf = f"Canvas{str(button_num)}"
                    #canvas = tk.Canvas(root, height=height, width=width, bg=bg)
                    #canvas.place(x=x, y=y)
                    canvascreat=f"\n{canvasf}=tk.Canvas(root,relief=\'raised\',borderwidth={borderwidth}, height={height}, width={width},bg='{bg}')\n{canvasf}.place(x={x}+xxv, y={y}+yyv)\n"
                    butoomlsttext.append(canvascreat)
                elif buttonlst[i + 11] == "Checkbutton":
                    Checkbuttonf = f"Checkbutton{str(button_num)}"
                    #===================================================
                    #var = tk.BooleanVar()
                    #checkbutton = tk.Checkbutton(root, text=text, variable=var, fg=fg, bg=bg, font=(font, font_size))
                    #checkbutton.place(x=y, y=x)
                    creatckbox=f"\n{Checkbuttonf}=tk.Checkbutton(root,relief=\'raised\',borderwidth={borderwidth}, text='{text}',variable=var,fg='{fg}',bg='{bg}', font=('{font}',{font_size}),width={width},height={height})"\
                               f"\n{Checkbuttonf}.place(x={x}+xxv,y={y}+yyv)\n"
                    butoomlsttext.append(creatckbox)
                    #=======================================================
                elif buttonlst[i + 11] == "Entry":
                    #print(width)
                    Entryf = f"Entry{str(button_num)}"
                    #===================================================
                    #entry = tk.Entry(root, width=width, fg=fg, bg=bg, font=(font, font_size))
                    #entry.insert(0, text)
                    #entry.place(x=10, y=10)
                    entrycreat=f"\n{Entryf}=tk.Entry(root,relief=\'raised\',borderwidth={borderwidth},width={width},fg='{fg}',bg='{bg}',font=('{font}',{font_size}))"\
                               f"\n{Entryf}.insert(0,'{text}')\n{Entryf}.place(x={x}+xxv,y={y}+yyv)\n"
                    butoomlsttext.append(entrycreat)
                    #====================================================
                elif buttonlst[i + 11] == "Label":
                    #print(width)
                    Labelf = f"Label{str(button_num)}"
                    #=========================================
                    #label = tk.Label(root, text=text, fg=fg, bg=bg, font=(font, font_size), height=height, width=width)
                    #label.place(x=x+xxv,y=y+yyv)
                    creatlabel=f"\n{Labelf}=tk.Label(root,relief=\'raised\',borderwidth={borderwidth}, text='{text}',fg='{fg}',bg='{bg}',font=('{font}',{font_size}),height={height},width={width})"\
                               f"\n{Labelf}.place(x={x}+xxv,y={y}+yyv)"
                    butoomlsttext.append(creatlabel)
                    #========================================================
                elif buttonlst[i + 11] == "Listbox":
                    #print(width)
                    Listboxf = f"Listbox{str(button_num)}"
                    #listbox = tk.Listbox(root, fg=fg, bg=bg, font=(font, font_size), height=height, width=width)
                    #listbox.insert(tk.END, text)
                    #listbox.place(x=0, y=0)
                    creatlistbox=f"\n{Listboxf}=tk.Listbox(root,relief=\'raised\',borderwidth={borderwidth}, fg='{fg}',bg='{bg}',font=('{font}',{font_size}),height={height},width={width})"\
                                 f"\n{Listboxf}.insert(tk.END, '{text}')\n{Listboxf}.place(x={x}+xxv,y={y}+yyv)\n"
                    butoomlsttext.append(creatlistbox)
                    #===================================================
                elif buttonlst[i + 11] == "Text":
                    Listboxf = f"Text{str(button_num)}"
                    #textbox = tk.Text(root, fg=fg, bg=bg, font=(font, font_size), height=height, width=width)
                    #textbox.place(x=x+xxv,y=y+yyv)
                    creattext=f"\n{Listboxf}=tk.Text(root,relief=\'raised\',borderwidth={borderwidth}, fg='{fg}',bg='{bg}',font=('{font}',{font_size}),height={height},width={width})"\
                              f"\n{Listboxf}.place(x={x}+xxv,y={y}+yyv)\n"
                    butoomlsttext.append(creattext)
                    #=====================================
                elif buttonlst[i + 11] == "ScrolledText":
                    Scrolledf = f"ScrolledT{str(button_num)}"
                    #st = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=width, height=height, font=(font, font_size),fg=fg, bg=bg)
                    #st.insert(tk.INSERT, text)
                    #st.place(x=x, y=y)
                    creatscroll=f"\n{Scrolledf}= scrolledtext.ScrolledText(root,relief=\'raised\',borderwidth={borderwidth}, wrap=tk.WORD, width={width},height={height},font=('{font}',{font_size}),fg='{fg}',bg='{bg}')"\
                                f"\n{Scrolledf}.insert(tk.INSERT,'{text}')\n{Scrolledf}.place(x={x}+xxv,y={y}+yyv)\n"
                    butoomlsttext.append(creatscroll)
                elif buttonlst[i + 11] == "Combobox":
                    Comboboxf=f"Combobox{str(button_num)}"
                    values = ['Option 1', 'Option 2', 'Option 3']
                    #======================================================
                    creatcombos=f"\n{Comboboxf}=ttk.Combobox(root, values=valuescombo, font=('{font}',{font_size}),foreground='{fg}',background='{bg}',height={height},width={width})"\
                                f"\n{Comboboxf}.place(x={x}+xxv,y={y}+yyv)"\
                                f"\n{Comboboxf}.insert(tk.END,'{text}')"
                    butoomlsttext.append(creatcombos)
                elif buttonlst[i + 11] == "OptionMenu":

                    OptionMf=f"OptionMenu{str(button_num)}"
                    creatptionmenu=f"\nselected_valueOP = tk.StringVar()\n{OptionMf}= tk.OptionMenu(root, selected_valueOP,\'{text}\')"\
                                   f"\n{OptionMf}.configure(relief=\'raised\',borderwidth={borderwidth},height={height},width={width},foreground='{fg}',background='{bg}', font=('{font}',{font_size}))"\
                                   f"\nselected_valueOP.set('{text}')\n{OptionMf}.place(x={x}+xxv,y={y}+yyv)\n"
                    butoomlsttext.append(creatptionmenu)
                elif buttonlst[i + 11] == "Radiobutton":
                    Radiobuttonf = f"Radiobutton{str(button_num)}"
                    Radiobutooncreat = f"\n{Radiobuttonf}= tk.Radiobutton(root, text='{text}',variable=tk.StringVar(), value='{text}')"\
                                  f"\n{Radiobuttonf}.config(width={width},height={height},foreground='{fg}',background='{bg}',font=('{font}',{font_size}),relief='raised',borderwidth={borderwidth})"\
                                  f"\n{Radiobuttonf}.place(x={x},y={y})\n"
                    # print("==",butooncreat)
                    butoomlsttext.append(Radiobutooncreat)

        #=======================================================
    if treeviewname[0]=="":
         butoomlsttext.append("\nroot.mainloop()")
    else:
        butoomlsttext.append(f"\nif __name__ == \"__main__\":\n\ttry:\n\t\tdb = Database(\"employees.db\")\n\t\tapp = Application(db)\n\texcept KeyboardInterrupt:\n\t\tpass")

    textallbutton = "  ".join(butoomlsttext)
    return textallbutton
    #print(textallbutton)
def add_text(event, text):
    # get the typed character
    char = text[0]
    text = text[1:]

    # get the scrolledtext widget and append the character
    scrolledtext = event.widget
    scrolledtext.insert(tk.END, char)
    scrolledtext.see(tk.END)

    # play the click sound
    sound1()

    if text:
        # schedule the next character to be added after a short delay
        scrolledtext.after(1, add_text, event, text)


def create_lambda(text):
    # create a lambda function that calls add_text with the given text
    return lambda event: add_text(event, text)

def bind_text_widgets(scrolledtext, text):
    scrolledtext.bind('<FocusIn>', create_lambda(text))
#from tkinter.scrolledtext import ScrolledText

#create_buttons(buttonlst)

#button = Button(root, text="Click me", fg="white", bg="blue", font=("Arial", 12), width=5, height=1)
#button.place(x=100, y=100)

def startcode():

    sound()
    buttonsdfd = create_buttons11(buttonlst)
    global canv1make
    global scrolledtextWW
    # root = tk.Tk()
    scrolledtextWW = tk.scrolledtext.ScrolledText(canvas1, font=('Arial', 10), background=bgbgbg, foreground='white', height=32, width=130,relief='ridge',borderwidth=4)
    text = buttonsdfd
    # bind the <FocusIn> event to a lambda function that calls add_text with the correct text
    bind_text_widgets(scrolledtextWW, text)
    # pack the scrolledtext widget and run the tkinter mainloop
    scrolledtextWW.place(x=100, y=100)


move_entry= tk.Entry(tab1,bd=3, width=3, fg='white', bg=bgbgbg, font=('Arial', 8),cursor='hand2')
move_entry.insert(0, Moves)
move_entry.place(x=561 + xxv, y=497 + yyv)


# ============================================================================

root.startcode = Button(tab2, text='Start_Code',bd=3,command=startcode, bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=20,cursor='hand2')
root.startcode.place(x=494 + xxv, y=547 + yyv)


def copy_text(scrolledtextWW):
    sound()
    scrolledtextWW.tag_add('sel', '1.0', tk.END)
    text_widget = scrolledtextWW.get("sel.first", "sel.last")
    root.clipboard_clear()
    root.clipboard_append(text_widget)

copy_button = Button(tab2, text='Copy_Co',bd=3,command=lambda: copy_text(scrolledtextWW), bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=9,cursor='hand2')
copy_button.place(x=495 + xxv, y=578 + yyv)




def clear_text(scrolledtext):
    sound()
    scrolledtextWW.delete('1.0', tk.END)
    scrolledtextWW.place_forget()

clear_button = Button(tab2, text='Exit_Co',bd=3,command=lambda: clear_text(scrolledtextWW), bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=9,cursor='hand2')
clear_button.place(x=582 + xxv, y=578 + yyv)
#===============


new1lis=[]
cxcx=0
def comborunauto():
    global TTcombo
    global cxcx
    global getbutton
    global TTcomcoMins
    global keydrag
    if keydrag == True:
        keydrag=False
    else:
        keydrag = True

    fillxx=0
    TTcomcoMins=0
    TTcombo=13
    for i in range(0, len(buttonlst), 12):
          buttonlst.insert(i + 1+fillxx ,listbuttonwdget[fillxx])
          fillxx = fillxx+1
    #print("buttonlst after fill wdidget:-",buttonlst)
    # comboboxw.current(comboboxw_values(cxcx))
    cxcx = cxcx + 1
    #print("Button count:", len(comboboxw_values))
    #print("Button details:", comboboxw_values)
    # Assuming you have a combobox widget called comboboxw
    comboboxw['values'] = comboboxw_values
    #print("in auto run",buttonlst)
    for h in range(len(comboboxw_values)):
        comboboxw.current(h)
        on_combobox_selected(h)
    #print
    TTcomcoMins=0
    TTcombo = 13
    getbutton = True
    if keydrag == True:
        keydrag = False
    else:
        keydrag = True

listbuttonwdget=[]
def printbuttons():
        sound()
        global getbutton
        getbutton = False
        global buttonlst
        global button_widget
        global comboboxw_values
        global comboboxw
        new1lis = buttonlst
        comboboxw_values = []
        comboboxw['values'] = ()
        #print("len of buttonlst before for:-", len(buttonlst))
        cxcx=0

        for i in range(0, len(buttonlst), 12):
                button_num, x, y, height, width, text, fg, bg, font, font_size, kindsss, borderwidth = buttonlst[i:i + 12]  # Update the number of values

                if kindsss=='Button':
                      button_widget = tk.Button(canvas1, text=text)
                      canvas1.create_window(x, y, window=button_widget)

                      listbuttonwdget.append(button_widget)

                      #button_widget.config(font=(font, font_size))
                elif kindsss=="Canvas":
                    f = f"Canvas{button_num}"
                    button_widget = tk.Canvas(canvas1)
                    canvas1.create_window(x, y, window=button_widget)
                    pointer_id = button_widget.create_rectangle(0, 0, 1, 1, fill="", outline="",
                                                                tags=("pointer", f))

                    text_entry.delete(0, tk.END)
                    text_entry.insert(0, text)

                    listbuttonwdget.append(button_widget)

                elif kindsss=="Checkbutton":
                    button_widget = tk.Checkbutton(canvas1, text="Button")
                    chkbuttonhh.append(button_widget)

                    ff = f"Check {button_num}"
                    chkbuttonhh.append(ff)
                    listbuttonwdget.append(button_widget)

                elif kindsss == "Entry":
                    button_widget = tk.Entry(canvas1)
                    canvas1.create_window(x, y, window=button_widget)

                    listbuttonwdget.append(button_widget)
                elif kindsss == "Label":
                    button_widget = tk.Label(canvas1, text="Label")
                    canvas1.create_window(x, y, window=button_widget)

                    listbuttonwdget.append(button_widget)

                elif kindsss == "Radiobutton":
                    button_widget = tk.Radiobutton(canvas1, text="Button")
                    ff = f"RadioB {button_num}"
                    radiobtms.append(button_widget)
                    radiobtms.append(ff)
                    update_button()
                    listbuttonwdget.append(button_widget)

                elif kindsss == "Listbox":
                    button_widget = tk.Listbox(canvas1)
                    canvas1.create_window(x, y, window=button_widget)
                    #button_widget.config(font=(font, 10), width=width)
                    button_widget.insert(END, text)

                    listbuttonwdget.append(button_widget)

                elif kindsss == "Text":
                    button_widget = tk.Text(canvas1)
                    button_widget.insert(tk.END, text)

                    listbuttonwdget.append(button_widget)

                elif kindsss == "ScrolledText":
                    button_widget = scrolledtext.ScrolledText(canvas1, width=25, height=15)
                    button_widget.place(x=x, y=y)
                    button_widget.insert(tk.END, text)

                    listbuttonwdget.append(button_widget)

                elif kindsss == "Combobox":
                    # combo_box = ttk.Combobox(root, values=values, font=(font, font_size), foreground=fg, background=bg,height=height, width=width)
                    # combo_box.place(x=0, y=0)
                    button_widget = ttk.Combobox(canvas1, width=width)
                    button_widget.config(width=width)
                    button_widget.config(foreground=fg)
                    button_widget.place(x=x, y=y)
                    #button_widget.configure(background=bg, width=width)
                    button_widget.insert(tk.END, text)

                    listbuttonwdget.append(button_widget)

                elif kindsss == "OptionMenu":
                    global option
                    global variable
                    f = f"OptionMenu{button_num}"
                    options = ["Option 1", "Option 2", "Option 3"]
                    variable = tk.StringVar(canvas1)
                    variable.set(options[0])
                    button_widget = tk.OptionMenu(canvas1, variable, *options)
                    button_widget.configure(width=width, foreground=fg, background=bg)
                    button_widget.place(x=x, y=y)
                    f = f"OptionM{button_num}"
                    button_widget["menu"].delete("0", "end")
                    options = []
                    new_option = f
                    options.append(new_option)
                    variable.set(options[0])  # reset the selected value to the first option
                    button_widget["menu"].delete(0, "end")  # delete the existing menu items
                    for option in options:
                        button_widget["menu"].add_command(label=option, command=tk._setit(variable, option))
                        # print(option,variable)
                    optinmaddss.append(option)
                    optinmaddss.append(variable)
                    optinmaddss.append(button_widget["menu"])

                    listbuttonwdget.append(button_widget)
                #print(f"no :-{button_num}, x:- {x}, y:- {y}, height:- {height},width :- {width}, text :-{text}, fg:-{fg},bg:-{bg},font:-{font},font size:-{font_size},kind:-{kindsss},borderwidth:-{borderwidth}\n")
                #new1lis.insert(i + 1, button_widget)
                # -------------------------------------------

                comstr = f"{button_num}  {text}"
                comboboxw_values.append(comstr)
        #print("listbuttonwdget",listbuttonwdget)
        comborunauto()

            #-------------------------------------------


buttonlst1=[]

def ResetAll():
    global button_widget
    button_widget=""

    for widget in canvas1.winfo_children():
        widget.destroy()
    global buttonlst
    buttonlst = []
    global oves
    oves = 1
    global eventxy
    eventxy = []
    global buttoncount
    buttoncount = 1
    global buttonlistkey
    buttonlistkey = False
    global addlist
    addlist = [0]
    global comboboxw_values
    comboboxw_values = []
    global number
    number = 0
    global grtmum
    grtmum = [0]
    global kinds
    kinds = ["t"]
    global TTcombo
    TTcombo = 13
    global TTcomcoMins
    TTcomcoMins = 0
    global colorjump
    colorjump = False
    global getbutton
    getbutton = True
    global destroyesno
    destroyesno = False
    global buttonnamenew
    buttonnamenew = ["g"]
    global keydrag
    keydrag = False
    global KeyDragOnOffName
    KeyDragOnOffName = ["none"]
    global optinmaddss
    optinmaddss = []
    global chkbuttonhh
    chkbuttonhh = []
    global radiobtms
    radiobtms = []
    comboboxw_values = []
    grtmum = [0]
    kinds = ["t"]
    TTcombo = 13
    TTcomcoMins = 0
    eventxy = []
    buttonlst = []
    buttoncount = 1
    buttonlistkey = False
    global dontruns
    dontruns = False
    global cok
    cok = 1
    global buttonlst1
    buttonlst1 = []
    global new1lis
    new1lis = []
    global cxcx
    cxcx = 0
#-------------------------------------------------------
def load_list():
    sound()
    global buttonlst
    global mainprogscr
    global addlist  # Add a global variable for the third list


    program_path = os.path.dirname(os.path.abspath(__file__))

    # Open the file dialog to choose the file
    file_path = filedialog.askopenfilename(
        initialdir=program_path,
        title="Select File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
            ResetAll()

            try:
                with open(file_path, "r") as f:
                    buttonlst = []
                    mainprogscr = []
                    addlist = []  # Initialize the third list to an empty list
                    i = 0
                    for line in f:
                        values = line.strip().split(',')
                        for value in values:
                            try:
                                if i == 0:
                                    buttonlst.append(int(value))
                                elif i == 1:
                                    mainprogscr.append(int(value))
                                else:
                                    addlist.append(int(value))  # Append the value to the third list
                            except ValueError:
                                if i == 0:
                                    buttonlst.append(value)
                                elif i == 1:
                                    mainprogscr.append(value)
                                else:
                                    addlist.append(value)  # Append the value to the third list
                        i += 1
                    #print("Lists loaded.")
                    #print("Button list:", buttonlst)
                    #print("Main program script:", mainprogscr)
                    #print("Additional list:", addlist)  # Print the third list to the console
                    #print("Lists loaded.")
                    #print("buttonlst1: ", buttonlst)
                    #print("mainprogscr: ", mainprogscr)
                    rootmx.delete(0, tk.END)
                    rootmx.insert(0, mainprogscr[2])
                    rootmy.delete(0, tk.END)
                    rootmy.insert(0, mainprogscr[3])
                    rootcolor.delete(0, tk.END)
                    rootcolor.insert(0, mainprogscr[4])

                    draw_rectangle()
                    #print("len of buttonlst when load:-", len(buttonlst))
                    #for i in range(0, len(buttonlst), 12):
                        #button_num, x, y, height, width, text, fg, bg, font, font_size, kindsss,borderwidth = buttonlst[i:i + 12]
                        #print(f"no :-{button_num}, x:- {x}, y:- {y}, height:- {height},width :- {width}, text :-{text}, fg:-{fg},bg:-{bg},font:-{font},font size:-{font_size},kind:-{kindsss},borderwidth:-{borderwidth}\n")
                    printbuttons()
                    messagebox.showinfo("File Loaded", "The file was successfully loaded.")


            except FileNotFoundError:
                messagebox.showerror("File Error", "File not found.")

    f.close()

cok=1
def save_list():
    sound()
    buttonlst1 = []
    for i in range(0, len(buttonlst), 13):
        buttonlst1.extend(buttonlst[i:i + 1])  # Append buttonlst[0+i]
        buttonlst1.extend(buttonlst[2 + i:i + 13])  # Append buttonlst[2+i] to buttonlst[11+i]

    #print(buttonlst1)
    program_path = os.path.dirname(os.path.abspath(__file__))

    file_name = filedialog.asksaveasfilename(
        initialdir=program_path,
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_name:
            with open(file_name, "w") as f:
                f.write(','.join(str(x) for x in buttonlst1))

                f.write('\n')
                f.write(','.join(str(x) for x in mainprogscr))

                f.write('\n')
                f.write(','.join(str(x) for x in addlist))

            messagebox.showinfo("File Saved", "The file was successfully saved.")
    f.close()
    #print ("in save addlist ",addlist)
save_button  = Button(tab2, text='Save_Project',bd=3,command=save_list, bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=20,cursor='hand2')
save_button .place(x=494 + xxv, y=484 + yyv)

load_button = Button(tab2, text='Load_Project',bd=3,command=load_list, bg=bgbgbg, fg='white', font=('Arial', 10), height=1, width=20,cursor='hand2')
load_button.place(x=494 + xxv, y=515 + yyv)



def draw_lines():
    WIDTH = 1260
    HEIGHT = 720
    ROWS = 60
    COLS = 120
    # Calculate the distance between each row and column
    row_distance = HEIGHT // ROWS
    col_distance = WIDTH // COLS
    square_width = col_distance - 1  # Width of the squares
    square_height = row_distance - 1  # Height of the squares

    # Draw the transparent squares
    for row in range(ROWS):
        y = row * row_distance
        for col in range(COLS):
            x = col * col_distance
            # Set the color with alpha value (RGB)
            color = f"#{''.join(['199'] * 3)}"
            canvas1.create_rectangle(x, y, x + square_width, y + square_height, outline=color)





#drowlines1()
def draw_rectangle(colors1):
    sound()

    #print("rectangle def",mainprogscr)
    global canv1make
    fillmainpro()
    canv1make=f"canvas1 = tk.Canvas(root,width={int(mainprogscr[2])-5},height={int(mainprogscr[2])-5},background='{mainprogscr[4]}',borderwidth=1)"

    global rectangle_id
    canvas_width = canvas1.winfo_width()
    canvas_height = canvas1.winfo_height()

    rect_width = int(rootmx.get())
    rect_height = int(rootmy.get())

    x1 = (canvas_width - rect_width) / 2
    y1 = (canvas_height - rect_height) / 2
    x2 = x1 + rect_width
    y2 = y1 + rect_height
    hex_color9o = rootcolor.get()

    if rectangle_id is not None:
        canvas1.delete(rectangle_id)
    #print("===in rect ==>",colors1)
    rectangle_id = canvas1.create_rectangle(x1, y1, x2, y2, fill=colors1, outline="green")
    draw_lines()
#=========================================================
def update_running_time():
    now = datetime.now()
    now1 = now.strftime("%I-%M-%S %p")
    time1 = f"Date:  {now.year}-{now.month}-{now.day}  Time:{now1}"
    Label3ff.configure( foreground="white", font=("Arial", 7), text=time1)
    root.after(1000, update_running_time)
update_running_time()
def call_function_once():
    global function_called
    if not function_called:
        draw_lines()
        #print ("i drow the lines when start")
        function_called = True

function_called = False
root.after(600, call_function_once)

root.mainloop()