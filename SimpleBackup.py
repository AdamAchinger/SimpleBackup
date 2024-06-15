from tkinter import * 
from libs.widgets import targetWidget
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
frameTop.pack(padx=3,pady=1,side=TOP,fill=X)

### Bottom ###
frameBottom = Frame(root,bg="black",width=400,height=50)
frameBottom.pack(padx=3,pady=1,side=BOTTOM,fill=X)

frameBB = Frame(frameBottom,bg="white",width=400,height=25)
frameBB.pack(padx=3,pady=3,side=TOP,fill=X)


### Left ###
frameLeft = Frame(root,bg="black",width=400,height=appHeight)
frameLeft.pack(padx=2,pady=3,side=LEFT,fill=BOTH,expand=1)

frameLT = Frame(frameLeft,bg="blue",width=400,height=50)
frameLT.pack(padx=3,pady=3,side=TOP,fill=X)
frameLT.pack_propagate(False)
config = open('S:\GitHub\SimpleBackup\config.json','r').read()
backupPlans = json.loads(config)



backupPlanSourceDir = []
backupPlanNames = []
for x in backupPlans["backupPlans"]:
    backupPlanNames.append(str(x["name"]))
    backupPlanSourceDir.append(x["sourceDir"])

backupSelection1 = ctk.StringVar(value="Select Backup Plan")
backupSelection = ctk.CTkOptionMenu(frameLT,variable=backupSelection1,values=backupPlanNames,font=("ROBOTO",24),height=50)
backupSelection.pack(padx=6,pady=4,side=LEFT,fill=X,expand=1)

RefreshButton11 = ctk.CTkButton(frameLT,text="Refresh",font=("ROBOTO",24),width=110,height=50)
RefreshButton11.pack(padx=6,pady=4,side=LEFT)

##### TOPBAR SELECTED DIR #####
frameTB = Frame(frameTop,bg="black",width=400,height=25)
frameTB.pack(padx=3,pady=3,side=BOTTOM,fill=X)
frameTB.pack_propagate(False)


backupSelectedDir = ctk.CTkLabel(frameTB,textvariable=ctk.StringVar(value=backupPlanSourceDir[0]),font=("ROBOTO",16))
backupSelectedDir.pack(padx=12,pady=3,side=LEFT)


frameLB = Frame(frameLeft,bg="green",width=400,height=appHeight)
frameLB.pack(padx=3,pady=3,side=BOTTOM,fill=BOTH,expand=1)



### Right ###
frameRight = Frame(root,bg="black",width=400,height=appHeight)
frameRight.pack(padx=2,pady=3,side=RIGHT,fill=BOTH,expand=1)

####################

targetDir1 = "F:/SimpleBackupTarger/PixelProcesor/"
targetDir2 = "I:/SimpleBackupTarger/PixelProcesor/"
targetDir3 = ""

targetNote1 = "External F Drive"
targetNote2 = "External I Drive"
targetNote3 = ""

targetName1 = "Backup 1"
targetName2 = "Backup 2"
targetName3 = ""

target1 = targetWidget(root,frameRight,targetDir1,targetNote1,targetName1)
target2 = targetWidget(root,frameRight,targetDir2,targetNote2,targetName2)
target3 = targetWidget(root,frameRight,targetDir3,targetNote3,targetName3)








root.mainloop()

