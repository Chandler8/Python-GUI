# Test

import tkinter as tk
from tkinter import Label, filedialog, Text
import os

root = tk.Tk()
# Create appending method here, loop over this later on as well
apps = []

def addApp():

# Create a function that stops appended files from repeating on top of each other upon every new appendage
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                            filetypes=(("executables","*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    # Indentation matters, be careful where you place variables

# Add files and their paths to our main working area
    for app in apps:
     label = tk.Label(frame, text=app, bg="royalblue")
     label.pack()

# Outer frame that holds our work space
canvas = tk.Canvas(root, height=700, width=700, bg="deepskyblue")
canvas.pack()

# Inner frame for our files to be stored on
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Now create a clickable button that is attached to the root, not the workspace. AKA it will sit parallel with the borders of the application
openFile = tk.Button(root, text="Open File", padx=10,
                        pady=5, fg="white", bg="red", command=addApp)

openFile.pack()

# Create 2nd clickable root button that runs our selected applications
runApps = tk.Button(root, text="Run Apps", padx=10,
                        pady=5, fg="white", bg="red")

runApps.pack()

root.mainloop()