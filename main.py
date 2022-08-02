import sys
import os
import subprocess
from pyinjector import inject
import psutil
import time

launch = input("press 1 to launch 7.40, 2 to quit:\n")
if launch == "2":
    sys.exit
else:
    print("Opening LawinServer")
    os.chdir(r'C:\Users\nicol\Desktop\normal-lawin\LawinServer-main')
    p = subprocess.Popen(r'C:\Users\nicol\Desktop\normal-lawin\LawinServer-main\start.bat')
    print("Opening Fiddler")
    p = subprocess.Popen(r'C:\Users\nicol\AppData\Local\Programs\Fiddler\Fiddler.exe')
    print("Launching 7.40")
    os.chdir(r'C:\Users\nicol\Desktop\fortnite-builds\7.40\FortniteGame\Binaries\Win64')
    p = subprocess.Popen(r'C:\Users\nicol\Desktop\fortnite-builds\7.40\FortniteGame\Binaries\Win64\Launcher.bat', creationflags=subprocess.CREATE_NEW_CONSOLE)
    print("Launched 7.40")
    time.sleep(48)
    process_name = "Fortnite"
    pid = None
    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid
    inject(pid, r'C:\Users\nicol\Desktop\UniversalFNConsole.dll')
    