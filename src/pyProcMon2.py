#!/usr/bin/python
import psutil
import datetime

# Create a list of processes, and let the user know these processes are now running

# While True: create another list of processes and check to see if they already exist in the current list
# If not, we tell the user the process was created.
# How do we check which processes have died?

#print "Running processes..."
#for proc in psutil.process_iter():
#    print "\n\nPid: {:<10s}\tProcess: {}".format(str(proc.pid), proc.name(), width=10)
#    try:
#        print "Pid: {:<10s}\tProcess: {}".format(str(proc.ppid()), proc.parent().name(), width=10)
#    except:
#        print "Parent unknown."

initialDict = dict.fromkeys(psutil.process_iter())

while True:
    secondDict = dict.fromkeys(psutil.process_iter())
    terminatedProcesses = initialDict.viewkeys() - secondDict.viewkeys()
    for dead in terminatedProcesses:
        try:
            print "\n\n[-] Terminated: Pid: {:<10s}\tProcess: {}".format(str(dead.pid), dead.name(), width=10)

        except:
            print "\n\n[-] Process terminated, but data no longer exists."
    newProcesses = secondDict.viewkeys() - initialDict.viewkeys()
    initialDict = secondDict
    for created in newProcesses:
        try:
            print "\n\n[+] Created: Pid: {:<10s}\tProcess: {}".format(str(created.pid), created.name(), width=10)
        except:
            print "\n\n[+] Process created, but data no longer exists."
        try:
            print "Command line: {}\nAbsolute path: {}\nCreation time: {}".format(
                created.cmdline(),
                created.exe(),
                datetime.datetime.fromtimestamp(created.create_time()).strftime("%Y-%m-%d %H:%M:%S"))
        except:
            print "Additional process creation data unavailable."
        try:
            print "Parent Pid: {:<10s}\tParent Process: {}".format(str(created.ppid()), created.parent().name(), width=10)
        except:
            print "Parent unknown."
        try:
            print "Process is running as {}".format(created.username())
        except:
            print "No owner information for the process is available."

