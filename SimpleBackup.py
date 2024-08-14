from tkinter import * 
import customtkinter as ctk
from datetime import datetime
import json
import os
import sys
import shutil

root = ctk.CTk()

### Version ###
toolVersion = 6.3

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
### Functions ###
def refresh():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def openConfig():
    os.system("notepad.exe "+"config.json")
    
def openLog():
    os.system("notepad.exe "+"log.txt")

def openDirectory(Path):  
    os.startfile(Path)

### set endlog ###

endlog = ctk.StringVar()

def logIt(command):
    with open("log.txt","a") as logFile:
        now = datetime.now()
        formatted_date = now.strftime('%d.%m.%Y %H:%M:%S')
        logFile.writelines(f"{formatted_date} | {command} \n")
    logFile.close()

    endlog.set(command)

def backup(source,target,name,v):
    now = datetime.now()
    fd = now.strftime('%d%m%Y')
    t = f"{target}\\v{v}_{fd}\\{name}"
    shutil.copytree(source,t)


### Start Log ###
with open("log.txt","a") as logFile:
    logFile.writelines(f"######################################################\n")
logFile.close()

logIt("SimpleBackup  >  Start")

################################################################

### TOP ###
frameTop = ctk.CTkFrame(root,height=64)
frameTop.pack(fill=X)


RefreshButton = ctk.CTkButton(frameTop,text="Refresh",command=lambda:[ logIt("Refresh"), refresh() ],font=("ROBOTO",16),height=32,width=128)
RefreshButton.pack(side=LEFT,padx=4,pady=4)

ConfigButton = ctk.CTkButton(frameTop,text="Open Config",command=lambda:[ logIt("Open Config"+"  |  "+"config.json"), openConfig() ],font=("ROBOTO",16),height=32,width=128)
ConfigButton.pack(side=LEFT,padx=4,pady=4)

LogButton = ctk.CTkButton(frameTop,text="Open Log",command=lambda:[ logIt("Open Log"+"  |  "+"log.txt"), openLog() ],font=("ROBOTO",16),height=32,width=128)
LogButton.pack(side=LEFT,padx=4,pady=4)



frameMiddle = ctk.CTkScrollableFrame(root,height=32)
frameMiddle.pack(expand=TRUE,fill=BOTH,pady=4)


### JSON ###

with open("config.json","r") as config: 
    data = json.loads(config.read())


