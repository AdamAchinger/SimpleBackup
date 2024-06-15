from tkinter import *
import customtkinter as ctk
import os
import sys
import pathlib 

def configButton(targetName):
    import customtkinter as ctk

    root = ctk.CTkToplevel()
    root.grab_set()

    root.title(targetName+" Config")
    #root.iconbitmap('S:\GitHub\SimpleBackup\img\AA_icon.ico')
    root.resizable(False,False)

    #####
    # application dimensions
    appWidth = 350
    appHeight = 100
    # get windows screan width and height
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    # center position 
    appXpos = int((screenWidth/2)-(appWidth/2))
    appYpos = int((screenHeight/2)-(appHeight/2))
    # create app window 
    root.geometry(f'{appWidth}x{appHeight}+{appXpos}+{appYpos}')
    #####    
      
    infoLable4 = ctk.CTkLabel(root,text="Name:",font=("ROBOTO",18))
    infoLable4.grid(row=0,column=0,padx=12,pady=2,sticky=E)
    infoLable5 = ctk.CTkLabel(root,text="Target:",font=("ROBOTO",18))
    infoLable5.grid(row=1,column=0,padx=12,pady=2,sticky=E)
    infoLable6 = ctk.CTkLabel(root,text="Note:",font=("ROBOTO",18))
    infoLable6.grid(row=2,column=0,padx=12,pady=2,sticky=E)

    infoInput44 = ctk.CTkEntry(root,placeholder_text="Name",font=("ROBOTO",18),width=250)
    infoInput44.grid(row=0,column=1,padx=12,pady=2,sticky=W)
    infoInput55 = ctk.CTkEntry(root,placeholder_text="Target Directory",font=("ROBOTO",18),width=250)
    infoInput55.grid(row=1,column=1,padx=12,pady=2,sticky=W)
    infoInput66 = ctk.CTkEntry(root,placeholder_text="Note",font=("ROBOTO",18),width=250)
    infoInput66.grid(row=2,column=1,padx=12,pady=2,sticky=W)

    root.mainloop()




def targetWidget(root,frameRight,targetDir,targetNote,targetName):
    import os

    isDirValid = os.path.exists(targetDir)
    
    print(targetDir)
    print(isDirValid)

    if(isDirValid == True):
        targetState = "Ready"
        targetStateColor = "green"
    else:
        targetState = "Unready"
        targetStateColor = "red"
    if(targetDir == ""):
        targetState = "Unset"
        targetStateColor = "orange"

    if(targetName==""):
        targetName = "Untitled"


    frameRT = Frame(frameRight,bg="blue",width=400,height=225)
    frameRT.pack(padx=3,pady=6,side=TOP,fill=BOTH)
    frameRT.pack_propagate(False)


    frameRTT1 = Frame(frameRT,bg="black",width=400,height=50)
    frameRTT1.pack(padx=3,pady=1,side=TOP,fill=X)
    frameRTT1.grid_propagate(False)


    infoLable7 = ctk.CTkLabel(frameRTT1,text=targetName,font=("ROBOTO",20))
    infoLable7.pack(padx=12,pady=2,side=LEFT)

    infoLable71 = ctk.CTkLabel(frameRTT1,text=targetState,font=("ROBOTO",20),text_color=targetStateColor)
    infoLable71.pack(padx=2,pady=2,side=LEFT)

    infoLable711 = ctk.CTkLabel(frameRTT1,text="Note: "+targetNote,font=("ROBOTO",20))
    infoLable711.pack(padx=12,pady=2,side=LEFT)


    frameRTT2 = Frame(frameRT,bg="black",width=400,height=35)
    frameRTT2.pack(padx=3,pady=1,side=TOP,fill=X)
    frameRTT2.pack_propagate(False)

    infoLable77 = ctk.CTkLabel(frameRTT2,text=targetDir,font=("ROBOTO",18))
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

    infoLable11 = ctk.CTkLabel(frameRTB,text="231",font=("ROBOTO",18))
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

    ResreshButton1 = ctk.CTkButton(frameRTBB,text="Resresh",font=("ROBOTO",22),width=70,height=35)
    ResreshButton1.pack(padx=6,pady=6,side=LEFT)

    configButton1 = ctk.CTkButton(frameRTBB,text="Config",command=lambda: configButton(targetName),font=("ROBOTO",22),width=70,height=35)
    configButton1.pack(padx=6,pady=6,side=LEFT)