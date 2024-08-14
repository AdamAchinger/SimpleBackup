import shutil

def backup(source,target):
    shutil.copytree(source,target)

x = f"S:\\sBackupSource\\Test"
y = f"S:\\sBackupTarget\\Test\\v1"
backup(x,y)