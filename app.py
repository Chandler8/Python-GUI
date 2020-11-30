import tkinter as tk
from tkinter import Label, filedialog, Text
import os

root = tk.Tk()

# Create appending method here, loop over this later on as well
# This empty array is what all of our added .exe files will get pushed too
apps = []

# Error handling, this gets rid of empty places in our files, accounting for if a user where to select a blank or invalid file type
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        # print(tempApps)
        # This organizes the users input files by seperating them by commas 
        tempApps = tempApps.split(',')
        # Strips out any existing white space or gaps between our chosen apps
        apps = [x for x in tempApps if x.strip()]

def addApp():

    # Create a function that stops appended files from repeating on top of each other upon every new appendage
    for widget in frame.winfo_children():
        widget.destroy()

    # Drill down into root file (C drive) and filter so that only files with the .exe designation are displayed as available to interact with to users
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                            filetypes=(("executables","*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    # Indentation matters, be careful where you place variables

    # Add files and their paths to our main working area
    for app in apps:
     label = tk.Label(frame, text=app, bg="royalblue")
     label.pack()

# Create a funtion that loops over our apps array and allows the operating system to run the files
def runApps():
    for app in apps:
        os.startfile(app)

# Outer frame that holds our work space
canvas = tk.Canvas(root, height=700, width=700, bg="deepskyblue")
canvas.pack()

# Inner frame for our files to be stored on
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Now create a clickable button that is attached to the root, not the workspace. AKA it will sit parallel with the borders of the application, add in our command function that is defined above.
openFile = tk.Button(root, text="Open File", padx=10,
                        pady=5, fg="white", bg="red", command=addApp)

openFile.pack()

# Create 2nd clickable root button that runs our selected applications, add in our command function that is defined above
runApps = tk.Button(root, text="Run Apps", padx=10,
                        pady=5, fg="white", bg="red", command=runApps)

runApps.pack()

# Setup previously entered apps persisting upon reload
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()

# Whenever app is closed this creates a text file that saves all files the user ran in that particular instance
# Technically speaking, this loops over apps again and gives users the ability to save their files (w=write)
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')


# Future Dev

    # Would like to add a "routines" feature that a user could open up depening upon their desired outcome
                # For example a user could have a "Work From Home" routine containing all neccessary programs for that situation
                # A user could also have a "Gaming" routine that opens their desired client for gaming and possibly the steam store so they could add to their arsenal

    # Could also add a delete button within the root that can just delete individual files from your lineup
                # lets say if a user accidently added something they dont care to have there

    # Would love to create an automated delete feature that would scrap whole files 
                # In the event an entire routine got outdated, you could kill it