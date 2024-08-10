

def logIt(function):
    with open("log.txt","a") as logFile:
        from datetime import datetime
        now = datetime.now()
        formatted_date = now.strftime('%d.%m.%Y %H:%M:%S')
        logFile.writelines(f"{formatted_date} | {function} \n")

    logFile.close()


logIt("[ SimpleBackup -> External F]")