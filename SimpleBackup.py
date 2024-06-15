from tkinter import * 
import customtkinter as ctk
import json


root = ctk.CTk()

### Version ###
toolVersion = 2.1

root.title("Simple Backup"+" v"+str(toolVersion))
root.iconbitmap('S:\GitHub\SimpleBackup\img\AA_icon.ico')
#root.resizable(False,False)

#####
# application dimensions
appWidth = 1000
appHeight = 800
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

updateButton11 = ctk.CTkButton(frameLT,text="UPDATE",font=("ROBOTO",24),width=110,height=50)
updateButton11.pack(padx=6,pady=4,side=LEFT)

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

frameRT = Frame(frameRight,bg="blue",width=400,height=225)
frameRT.pack(padx=3,pady=3,side=TOP,fill=BOTH)
frameRT.pack_propagate(False)


frameRTT1 = Frame(frameRT,bg="black",width=400,height=50)
frameRTT1.pack(padx=3,pady=1,side=TOP,fill=X)
frameRTT1.grid_propagate(False)


infoLable7 = ctk.CTkLabel(frameRTT1,text="Backup 1",font=("ROBOTO",20))
infoLable7.pack(padx=12,pady=2,side=LEFT)

infoLable71 = ctk.CTkLabel(frameRTT1,text="READY",font=("ROBOTO",20),text_color="green")
infoLable71.pack(padx=2,pady=2,side=LEFT)

infoLable711 = ctk.CTkLabel(frameRTT1,text="Note: "+"Ext Drive",font=("ROBOTO",20))
infoLable711.pack(padx=12,pady=2,side=LEFT)


frameRTT2 = Frame(frameRT,bg="black",width=400,height=35)
frameRTT2.pack(padx=3,pady=1,side=TOP,fill=X)
frameRTT2.pack_propagate(False)

infoLable77 = ctk.CTkLabel(frameRTT2,text="F:/SimpleBackup/PixelProcesor/",font=("ROBOTO",18))
infoLable77.pack(padx=12,pady=2,side=LEFT)




frameRTB = Frame(frameRT,bg="black",width=400,height=100)
frameRTB.pack(padx=3,pady=1,side=TOP,fill=X)
frameRTB.grid_propagate(False)

infoLable1 = ctk.CTkLabel(frameRTB,text="File Amount:",font=("ROBOTO",18))
infoLable1.grid(row=0,column=0,padx=12,pady=2,sticky=NW)
infoLable2 = ctk.CTkLabel(frameRTB,text="First Update:",font=("ROBOTO",18))
infoLable2.grid(row=1,column=0,padx=12,pady=2,sticky=W)
infoLable3 = ctk.CTkLabel(frameRTB,text="Last Update:",font=("ROBOTO",18))
infoLable3.grid(row=2,column=0,padx=12,pady=2,sticky=W)

infoLable11 = ctk.CTkLabel(frameRTB,text="4022",font=("ROBOTO",18))
infoLable11.grid(row=0,column=1,padx=6,pady=2,sticky=NW)
infoLable22 = ctk.CTkLabel(frameRTB,text="10.12.2023",font=("ROBOTO",18))
infoLable22.grid(row=1,column=1,padx=6,pady=2,sticky=W)
infoLable33 = ctk.CTkLabel(frameRTB,text="12.02.2024",font=("ROBOTO",18))
infoLable33.grid(row=2,column=1,padx=6,pady=2,sticky=W)


infoLable4 = ctk.CTkLabel(frameRTB,text="Source Size:",font=("ROBOTO",18))
infoLable4.grid(row=0,column=2,padx=12,pady=2,sticky=NW)
infoLable5 = ctk.CTkLabel(frameRTB,text="Backup Size:",font=("ROBOTO",18))
infoLable5.grid(row=1,column=2,padx=12,pady=2,sticky=W)
infoLable6 = ctk.CTkLabel(frameRTB,text="Backup Amount:",font=("ROBOTO",18))
infoLable6.grid(row=2,column=2,padx=12,pady=2,sticky=W)

infoLable44 = ctk.CTkLabel(frameRTB,text="1,23 GB",font=("ROBOTO",18))
infoLable44.grid(row=0,column=3,padx=6,pady=2,sticky=NW)
infoLable55 = ctk.CTkLabel(frameRTB,text="10,23 GB",font=("ROBOTO",18))
infoLable55.grid(row=1,column=3,padx=6,pady=2,sticky=W)
infoLable66 = ctk.CTkLabel(frameRTB,text="10",font=("ROBOTO",18))
infoLable66.grid(row=2,column=3,padx=6,pady=2,sticky=W)


frameRTBB = Frame(frameRT,bg="black",width=400,height=120)
frameRTBB.pack(padx=3,pady=1,side=TOP,fill=X,expand=1)
frameRTBB.grid_propagate(False)

backupButton1 = ctk.CTkButton(frameRTBB,text="Backup",font=("ROBOTO",22),width=70,height=35)
backupButton1.pack(padx=6,pady=6,side=LEFT)

restoreButton1 = ctk.CTkButton(frameRTBB,text="Restore",font=("ROBOTO",22),width=70,height=35)
restoreButton1.pack(padx=6,pady=6,side=LEFT)

openButton1 = ctk.CTkButton(frameRTBB,text="Open",font=("ROBOTO",22),width=70,height=35)
openButton1.pack(padx=6,pady=6,side=LEFT)

updateButton1 = ctk.CTkButton(frameRTBB,text="Update",font=("ROBOTO",22),width=70,height=35)
updateButton1.pack(padx=6,pady=6,side=LEFT)

configButton1 = ctk.CTkButton(frameRTBB,text="Config",font=("ROBOTO",22),width=70,height=35)
configButton1.pack(padx=6,pady=6,side=LEFT)








root.mainloop()

