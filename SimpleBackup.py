from tkinter import * 
import customtkinter as ctk
import json
import os

root = ctk.CTk()

### Version ###
toolVersion = 4.1

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

    frameBackup1 = ctk.CTkFrame(frameBackup,bg_color="yellow",height=256)
    frameBackup1.pack(fill=X,padx=4,pady=4)

    frameBackupSourceTop = ctk.CTkFrame(frameBackup1,bg_color="blue",height=64)
    frameBackupSourceTop.pack(expand=TRUE,fill=X,padx=4,pady=4)

    frameBackupSourceBottom = ctk.CTkFrame(frameBackup1,bg_color="blue",height=64)
    frameBackupSourceBottom.pack(expand=TRUE,fill=X,padx=4,pady=4)

    ### Top ###
    SourceNameLable = ctk.CTkLabel(frameBackupSourceTop,text="SimpleBackup",font=("ROBOTO",32))
    SourceNameLable.pack(padx=16,pady=4)

    ### Bottom ### 

    SourcePathLable = ctk.CTkLabel(frameBackupSourceBottom,text="S:/GitHub/SimpleBackup",font=("ROBOTO",16))
    SourcePathLable.pack(side=LEFT,padx=8)

    OpenSourceButton = ctk.CTkButton(frameBackupSourceBottom,text="Open Source",font=("ROBOTO",16),height=24,width=24)
    OpenSourceButton.pack(side=RIGHT,padx=4,pady=4)

    ### Multi Frame ### 
    frameBackupTarget = ctk.CTkFrame(frameBackup,bg_color="green",height=64)
    frameBackupTarget.pack(expand=TRUE,fill=X,padx=4,pady=4)

    for x in range(3):
            ### Frame ###
            frameTarget = ctk.CTkFrame(frameBackupTarget,bg_color="red",height=32)
            frameTarget.pack(expand=TRUE,fill=X,padx=2,pady=2)


            ### Top ###
            frameTargetTop = ctk.CTkFrame(frameTarget,bg_color="red",height=32)
            frameTargetTop.pack(expand=TRUE,fill=X,padx=2,pady=2)    

            TargetNameLable = ctk.CTkLabel(frameTargetTop,text="Externl F:",font=("ROBOTO",16))
            TargetNameLable.pack(side=LEFT,padx=16) 

            TargetUpdateDateLable = ctk.CTkLabel(frameTargetTop,text="03.08.2024",font=("ROBOTO",16))
            TargetUpdateDateLable.pack(side=LEFT,padx=16) 

            RestoreButton = ctk.CTkButton(frameTargetTop,text="Restore",font=("ROBOTO",16),height=24,width=24)
            RestoreButton.pack(side=RIGHT,padx=4,pady=4)

            BackupButton = ctk.CTkButton(frameTargetTop,text="Backup",font=("ROBOTO",16),height=24,width=24)
            BackupButton.pack(side=RIGHT,padx=4,pady=4)

            ### Bottom ### 

            frameTargetBottom = ctk.CTkFrame(frameTarget,bg_color="red",height=32)
            frameTargetBottom.pack(expand=TRUE,fill=X,padx=2,pady=2)        

            TargetLable = ctk.CTkLabel(frameTargetBottom,text="F:/SimpleBackupTarget/SimpleBackup",font=("ROBOTO",16))
            TargetLable.pack(side=LEFT,padx=8)

            OpenTargetButton = ctk.CTkButton(frameTargetBottom,text="Open Target",font=("ROBOTO",16),height=16,width=24)
            OpenTargetButton.pack(side=RIGHT,padx=4,pady=4)





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

