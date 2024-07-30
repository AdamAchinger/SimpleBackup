from tkinter import * 
import customtkinter as ctk
import json
import os

root = ctk.CTk()

### Version ###
toolVersion = 2.1

root.title("Simple Backup"+" v"+str(toolVersion))
root.iconbitmap('S:\GitHub\SimpleBackup\img\AA_icon.ico')
#root.resizable(False,False)

#####
# application dimensions
appWidth = 512
appHeight = 512
# get windows screan width and height
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# center position 
appXpos = int((screenWidth/2)-(appWidth/2))
appYpos = int((screenHeight/2)-(appHeight/2))
# create app window 
root.geometry(f'{appWidth}x{appHeight}+{appXpos}+{appYpos}')
##### 

fSize = 11

### TOP ###
frameTop = ctk.CTkFrame(root,bg_color="blue",height=64)
frameTop.pack(fill=X)

ConfigButton = ctk.CTkButton(frameTop,text="Open Config",font=("ROBOTO",16),height=32)
ConfigButton.pack(side=LEFT,padx=4,pady=4)

MasterLogButton = ctk.CTkButton(frameTop,text="Open Log",font=("ROBOTO",16),height=32)
MasterLogButton.pack(side=LEFT,padx=4,pady=4)


frameMiddle = ctk.CTkScrollableFrame(root,bg_color="orange",height=32)
frameMiddle.pack(expand=TRUE,fill=BOTH,pady=4)

for x in range(5):
    frameBackup = ctk.CTkFrame(frameMiddle,bg_color="red",height=256)
    frameBackup.pack(fill=X,padx=8,pady=4)

frameBottom = ctk.CTkFrame(root,bg_color="white",height=32)
frameBottom.pack(fill=X)

logLable = ctk.CTkLabel(frameBottom,text="[ S:/SimpleBackup -> F:/SimpleBackup ] [Complited] ")
logLable.pack(side=LEFT,padx=4)

root.mainloop()

