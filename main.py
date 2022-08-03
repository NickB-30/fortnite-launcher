import sys
import os
import subprocess
from pyinjector import inject
import psutil
import time

def start():
    launch = input("[1] - launch\n[2] - add fortnite build\n[3] - remove fortnite build\n[4] - set console dll path\n[5] - set fiddler path\n[6] - quit\n")
    # add builds
    if launch == "2":
        txt = open("location.txt", "a")
        loc = input("Game Location: ")
        txt.write(f"\n{loc}")
        print("Added Directory")
        start()
    # launch game
    elif launch == "1":
        with open('location.txt') as txt:
            locations = []
            i = 1
            for line in txt:
                print(f"{i}: {line}")
                i+=1
                locations.append(line)   
        number = int(input("Launch: "))
        build = locations[number-1]
        location = build+"\Launcher.bat"
        print(locations[number-1])
        print("Opening LawinServer")
        os.chdir(r'C:\Users\nicol\Desktop\normal-lawin\LawinServer-main')
        p = subprocess.Popen(r'C:\Users\nicol\Desktop\normal-lawin\LawinServer-main\start.bat')
        print("Opening Fiddler")
        p = subprocess.Popen(r'C:\Users\nicol\AppData\Local\Programs\Fiddler\Fiddler.exe')
        os.chdir(build)
        p = subprocess.Popen(location, creationflags=subprocess.CREATE_NEW_CONSOLE)
        print("Launching Fortnite")
        time.sleep(48)
        injected = False
        while injected == False:
            process_name = "Fortnite"
            pid = None
            for proc in psutil.process_iter():
                if process_name in proc.name():
                    pid = proc.pid
            if pid != None:
                inject(pid, r'C:\Users\nicol\Desktop\UniversalFNConsole.dll')
                injected = True
                print("Injected Console DLL")
    # remove builds
    elif launch == "3":
        with open("location.txt", "r") as txt:
            i = 1
            for line in txt:
                print(f"{i}: {line}")
                i+=1 
            number = int(input("Remove: "))
        with open("location.txt", "r") as file:
            lines = file.readlines()
            x=1
            with open('location.txt', 'w') as remove:
                for line in lines:
                    if x != number:
                        remove.write(line)
                    x+=1
        start()
    # set console dll path
    elif launch == "4":
        start()
    # set fiddler.exe path
    elif launch == "5":
        start()
    # quit
    elif launch == "6":
        sys.exit
    else:
        print("Invalid Choice")
        start()        
start()