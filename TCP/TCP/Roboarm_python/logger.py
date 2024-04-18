import os
import time
import datetime

class Logger():
    def __init__(self, folderPath= "C:\\Users\\lamch\\Desktop\\TCP\\TCP\\Roboarm_python\\", logPath=""):
        self.folderPath = folderPath
        self.logPath = logPath

    def log(self, message):
        Year = time.localtime().tm_year
        Month = time.localtime().tm_mon
        Day = time.localtime().tm_mday

        self.logPath=self.folderPath + str(Year) + "\\" + str(Month)
        if not os.path.exists(self.logPath):
            os.makedirs(self.logPath)

        logPath = os.path.join(self.logPath, str(Day) + "_log.txt")
        with open(logPath, "a") as logWriter:
            logWriter.write(datetime.datetime.now().strftime("%Y-%m-%d %a %H:%M:%S   ") + message+"\n")