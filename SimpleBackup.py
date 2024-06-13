from tkinter import * 


root = Tk()

### Version ###
toolVersion = 2.1

root.title("Simple Backup"+" v"+str(toolVersion))
root.iconbitmap('S:\GitHub\SimpleBackup\img\AA_icon.ico')
#root.resizable(False,False)

#####
# application dimensionsń
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


bgColor = "#24292e"
fgColor = "#C0C0C0"
hlColor = "#444444"
fontSize = 11
root.config(bg=bgColor,padx=3,pady=3)

'''
backupName = "PixelProcesor"
backupMainDir = "S:\GitHub\PixelProcesor"
'''

### dif
backupPlans = ["PixelProcesor","SimpleBackup"]
backupPlansSourceDir = ["S:\GitHub\PixelProcesor","S:\GitHub\SimpleBackup"]


### TOP ###
frameTop = Frame(root,bg="black",width=400,height=50)
frameTop.pack(padx=3,pady=1,side=TOP,fill=X)

frameTT = Frame(frameTop,bg="black",width=400,height=50)
frameTT.pack(side=TOP,fill=X)
frameTT.pack_propagate(False)


##### TOPBAR BACKUP SELECTION #####
frameTTL = Frame(frameTT,bg="violet",width=300,height=50)
frameTTL.pack(padx=3,pady=3,side=LEFT)
frameTTL.pack_propagate(False)

backupSelection1 = StringVar(value="Select Backup Plan")

backupSelection = OptionMenu(frameTTL,backupSelection1,*backupPlans)
backupSelection.config(font=("ROBOTO",16))
backupSelection.pack(padx=6,pady=6)


##### TOPBAR BUTTONS #####
frameTTR = Frame(frameTT,bg="yellow",width=11700,height=50)
frameTTR.pack(padx=3,pady=3,side=LEFT,fill=X)
frameTTR.pack_propagate(False)

backupButton = Button(frameTTR,text="Backup",font=("ROBOTO",16))
backupButton.pack(padx=6,pady=6,side=LEFT)

restoreButton = Button(frameTTR,text="Restore",font=("ROBOTO",16))
restoreButton.pack(padx=6,pady=6,side=LEFT)

configButton = Button(frameTTR,text="Config",font=("ROBOTO",16))
configButton.pack(padx=6,pady=6,side=LEFT)


##### TOPBAR SELECTED DIR #####
frameTB = Frame(frameTop,bg="magenta",width=400,height=25)
frameTB.pack(padx=3,pady=3,side=BOTTOM,fill=X)
frameTB.pack_propagate(False)


backupSelectedDir = Label(frameTB,textvariable=backupSelection1,font=("ROBOTO",16))
backupSelectedDir.pack(padx=6,pady=1,side=LEFT)

### Bottom ###
frameBottom = Frame(root,bg="black",width=400,height=50)
frameBottom.pack(padx=3,pady=1,side=BOTTOM,fill=X)

frameBB = Frame(frameBottom,bg="white",width=400,height=25)
frameBB.pack(padx=3,pady=3,side=TOP,fill=X)


### Left ###
frameLeft = Frame(root,bg="black",width=400,height=appHeight)
frameLeft.pack(padx=2,pady=3,side=LEFT,fill=BOTH,expand=1)

frame1LT = Frame(frameLeft,bg="blue",width=400,height=50)
frame1LT.pack(padx=3,pady=3,side=TOP,fill=X)

frame1LB = Frame(frameLeft,bg="green",width=400,height=appHeight)
frame1LB.pack(padx=3,pady=3,side=BOTTOM,fill=BOTH,expand=1)


### Right ###
frameRight = Frame(root,bg="black",width=400,height=appHeight)
frameRight.pack(padx=2,pady=3,side=RIGHT,fill=BOTH,expand=1)

frameRT = Frame(frameRight,bg="purple",width=400,height=300)
frameRT.pack(padx=3,pady=3,side=TOP,fill=BOTH,expand=1)
frameRT.pack_propagate(False)


frameRB = Frame(frameRight,bg="orange",width=400,height=300)
frameRB.pack(padx=3,pady=3,side=BOTTOM,fill=BOTH)
frameRB.pack_propagate(False)









root.mainloop()

