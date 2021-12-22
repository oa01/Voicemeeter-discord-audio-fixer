import psutil
import os
import time
import plyer.platforms.win.notification
from plyer import notification


# Programm written by blockcrafter
# if you use this please leave this annotations in the code
# Discord: blockcrafter#5759
# Github: blockcrafter21

def find_process_id(process_name):
    list_with_processes = []
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
            # Check if process name contains the given name string.
            if process_name.lower() in pinfo['name'].lower():
                list_with_processes.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return list_with_processes


def main():
    print("lul")
    listOfProcessIds = find_process_id('audiodg')
    # pid = str(listOfProcessIds['pid'])
    print(listOfProcessIds)
    print(listOfProcessIds[0]['pid'])
    aud_pr_pid = listOfProcessIds[0]['pid']
    aud_pr = psutil.Process(pid=aud_pr_pid)
    aud_pr.cpu_affinity([1])
    aud_pr.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)
    print(aud_pr.nice)
    notification.notify("Voicemeeter-Discord-Fixer","The audiodg.exe was set to Cpu 2, and the Priority of the Process is HIGHER_THEN_NORMAL")


if __name__ == '__main__':
    main()
