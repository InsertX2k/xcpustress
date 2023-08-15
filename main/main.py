"""
The main executable for xcpustress(.exe)

Copyright (C) 2023 - Ziad (Mr.X) Software

This program provides you with the capability to use it as a CLI program, which gives 
it a portable and lightweight feeling and can help you later create various wrapper GUIs 
for it.
"""
import sys, os
import subprocess
import threading
from colorama import Style, Back, Fore, init

# initializing colorama
init(autoreset=True)

# initializing application path variable
application_path = ''
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))


CLI_USAGE = """usage: xcpustress/<Executable Filename>(.exe/No extension) [stress test mode]
where:
* [stress test mode] can be any of the following:
1 -> performs a basic stress test, launches 1 instance of the stress test process, useful for very old computers with CPUs slower than 1 GHz
2 -> performs a more advanced stress test, launches 3 instances of the stress test process, useful for old computers with CPUs slower than 2 GHz
3 -> performs an even more advanced stress test, launches 5 instances of the stress test process, useful for computers aging 7 to 13 years old with CPUs faster than 2 GHz
4 -> performs an even more advanced stress test, launches 15 instances of the stress test process, useful for computers aging 5 to 10 years old with CPUs faster than 2 GHz
5 -> performs an high end stress test, launches 35 instances of the stress test process, useful for computers aging 3 to 1 year old with CPUs faster than 3 GHz
6 -> performs a high end burnin stress test, launches 50 instances of the stress test process, useful for highend computers (really high end ones)
7 -> performs the best and highest burn in tests possible, launches 150 instances of the stress test process, useful for monster PCs only! **USE WITH EXTREME CAUTION**
8 -> performs the INDESTRUCTABLE MONESTER STRESS TEST, launches 400 instances of the stress test process, useful for monster PCs only! **USE WITH EXTREME CAUTION** **MIGHT BURN YOUR CPU**

examples:
xcpustress 1
* performs a basic stress test on the processor

xcpustress 2
* performs a level two stress test on the processor

xcpustress 3
* performs a level three stress test on the processor (somewhat good for 3rd generation i3/i5/i7 Intel CPUs or older)

xcpustress 4
* performs a level four stress test on the processor (It is recommended for most processors newer than 2012)

xcpustress 5
* performs a burnin stress test on the processor (mostly recommended for most processors, including older ones, can cause overheating, but *really* stresses the processor)


"""

def launchStressInstance():
    subprocess.run(f"{application_path}\\xcpustress_rstrhost.exe", cwd=application_path, check=False)
    return


def main(args: list):
    try:
        if len(args) == 1: # no args
            print(f"{Fore.RED}error: no cli arguments passed")
            print(f"{CLI_USAGE}")
        else: 
            if str(args[1]) == "1": # perform a basic stress test, only one instance
                print(f"{Fore.YELLOW}info: performing a basic stress test, only one instance....\n\nIN CASE SOMETHING GOES WRONG KEEP A CMD WINDOW OPEN AND RUN THIS COMMAND: taskkill /f /im 'xcpustress_rstrhost.exe'")
                threading.Thread(target=launchStressInstance, name='basicstressthrd').start()
            elif str(args[1]) == "2": # perform a three instances stress test.
                print(f"{Fore.YELLOW}info: performing a level two stress test, 3 instances....\n\nIN CASE SOMETHING GOES WRONG KEEP A CMD WINDOW OPEN AND RUN THIS COMMAND: taskkill /f /im 'xcpustress_rstrhost.exe'")
                for i in range(3):
                    threading.Thread(target=launchStressInstance, name=f'stress{i}thrd').start()
            elif str(args[1]) == "3": # perform a five instances stress test.
                print(f"{Fore.YELLOW}info: performing a level three stress test, 5 instances....\n\nIN CASE SOMETHING GOES WRONG KEEP A CMD WINDOW OPEN AND RUN THIS COMMAND: taskkill /f /im 'xcpustress_rstrhost.exe'")
                for i in range(5):
                    threading.Thread(target=launchStressInstance, name=f'stress{i}thrd').start()
            elif str(args[1]) == "4": # performs a 15 instances stress test.
                print(f"{Fore.YELLOW}info: performing a level four stress test, 15 instances....\n\nIN CASE SOMETHING GOES WRONG KEEP A CMD WINDOW OPEN AND RUN THIS COMMAND: taskkill /f /im 'xcpustress_rstrhost.exe'")
                for i in range(15):
                    threading.Thread(target=launchStressInstance, name=f'stress{i}thrd').start()
            elif str(args[1]) == "5": # performs a burnin stress test, 35 instances.
                print(f"{Fore.RED}warning: performing a burnin stress test, 35 instances....\n\nIN CASE SOMETHING GOES WRONG KEEP A CMD WINDOW OPEN AND RUN THIS COMMAND: taskkill /f /im 'xcpustress_rstrhost.exe'")
                for i in range(35):
                    threading.Thread(target=launchStressInstance, name=f'stress{i}thrd').start()
            elif str(args[1]) == "6": # performs a burn-in stress test with 50 instances.
                print(f"{Fore.RED}warning: performing a burnin stress test, 50 instances....\n\nIN CASE SOMETHING GOES WRONG KEEP A CMD WINDOW OPEN AND RUN THIS COMMAND: taskkill /f /im 'xcpustress_rstrhost.exe'")
                for i in range(51):
                    threading.Thread(target=launchStressInstance, name=f'stress{i}thrd').start()
            elif str(args[1]) == "7": # performs the monster CPU stress test with 150 instances.
                print(f"{Fore.RED}warning: performing a monster burnin stress test, 150 + 10 instances....\n\nIN CASE SOMETHING GOES WRONG KEEP A CMD WINDOW OPEN AND RUN THIS COMMAND: taskkill /f /im 'xcpustress_rstrhost.exe'")
                for i in range(160):
                    threading.Thread(target=launchStressInstance, name=f'stress{i}thrd').start()
            elif str(args[1]) == "8": # performs the INDESTRUCTABLE MONESTER STRESS TEST, launches 400 instances of the stress test process
                print(f"{Fore.RED}warning: performing THE INDESTRUCTABLE MONSTER burnin stress test, 400 + 50 instances....\n\nIN CASE SOMETHING GOES WRONG KEEP A CMD WINDOW OPEN AND RUN THIS COMMAND: taskkill /f /im 'xcpustress_rstrhost.exe'")
                for i in range(450):
                    threading.Thread(target=launchStressInstance, name=f'stress{i}thrd').start()
            else: # probably user forgot what's the test mode or used switch /?
                print(f"{CLI_USAGE}")
        return None
    except KeyboardInterrupt:
        os.system("taskkill /f /im 'xcpustress_rstrhost.exe'")
        raise SystemExit(0)

if __name__ == '__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        os.system("taskkill /f /im 'xcpustress_rstrhost.exe'")
        raise SystemExit(0)