import tkinter as tk
from tkinter import Toplevel, Variable, ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
from tkinter.constants import LEFT

main_application = tk.Tk()
main_application.geometry("1200x800")
main_application.title("Vpad text editor")

################################ main menu ##############################
main_menu = tk.Menu()
# File_icons :
new_icon = tk.PhotoImage(file="icons2/new.png")
open_icon = tk.PhotoImage(file="icons2/open.png")
save_icon = tk.PhotoImage(file="icons2/save.png")
save_as_icon = tk.PhotoImage(file="icons2/save_as.png")
exit_icon = tk.PhotoImage(file="icons2/exit.png")

File = tk.Menu(main_menu,tearoff=0)

# Edit icons:
cut_icon = tk.PhotoImage(file='icons2/cut.png')
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

Edit = tk.Menu(main_menu,tearoff=0)

# Tool bar and Status bar icons:
tool_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_icon = tk.PhotoImage(file='icons2/status_bar.png')

View = tk.Menu(main_menu,tearoff=0)

# Colour:

light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

Colour_Theme = tk.Menu(main_menu,tearoff=0)

theme_colour = tk.StringVar()
colour_icon=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

colour_dict = {
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Nigh Blue':('#ededed','#6b9dc2')
}

# Cascade
main_menu.add_cascade(label="File",menu= File)
main_menu.add_cascade(label="Edit",menu= Edit)
main_menu.add_cascade(label="View",menu= View)
main_menu.add_cascade(label="Color Theme",menu=Colour_Theme)
#..........................&&&&& End main menu &&&&&.............................

################################ toolbar menu ##############################
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

## font box :

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=30,textvariable=font_family,state= "readonly")
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx= 5)

## size box :
size_var = tk.IntVar()
font_size =ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']= tuple(range(8,81,2))
font_size.current(2)
font_size.grid(row=0, column=1, padx=5)

## Bold Button :
Bold_icon = tk.PhotoImage(file="icons2/bold.png")
Bold_btn = ttk.Button(tool_bar,image= Bold_icon)
Bold_btn.grid(row=0,column=2, padx=5)

## Italic Button :
Italic_icon = tk.PhotoImage(file="icons2/italic.png")
Italic_btn = ttk.Button(tool_bar,image=Italic_icon)
Italic_btn.grid(row=0,column=3,padx=5)

## Underline Button :
Underline_icon = tk.PhotoImage(file="icons2/underline.png")
Underline_btn = ttk.Button(tool_bar,image=Underline_icon)
Underline_btn.grid(row=0,column=4,padx=5)

## Font Color Button :
Font_color_icon = tk.PhotoImage(file="icons2/font_color.png")
Font_color_btn = ttk.Button(tool_bar,image=Font_color_icon)
Font_color_btn.grid(row=0,column=5,padx=5)

## Text Alignment Button :
align_left_icon = tk.PhotoImage(file="icons2/align_left.png")
align_left_btn = ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

# align center :
align_center_icon =tk.PhotoImage(file="icons2/align_center.png")
align_center_btn =ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

# align right :
align_right_icon =tk.PhotoImage(file="icons2/align_right.png")
align_right_btn = ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

#..........................&&&&& End toolbar menu &&&&&.............................

################################ main menu ##############################
#..........................&&&&& End main menu &&&&&.............................

################################ main menu ##############################
#..........................&&&&& End main menu &&&&&.............................

################################ main menu ##############################
#..........................&&&&& End main menu &&&&&.............................

################################ main menu functionality ##############################

## file menu command :
File.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator="Ctrl+N")
File.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator="Ctrl+O")
File.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator="Ctrl+S")
File.add_command(label="Save As", image=save_as_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+S")
File.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator="Ctrl+Q")

## edit menu command :
Edit.add_command(label='Cut', image= cut_icon, compound=tk.LEFT, accelerator='Ctrl+X')
Edit.add_command(label='Copy', image= copy_icon, compound=tk.LEFT, accelerator='Ctrl+C')
Edit.add_command(label='Paste', image= paste_icon, compound=tk.LEFT, accelerator='Ctrl+V')
Edit.add_command(label='Clear All', image= clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X')
Edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F')

## View menu checkbutton :
View.add_checkbutton(label='Tool bar', image=tool_icon, compound=tk.LEFT)
View.add_checkbutton(label='Status bar', image=status_icon, compound=tk.LEFT)

## Colour menu radiobutton :
count = 0
for i in colour_dict:
    Colour_Theme.add_radiobutton(label = i,image = colour_icon[count], variable=theme_colour, compound=tk.LEFT)
    count += 1
#..........................&&&&& End main menu functionality &&&&&.............................

main_application.config(menu=main_menu)
main_application.mainloop()