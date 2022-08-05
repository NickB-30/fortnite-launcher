import sys
import os
import subprocess
from pyinjector import inject
import psutil
import time

def start():
    launch = input("[1] - launch\n[2] - add fortnite build\n[3] - remove fortnite build\n[4] - set fiddler path\n[5] - set lawin path\n[6] - quit\n")
    # add builds
    if launch == "2":
        with open("location.txt", "a") as txt:
            loc = input("Game Location: ")
            txt.write(f"\n{loc}")
            print("Added Fortnite Build")
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
        build = (locations[number-1])
        #build = build[:-1]
        print(build)
        print(locations[number-1])
        print("Opening LawinServer")
        lawinserver = ""
        with open ('lawin.txt', 'r') as lawin:
            for line in lawin:
                lawinserver+=line
        os.chdir(lawinserver)
        p = subprocess.Popen(f"{lawinserver}\start.bat")
        print("Opening Fiddler")
        os.chdir(r'C:\Users\nicol\Desktop\python\fortnite-launcher')
        fiddlerexe = ""
        with open ('fiddler.txt', 'r') as fiddler:
            for line in fiddler:
                fiddlerexe+=line
        p = subprocess.Popen(fiddlerexe)
        print(build)
        try:
            os.chdir(build)
            location = build+"\Launcher.bat"
        except:
            build = build[:-1]
            os.chdir(build)
            location = build+"\Launcher.bat"
        p = subprocess.Popen(location, creationflags=subprocess.CREATE_NEW_CONSOLE)
        print("Launching Fortnite")
        time.sleep(37)
        os.chdir(r'C:\Users\nicol\Desktop\python\fortnite-launcher')
        injected = False
        while injected == False:
            process_name = "Fortnite"
            pid = None
            while pid == None:
                for proc in psutil.process_iter():
                    if process_name in proc.name():
                        pid = proc.pid
                time.sleep(5)
                if pid != None:
                    consoledll = "UniversalFNConsole.dll"
                    print(pid, consoledll)
                    inject(pid, consoledll)
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
    # set fiddler.exe path
    elif launch == "4":
        with open('fiddler.txt', 'r+') as txt:
            fiddler = input("Fiddler Path: ")
            txt.write(fiddler)
        start()
    elif launch == "5":
        with open('lawin.txt', 'r+') as txt:
            lawin = input("LawinServer Path: ")
            txt.write(lawin)
        start()
    # quit
    elif launch == "6":
        sys.exit
    else:
        print("Invalid Choice")
        start()        
start()