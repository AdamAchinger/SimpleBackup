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

for x in range(1):
    frameBackup = ctk.CTkFrame(frameMiddle,bg_color="red",fg_color="blue",height=256)
    frameBackup.pack(fill=X,padx=4,pady=4)

    frameBackupSource = ctk.CTkFrame(frameBackup,bg_color="blue",height=64)
    frameBackupSource.pack(expand=TRUE,fill=X,padx=4,pady=4)

    SourceNameLable = ctk.CTkLabel(frameBackupSource,text="SimpleBackup",font=("ROBOTO",24))
    SourceNameLable.pack(side=LEFT,padx=16)

    SourcePathLable = ctk.CTkLabel(frameBackupSource,text="S:/GitHub/SimpleBackup",font=("ROBOTO",16))
    SourcePathLable.pack(side=LEFT,padx=8)

    OpenSourceButton = ctk.CTkButton(frameBackupSource,text="Open Source",font=("ROBOTO",16),height=32,width=24)
    OpenSourceButton.pack(side=RIGHT,padx=4,pady=4)

    frameBackupTarget = ctk.CTkFrame(frameBackup,bg_color="green",height=64)
    frameBackupTarget.pack(expand=TRUE,fill=X,padx=4,pady=4)

    for x in range(3):
            frameBackupDeepTarget = ctk.CTkFrame(frameBackupTarget,bg_color="red",height=32)
            frameBackupDeepTarget.pack(expand=TRUE,fill=X,padx=2,pady=2)

            TargetLable = ctk.CTkLabel(frameBackupDeepTarget,text="F:/SimpleBackupTarget/SimpleBackup")
            TargetLable.pack(side=LEFT,padx=8)

            OpenTargetButton = ctk.CTkButton(frameBackupDeepTarget,text="Open Target",font=("ROBOTO",16),height=24,width=24)
            OpenTargetButton.pack(side=RIGHT,padx=4,pady=4)

            RestoreButton = ctk.CTkButton(frameBackupDeepTarget,text="Restore",font=("ROBOTO",16),height=24,width=24)
            RestoreButton.pack(side=RIGHT,padx=4,pady=4)

            BackupButton = ctk.CTkButton(frameBackupDeepTarget,text="Backup",font=("ROBOTO",16),height=24,width=24)
            BackupButton.pack(side=RIGHT,padx=4,pady=4)



    '''
    BackupButton = ctk.CTkButton(frameBackup,text="Backup",font=("ROBOTO",16),height=32,width=24)
    BackupButton.pack(side=LEFT,padx=4,pady=4)

    RestoreButton = ctk.CTkButton(frameBackup,text="Restore",font=("ROBOTO",16),height=32,width=24)
    RestoreButton.pack(side=LEFT,padx=4,pady=4)

    OpenSourceButton = ctk.CTkButton(frameBackup,text="Open Source",font=("ROBOTO",16),height=32,width=24)
    OpenSourceButton.pack(side=LEFT,padx=4,pady=4)

    OpenTargetButton = ctk.CTkButton(frameBackup,text="Open Target",font=("ROBOTO",16),height=32,width=24)
    OpenTargetButton.pack(side=LEFT,padx=4,pady=4)
    '''



frameBottom = ctk.CTkFrame(root,bg_color="white",height=32)
frameBottom.pack(fill=X)

logLable = ctk.CTkLabel(frameBottom,text="[ S:/SimpleBackup -> F:/SimpleBackup ] [Complited] ")
logLable.pack(side=LEFT,padx=4)

root.mainloop()