for plan_name, pd in data.items():

    targetDirCount = len(pd["targetDir"])

    frameBackup = ctk.CTkFrame(frameMiddle,fg_color="#555555",height=256)
    frameBackup.pack(fill=X,padx=2,pady=6)

    frameBackup1 = ctk.CTkFrame(frameBackup,height=256)
    frameBackup1.pack(fill=X,padx=4,pady=2)

    frameBackupSourceTop = ctk.CTkFrame(frameBackup1,height=64)
    frameBackupSourceTop.pack(expand=TRUE,fill=X,padx=4,pady=4)

    frameBackupSourceBottom = ctk.CTkFrame(frameBackup1,height=64)
    frameBackupSourceBottom.pack(expand=TRUE,fill=X,padx=4,pady=4)

    ### Top ###
    SourceNameLable = ctk.CTkLabel(frameBackupSourceTop,text=plan_name,font=("ROBOTO",32))
    SourceNameLable.pack(padx=16,pady=4)

    ### Ready Target ###
    ExistDir = os.path.exists(pd["sourceDir"])
    if(ExistDir == True):
        readyColor = "green"
    else:   
        readyColor = "red"

    SourceReadyFrame = ctk.CTkFrame(frameBackupSourceBottom,height=12,width=12,fg_color=readyColor,corner_radius=100)
    SourceReadyFrame.pack(side=LEFT,padx=8) 

    SourcePathLable = ctk.CTkLabel(frameBackupSourceBottom,text=pd["sourceDir"],font=("ROBOTO",16))
    SourcePathLable.pack(side=LEFT,padx=2)


    OpenSourceButton = ctk.CTkButton(frameBackupSourceBottom,text="Open Source",command=lambda pd=pd :[ logIt(str("Open Source | "+pd["sourceDir"])),openDirectory(pd["sourceDir"])],font=("ROBOTO",16),height=24,width=24)
    OpenSourceButton.pack(side=RIGHT,padx=4,pady=4)

    ### Multi Frame ### 
    frameBackupTarget = ctk.CTkFrame(frameBackup,height=64)
    frameBackupTarget.pack(expand=TRUE,fill=X,padx=4,pady=4)


    ii = 0
    for x in range(targetDirCount):
        td1 = pd["targetDir"][ii]["path"]
        pdsd1 = pd["sourceDir"]
        name = pdsd1.split("\\")[-1]
        pn = plan_name


        ### Ready Target ###
        ExistDir1 = os.path.exists(str(td1))
        if(ExistDir1 == True):
            readyColor1 = "green"
        else:   
            readyColor1 = "red"


        def countFolders(td1):
            ExistDir12 = os.path.exists(str(td1))
            if(ExistDir12 == True):
                #### count folders ####
                entries = os.listdir(td1)
                v = str(sum(os.path.isdir(os.path.join(td1, entry)) for entry in entries) +1 )
            return v 
        
        ### Frame ###
        frameTarget = ctk.CTkFrame(frameBackupTarget,height=32)
        frameTarget.pack(expand=TRUE,fill=X,padx=2,pady=4)                     

        ### Top ###
        frameTargetTop = ctk.CTkFrame(frameTarget,height=32)
        frameTargetTop.pack(expand=TRUE,fill=X,padx=2,pady=2)
        

        TargetReadyFrame = ctk.CTkFrame(frameTargetTop,height=12,width=12,fg_color=readyColor1,corner_radius=100)
        TargetReadyFrame.pack(side=LEFT,padx=8) 

        TargetNameLable = ctk.CTkLabel(frameTargetTop,text=pd["targetDir"][ii]["name"],font=("ROBOTO",16))
        TargetNameLable.pack(side=LEFT,padx=2) 

        TargetUpdateDateLable = ctk.CTkLabel(frameTargetTop,text="03.08.2024",font=("ROBOTO",16))
        TargetUpdateDateLable.pack(side=LEFT,padx=8) 

        RestoreButton = ctk.CTkButton(frameTargetTop,text="Restore",font=("ROBOTO",16),height=24,width=24)
        RestoreButton.pack(side=RIGHT,padx=4,pady=4)

        BackupButton = ctk.CTkButton(frameTargetTop,text="Backup",command=lambda td1=td1,pdsd1=pdsd1,name=name,pn=pn:[ logIt(str("Backup | "+pn+" > "+td1)),backup(pdsd1,td1,name,countFolders(td1))],font=("ROBOTO",16),height=24,width=24)
        BackupButton.pack(side=RIGHT,padx=4,pady=4)

        ### Bottom ### 
        frameTargetBottom = ctk.CTkFrame(frameTarget,height=32)
        frameTargetBottom.pack(expand=TRUE,fill=X,padx=2,pady=2)        
        
        TargetLable = ctk.CTkLabel(frameTargetBottom,text=td1,font=("ROBOTO",16))
        TargetLable.pack(side=LEFT,padx=8)

        OpenTargetButton = ctk.CTkButton(frameTargetBottom,text="Open Target",command=lambda td1=td1 :[ logIt(str("Open Target > "+td1)),openDirectory(td1)],font=("ROBOTO",16),height=16,width=24)    
        OpenTargetButton.pack(side=RIGHT,padx=4,pady=4)

        ii += 1 



frameBottom = ctk.CTkFrame(root,height=32)
frameBottom.pack(fill=X)


logLable = ctk.CTkLabel(frameBottom,textvariable=endlog,font=("ROBOTO",16))
logLable.pack(side=LEFT,padx=16)

root.mainloop()

