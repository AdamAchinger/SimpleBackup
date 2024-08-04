from tkinter import * 
import customtkinter as ctk
import json
import os
import sys
import subprocess

root = ctk.CTk()

### Version ###
toolVersion = 4.3

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
################################################################
### TOP ###
frameTop = ctk.CTkFrame(root,height=64)
frameTop.pack(fill=X)

def openConfig():
    os.system("notepad.exe "+"config.json")
def openLog():
    os.system("notepad.exe "+"log.txt")
def refresh():
    python = sys.executable
    os.execl(python, python, * sys.argv)


ConfigButton = ctk.CTkButton(frameTop,text="Open Config",command=openConfig,font=("ROBOTO",16),height=32)
ConfigButton.pack(side=LEFT,padx=4,pady=4)

LogButton = ctk.CTkButton(frameTop,text="Open Log",command=openLog,font=("ROBOTO",16),height=32)
LogButton.pack(side=LEFT,padx=4,pady=4)

RefreshButton = ctk.CTkButton(frameTop,text="Refresh",command=refresh,font=("ROBOTO",16),height=32)
RefreshButton.pack(side=LEFT,padx=4,pady=4)

frameMiddle = ctk.CTkScrollableFrame(root,height=32)
frameMiddle.pack(expand=TRUE,fill=BOTH,pady=4)


### JSON ###

with open("config.json") as config: 
    data = json.loads(config.read())

backupsCount = len(data)
i = 0 
for plan_name, plan_details in data.items():

    targetDirCount = len(plan_details["targetDir"])

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

    ### Bottom ### 

    SourcePathLable = ctk.CTkLabel(frameBackupSourceBottom,text=plan_details["sourceDir"],font=("ROBOTO",16))
    SourcePathLable.pack(side=LEFT,padx=8)


    OpenSourceButton = ctk.CTkButton(frameBackupSourceBottom,text="Open Source",font=("ROBOTO",16),height=24,width=24)
    OpenSourceButton.pack(side=RIGHT,padx=4,pady=4)

    ### Multi Frame ### 
    frameBackupTarget = ctk.CTkFrame(frameBackup,height=64)
    frameBackupTarget.pack(expand=TRUE,fill=X,padx=4,pady=2)
    i += 1 

    ii = 0 
    for x in range(targetDirCount):

        ### Frame ###
        frameTarget = ctk.CTkFrame(frameBackupTarget,height=32)
        frameTarget.pack(expand=TRUE,fill=X,padx=2,pady=2)


        ### Top ###
        frameTargetTop = ctk.CTkFrame(frameTarget,height=32)
        frameTargetTop.pack(expand=TRUE,fill=X,padx=2,pady=2)    

        TargetNameLable = ctk.CTkLabel(frameTargetTop,text=plan_details["targetDir"][ii]["name"],font=("ROBOTO",16))
        TargetNameLable.pack(side=LEFT,padx=8) 

        TargetUpdateDateLable = ctk.CTkLabel(frameTargetTop,text="03.08.2024",font=("ROBOTO",16))
        TargetUpdateDateLable.pack(side=LEFT,padx=8) 

        RestoreButton = ctk.CTkButton(frameTargetTop,text="Restore",font=("ROBOTO",16),height=24,width=24)
        RestoreButton.pack(side=RIGHT,padx=4,pady=4)

        BackupButton = ctk.CTkButton(frameTargetTop,text="Backup",font=("ROBOTO",16),height=24,width=24)
        BackupButton.pack(side=RIGHT,padx=4,pady=4)

        ### Bottom ### 

        frameTargetBottom = ctk.CTkFrame(frameTarget,height=32)
        frameTargetBottom.pack(expand=TRUE,fill=X,padx=2,pady=2)        

        TargetLable = ctk.CTkLabel(frameTargetBottom,text=plan_details["targetDir"][ii]["path"],font=("ROBOTO",16))
        TargetLable.pack(side=LEFT,padx=8)

        OpenTargetButton = ctk.CTkButton(frameTargetBottom,text="Open Target",font=("ROBOTO",16),height=16,width=24)    
        OpenTargetButton.pack(side=RIGHT,padx=4,pady=4)

        ii += 1 



frameBottom = ctk.CTkFrame(root,bg_color="white",height=32)
frameBottom.pack(fill=X)

logLable = ctk.CTkLabel(frameBottom,text="[ S:/SimpleBackup -> F:/SimpleBackup ] [Complited] ")
logLable.pack(side=LEFT,padx=4)

root.mainloop()

