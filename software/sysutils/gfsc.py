# check the filesystem

from pathlib import Path as path

def onExecute(args: list):
    # Use filesystem structure
    has_system_dir = False
    has_usr_dir = False
    has_scripts_dir = False
    has_ext_dir = False
    has_usr_src = False

    if (path('system').exists()):
        has_system_dir = True
    if (path('usr').exists()):
        has_usr_dir = True
    if (path('usr/src').exists()):
        has_usr_src = True
    if (path('scripts').exists()):
        has_scripts_dir = True
    if (path('ext').exists()):
        has_ext_dir = True
    
    if (has_usr_dir == True 
        and has_system_dir == False
        and has_usr_src == False
        and has_ext_dir == False
        and has_scripts_dir == False):
        print("the filesystem is the U86 (Unix 86) format.")
    elif (has_usr_dir == False 
        and has_system_dir == True
        and has_usr_src == False
        and has_ext_dir == False
        and has_scripts_dir == False):
        print("the filesystem is the FS64 (Free System 64) format.")
    elif (has_usr_dir == True 
        and has_system_dir == True
        and has_usr_src == False
        and has_ext_dir == False
        and has_scripts_dir == False):
        print("the filesystem is the FSU86 (Free System + Unix 86) format.")
    elif (has_usr_dir == True 
        and has_system_dir == False
        and has_usr_src == True
        and has_ext_dir == (True or False)
        and has_scripts_dir == False):
        print("the filesystem is the U86R (Unix 86 Reduced) format.")
    elif (has_usr_dir == False 
        and has_system_dir == False
        and has_usr_src == False
        and has_ext_dir == False
        and has_scripts_dir == True):
        print("the filesystem is the SW12 (SnarlWin 12) format.")
    

