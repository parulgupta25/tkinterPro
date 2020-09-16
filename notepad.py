from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Parul's Notepad")
    file = None
    textArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        f = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")])
        if file == "":
            file = None
        else:
            # Save as a new file
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + "-Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()
def cut():
    textArea.event_generate(("<<Cut>>"))
def copy():
    textArea.event_generate(("<<Copy>>"))
def paste():
    textArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad", "Notepad by Parul Gupta")

if __name__ == '__main__':
    # Basic tkinter setup
    root = Tk()
    root.title("Parul's Notepad")
    root.wm_iconbitmap("Notepad.ico")
    root.geometry("644x408")

    # Add TextArea
    textArea = Text(root, font="lucida 13")
    file = None
    textArea.pack(expand=True, fill=BOTH)

    # Create MenuBar
    mainMenu = Menu(root)

    # File menu starts
    fileMenu = Menu(mainMenu, tearoff=0)
    # To open new file
    fileMenu.add_command(label="New", command=newFile)
    # To open already existing file
    fileMenu.add_command(label="Open", command=openFile)
    # To save the current file
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quitApp)
    mainMenu.add_cascade(label="File", menu=fileMenu)
    root.config(menu=mainMenu)

    # Edit menu starts
    editMenu = Menu(mainMenu, tearoff=0)
    # To give  a feature of cut, copy and paste
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    mainMenu.add_cascade(label="Edit", menu=editMenu)
    root.config(menu=mainMenu)

    # Help menu starts
    helpMenu = Menu(mainMenu, tearoff=0)
    helpMenu.add_command(label="About Notepad", command=about)
    mainMenu.add_cascade(label="Help", menu=helpMenu)
    root.config(menu=mainMenu)

    # Adding Scrollbar
    scrollbar = Scrollbar(textArea)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scrollbar.set)

    root.mainloop()
