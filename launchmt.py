from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfilename, askopenfilename


def savefile():
    files = [('Text Document', '*.txt')]
    file = asksaveasfilename(filetypes = files, defaultextension = files)
    try:
        the_thing = open(file, 'w')
        content = edit.get(1.0, "end-1c")
        the_thing.writelines(content)
    except:
        pass

def openfile():
    files = [('All files', '*.*')]
    file = askopenfilename(filetypes = files, defaultextension = files)
	try:
    	the_thing = open(file, 'r')
    	edit.delete(1.0,"end")
    	edit.insert(1.0, the_thing.read())
    	window.title(str(file) + " - Mantita Text Edit")
    except:
    	pass


window = Tk()
window.title("Untitled - Mantita Text Edit")

sphoto = PhotoImage(file = r"~/mantita/save.png")
lphoto = PhotoImage(file = r"~/mantita/load.png")

control_frame = Frame(window)
savebtn = Button(control_frame, text = "Save", image = sphoto, compound = LEFT, command = savefile)
openbtn = Button(control_frame, text = "Open", image = lphoto, compound = LEFT, command = openfile)

edit = Text(window, borderwidth = 1, relief = "sunken")

control_frame.grid(column=1, row=1)
savebtn.grid(column=1, row=1)
openbtn.grid(column=2, row=1)
edit.grid(column = 1,row = 2)

window.mainloop()
