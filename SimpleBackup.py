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
appWidth = 1000
appHeight = 785
# get windows screan width and height
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# center position 
appXpos = int((screenWidth/2)-(appWidth/2))
appYpos = int((screenHeight/2)-(appHeight/2))
# create app window 
root.geometry(f'{appWidth}x{appHeight}+{appXpos}+{appYpos}')
##### 


fontSize = 11


### TOP ###
frameTop = Frame(root,bg="blue",width=400,height=50)



root.mainloop()

