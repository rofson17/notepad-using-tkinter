from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untittle -Notepad")
    file=None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file =="":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def Quit():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))


def past():
    TextArea.event_generate(("<<Paste>>"))


def about():
    showinfo("Notepad", "Notepad by Rofson Jame Abu Siam")




if __name__ == '__main__':
    root=Tk()

    #tittle
    root.title("Untittle -Notepad")
    root.wm_iconbitmap("favicon.ico")
    root.geometry("550x400")
    root.minsize(470,300)

    #textarea
    TextArea=Text(root,font="Consolas 10")
    file=None
    TextArea.pack(expand=True, fill=BOTH)

    #menue bar
    #file menu start
    MenuBar=Menu(root)
    fileMenu=Menu(MenuBar, tearoff=0)

    #open  new file
    fileMenu.add_command(label="New", command=newFile)

    #opening file
    fileMenu.add_command(label="Open", command=openFile)

    #save current file
    fileMenu.add_command(label="Save", command=saveFile)
    #rename
    #save current file
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=Quit)

    MenuBar.add_cascade(label="File",menu=fileMenu)
    #file menu end

    #edit menu start
    editMen=Menu(MenuBar,tearoff=0)
    #cut feture
    editMen.add_command(label="Cut", command=cut)
    #copy
    editMen.add_command(label="Copy", command=copy)
    #paste
    editMen.add_command(label="Paste", command=past)
    MenuBar.add_cascade(label="Edit", menu=editMen)
    # edit menu start

    #about
    helpMenu=Menu(MenuBar,tearoff=0)
    helpMenu.add_command(label="About", command=about)
    MenuBar.add_cascade(label="Help", menu=helpMenu)
    #about menu end

    root.config(menu=MenuBar)

    #scroll bar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()