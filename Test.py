import customtkinter as ctk
from tkinter import LEFT, X
from datetime import datetime

# Initialize main application window
root = ctk.CTk()  # Create the main window (root)

# Initialize the StringVar to hold the log message
endlog = ctk.StringVar()

# Create a bottom frame
frameBottom = ctk.CTkFrame(root, height=32)  # No need for bg_color in customtkinter
frameBottom.pack(fill=X)



def logIt(x):
    endlog.set(x)

# Example usage: Call logIt to add an entry and update the label
x = ctk.CTkButton(root,text="fdff",command=lambda:logIt(datetime.now()))
x.pack()

# Create a label that displays the current log message
logLabel = ctk.CTkLabel(frameBottom, textvariable=endlog)  # Bind the label text to the StringVar
logLabel.pack(side=LEFT, padx=4)



# Run the main application loop
root.mainloop()
