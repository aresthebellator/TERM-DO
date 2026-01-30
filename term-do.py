#!/usr/bin/env python3
# ===============================================
# TERM-DO
# Copyright (c) 2025 aresthebellator
# Version: 2.0 
# ===============================================
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    print("""\033[1;33m
 ███████████                                                   █████         
▒█▒▒▒███▒▒▒█                                                  ▒▒███          
▒   ▒███  ▒   ██████  ████████  █████████████               ███████   ██████ 
    ▒███     ███▒▒███▒▒███▒▒███▒▒███▒▒███▒▒███  ██████████ ███▒▒███  ███▒▒███
    ▒███    ▒███████  ▒███ ▒▒▒  ▒███ ▒███ ▒███ ▒▒▒▒▒▒▒▒▒▒ ▒███ ▒███ ▒███ ▒███
    ▒███    ▒███▒▒▒   ▒███      ▒███ ▒███ ▒███            ▒███ ▒███ ▒███ ▒███
    █████   ▒▒██████  █████     █████▒███ █████           ▒▒████████▒▒██████ 
   ▒▒▒▒▒     ▒▒▒▒▒▒  ▒▒▒▒▒     ▒▒▒▒▒ ▒▒▒ ▒▒▒▒▒             ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  
                                                                             
    \033[0m""")

def MenuProject():
    clear_screen()
    welcome()
    print("\033[1;34m----------------------------\033[0m")
    print("\033[1;36m[1]\033[0m Create a project ")
    print("\033[1;36m[2]\033[0m Add task -- Remove task ")
    print("\033[1;36m[3]\033[0m Edit a project ")
    print("\033[1;36m[4]\033[0m View a project ")
    print("\033[1;36m[5]\033[0m Remove a project ")
    print("\033[1;31m[B]\033[0m Back to main menu ")
    return input("\033[1;33m==> \033[0m")

def MenuActivity():
    clear_screen()
    welcome()
    print("\033[1;36m[1]\033[0m Add activity ")
    print("\033[1;36m[2]\033[0m Edit activity ")
    print("\033[1;36m[3]\033[0m Remove activity ")
    print("\033[1;36m[4]\033[0m View all activities ")
    print("\033[1;31m[B]\033[0m Back to main menu ")
    return input("\033[1;33m==> \033[0m")

def CreateProject():
    clear_screen()
    welcome()
    print("\033[1;36mCREATE PROJECT\033[0m")
    nameF = input("Write here the name of folder you want to create or press 'b' for back: ")
    if nameF.lower() == 'b':
        return
    if os.path.exists(nameF):
        print("\033[1;31mYour folder is already exists.\033[0m")
        time.sleep(1)
        return
    else:
        print("\033[1;36mWrite here the position you want the folder is gonna be placed or press 'b' for back:\033[0m")
        print("[1] Documents")
        print("[2] Desktop")
        print("\033[1;31m[B] Back\033[0m")
        p = input("\033[1;33m==> \033[0m")
        if p.lower() == 'b':
            return

        if p == "1":
            os.chdir(os.path.expanduser("~/Documents"))
            os.mkdir(nameF)
            os.chdir(nameF)
        elif p == "2":
            os.chdir(os.path.expanduser("~/Desktop"))
            os.mkdir(nameF)
            os.chdir(nameF)
        else:
            print("\033[1;31mYou doesn't choose a correct option. Retry!\033[0m")
            time.sleep(1)
            return

        print(f"\033[1;32m{nameF} created succesfully\033[0m")
        
        namefiletxt = input("Write here the name of your file txt: ")
        filepath = namefiletxt + ".txt"
        with open(filepath,'w') as f:
            pass
        print(f"\033[1;32m{namefiletxt} Created!\033[0m")
        print("\033[1;36mNow you can choose EDIT PROJECT to add tasks.\033[0m")
        time.sleep(2)

def AddORemoveTask():
    clear_screen()
    welcome()
    print("\033[1;36mCHOOSE:\033[0m")
    print("[1] ADD TASK")
    print("[2] REMOVE TASK")
    choose = input("\033[1;33m==> \033[0m")
    
    if choose == '1':
        print("\033[1;36mADD TASK\033[0m")
        print("[1] Documents ")
        print("[2] Desktop ")
        nameP = input("Write here the position of your folder or press 'b' for back: ")
        if nameP.lower() == 'b':
            return
        elif nameP == '1':
            os.chdir(os.path.expanduser("~/Documents"))
            nameFolder = input("Write here the name of your folder: ")
            if not os.path.exists(nameFolder):
                print("\033[1;31mFOLDER NOT FOUND\033[0m")
                time.sleep(1)
                return
            os.chdir(nameFolder)
            nameFile = input("Write here the name of your file: ")
            filepath = nameFile + ".txt"
            if os.path.exists(filepath):
                with open(filepath,'a') as f:
                    while True:
                        nameT = input("Write the task here: ")
                        f.write(f"\033[1;32mTASK:\033[0m   {nameT}\n")
                        ans = input("Do you want add new task? (y/n): ")
                        if ans.lower() == 'n':
                            print("\033[1;36mTasks added!\033[0m")
                            time.sleep(1)
                            break
            else:
                print("\033[1;31mPROJECT NAME INVALID\033[0m")
                time.sleep(2)

        elif nameP == '2':
            os.chdir(os.path.expanduser("~/Desktop"))
            nameFolder = input("Write here the name of your folder: ")
            if not os.path.exists(nameFolder):
                print("\033[1;31mFOLDER NOT FOUND\033[0m")
                time.sleep(1)
                return
            os.chdir(nameFolder)
            nameFile = input("Write here the name of your file: ")
            filepath = nameFile + ".txt"
            if os.path.exists(filepath):
                with open(filepath,'a') as f:
                    while True:
                        nameT = input("Write the task here: ")
                        f.write(f"\033[1;32mTASK:\033[0m   {nameT}\n")
                        ans = input("Do you want add new task? (y/n): ")
                        if ans.lower() == 'n':
                            print("\033[1;36mTasks added!\033[0m")
                            time.sleep(1)
                            break
            else:
                print("\033[1;31mPROJECT NAME INVALID\033[0m")
                time.sleep(2)

    elif choose == '2':
        print("\033[1;36mREMOVE TASK\033[0m")
        print("[1] Documents")
        print("[2] Desktop")
        nameP = input("Write here the position of your folder or press 'b' for back: ")
        if nameP.lower() == 'b':
            return
        elif nameP == '1':
            os.chdir(os.path.expanduser("~/Documents"))
            nameFolder = input("Write here the name of your folder: ")
            os.chdir(nameFolder)
            nameFile = input("Write here the name of your file: ")
            filepath = nameFile + ".txt"
            if os.path.exists(filepath):
                with open(filepath,'r') as file:
                    lines = file.readlines()
                if not lines:
                    print("\033[1;33mFile is empty.\033[0m")
                else:
                    print("\n\033[1;34mCurrent tasks:\033[0m\n")
                    for i,line in enumerate(lines,start=1):
                        print(f"[{i}] {line.strip()}")
                    task_remove = input("\nKeyword of task to remove: ").strip().lower()
                    lines_to_keep = []
                    removed_task = None
                    for line in lines:
                        if task_remove in line.lower() and removed_task is None:
                            removed_task = line.strip()
                            continue
                        lines_to_keep.append(line)
                    with open(filepath,'w') as file:
                        file.writelines(lines_to_keep)
                    if removed_task:
                        print(f"\n\033[1;31mRemoved task:\033[0m {removed_task}")
                        print(f"\033[1;32mDone. File updated.\033[0m")
                    else:
                        print("\033[1;33mNo matching task found.\033[0m")
            time.sleep(2)
        
        elif nameP == '2':
            os.chdir(os.path.expanduser("~/Desktop"))
            nameFolder = input("Write here the name of your folder: ")
            os.chdir(nameFolder)
            nameFile = input("Write here the name of your file: ")
            filepath = nameFile + ".txt"
            if os.path.exists(filepath):
                with open(filepath,'r') as file:
                    lines = file.readlines()
                if not lines:
                    print("\033[1;33mFile is empty.\033[0m")
                else:
                    print("\n\033[1;34mCurrent tasks:\033[0m\n")
                    for i,line in enumerate(lines,start=1):
                        print(f"[{i}] {line.strip()}")
                    task_remove = input("\nKeyword of task to remove: ").strip().lower()
                    lines_to_keep = []
                    removed_task = None
                    for line in lines:
                        if task_remove in line.lower() and removed_task is None:
                            removed_task = line.strip()
                            continue
                        lines_to_keep.append(line)
                    with open(filepath, "w") as file:
                        file.writelines(lines_to_keep)
                    if removed_task:
                        print(f"\n\033[1;31mRemoved task:\033[0m {removed_task}")
                        print("\033[1;32mDone. File updated.\033[0m")
                    else:
                        print("\033[1;33mNo matching task found.\033[0m")
            time.sleep(2)

def Add():
    running_add = True
    while running_add:
        clear_screen()
        welcome()
        print("\n\033[1;36mADD ACTIVITY\033[0m")
        print("Write here the position of your folder or press 'b' to go back: ")
        print("[1] Documents")
        print("[2] Desktop")
        choose = input("\033[1;33m==> \033[0m")
        if choose.lower() == 'b':
            return
        elif choose == '1':
            os.chdir(os.path.expanduser("~/Documents"))
            nameF = input("Write here the name of your folder: ")
            os.chdir(nameF)
            data = input("DAY (ex: 15_12_25): ")
            filepath = data + ".txt"
            if not os.path.exists(filepath):
                print(f"\033[1;31mError, can't find the day: {data}\033[0m")
                create = input("Do you want to create this day? (y/n): ")
                if create.lower() == 'y':
                    with open(filepath,'w') as f: pass
                    print(f"\033[1;32m{data} Created!\033[0m")
                    time.sleep(1)
                else: continue
            adding_items = True
            while adding_items:
                clear_screen()
                print(f"\033[1;36m--- Adding to {data} ---\033[0m")
                new_activity = input("Write the activity: ")
                req_time = input("Do you have a specific time for this activity? (y/n): ")
                if req_time.lower() == 'y':
                    time_activity = input("At: ")
                else:
                    time_activity = "NO TIME"
                with open(filepath,'a') as f:
                    f.write(f"\033[1;32mACTIVITY:\033[0m {new_activity} | \033[1;34mTIME:\033[0m {time_activity}\n")
                print("\033[1;32mActivity added!\033[0m")
                again = input("\nDo you want to add another activity to THIS day? (y/n): ")
                if again.lower() != 'y':
                    adding_items = False
            print("\n[1] Change day / [2] Back to menu")
            choice = input("\033[1;33m==> \033[0m")
            if choice != '1': running_add = False
        
        elif choose == '2':
            os.chdir(os.path.expanduser("~/Desktop"))
            nameF = input("Write here the name of your folder: ")
            os.chdir(nameF)
            data = input("DAY (ex: 25_12_25): ")
            filepath = data+".txt"
            if not os.path.exists(filepath):
                print(f"\033[1;31mError, can't find the day: {data}\033[0m")
                create = input("Do you want to create this day? (y/n): ")
                if create.lower() == 'y':
                    with open(filepath,'w') as f: pass
                    print(f"\033[1;32m{data} Created!\033[0m")
                    time.sleep(1)
                else: continue
            adding_items = True
            while adding_items:
                clear_screen()
                print(f"\033[1;36m--- Adding to {data} ---\033[0m")
                new_activity = input("Write the activity: ")
                req_time = input("Do you have specific time for this activity? (y/n): ")
                if req_time.lower() == 'y':
                    time_activity = input("At: ")
                else:
                    time_activity = "NO TIME"
                with open(filepath,'a') as f:
                    f.write(f"\033[1;32mACTIVITY:\033[0m {new_activity} | \033[1;34mTIME:\033[0m {time_activity}\n")
                print("\033[1;32mActivity added! \033[0m")
                again = input("\nDo you want to add another activity THIS day? (y/n): ")
                if again.lower() != 'y':
                    adding_items = False
            print("\n[1] Change day / [2] Back to menu")
            choice = input("\033[1;33m==> \033[0m")
            if choice != '1': running_add = False

def EditProject():
    clear_screen()
    welcome()
    print("\033[1;36mEDIT PROJECT\033[0m")
    print("Write here the position of your folder or press 'b' to go back: ")
    print("[1] Documents")
    print("[2] Desktop")
    choose = input("\033[1;33m==> \033[0m")
    if choose.lower() == 'b':
        return
    elif choose == '1':
        os.chdir(os.path.expanduser("~/Documents"))
        nameF = input("Write here the name of your folder: ")
        os.chdir(nameF)
        nameproject = input("Enter the name of the project or press 'b' for back: ")
        if nameproject.lower() == 'b': return
        filepath = nameproject + ".txt"
        if os.path.exists(filepath):
            with open(filepath,'r') as file:
                lines = file.readlines()
            if not lines:
                print(f"\033[1;33mThe Project {filepath} is empty. \033[0m")
                add = input("Do you want add something? (y/n): ")
                if add.lower() == 'y':
                    while True:
                        new_task = input("Enter the new task: ")
                        with open(filepath,'a') as file:
                            file.write(f"\033[1;32mTASK:\033[0m {new_task}\n")
                        ans = input("Do you want add new task? (y/n): ")
                        if ans.lower() == 'n': break
            else:
                print("\n\033[1;34m### YOUR TASKS ###\033[0m")
                for i, line in enumerate(lines):
                    print(f"[{i+1}] {line.strip()}")
                try:
                    line_number = int(input("\nEnter the number of the activity to modify: "))
                    if 1 <= line_number <= len(lines):
                        new_task = input("Write here the tasks: ")
                        lines[line_number-1] = f"\033[1;32mTASK:\033[0m {new_task}\n"
                        with open(filepath,'w') as file:
                            file.writelines(lines)
                        print("\033[1;32mUpdated!\033[0m")
                except: print("\033[1;31mInvalid input\033[0m")
        else: print("\033[1;31mFile not found\033[0m")
        time.sleep(2)
    elif choose == '2':
        os.chdir(os.path.expanduser("~/Desktop"))
        nameF = input("Write here the name of your folder: ")
        os.chdir(nameF)
        nameproject = input("Enter the name of the project or press 'b' for back: ")
        if nameproject.lower() == 'b': return
        filepath = nameproject + ".txt"
        if os.path.exists(filepath):
            with open(filepath,'r') as file:
                lines = file.readlines()
            if not lines:
                print(f"\033[1;33mThe Project {filepath} is empty. \033[0m")
                add = input("Do you want add something? (y/n): ")
                if add.lower() == 'y':
                    while True:
                        new_task = input("Enter the new task: ")
                        with open(filepath,'a') as file:
                            file.write(f"\033[1;32mTASK:\033[0m {new_task}\n")
                        ans = input("Do you want add new task? (y/n): ")
                        if ans.lower() == 'n': break
            else:
                print("\n\033[1;34m### YOUR TASKS ###\033[0m")
                for i, line in enumerate(lines):
                    print(f"[{i+1}] {line.strip()}")
                try:
                    line_number = int(input("\nEnter the number of the activity to modify: "))
                    if 1 <= line_number <= len(lines):
                        new_task = input("Write here the tasks: ")
                        lines[line_number-1] = f"\033[1;32mTASK:\033[0m {new_task}\n"
                        with open(filepath,'w') as file:
                            file.writelines(lines)
                        print("\033[1;32mUpdated!\033[0m")
                except: print("\033[1;31mInvalid input\033[0m")
        else: print("\033[1;31mFile not found\033[0m")
        time.sleep(2)

def Edit():
    clear_screen()
    welcome()
    print("\033[1;36mEDIT ACTIVITY\033[0m")
    print("[1] Documents | [2] Desktop")
    choose = input("\033[1;33m==> \033[0m")
    if choose.lower() == 'b': return
    elif choose == '1':
        os.chdir(os.path.expanduser("~/Documents"))
        nameF = input("Write here the name of your folder: ")
        os.chdir(nameF)
        dateEdit = input("Write here the DATE (ex: 15_12_25) or 'b' for back: ")
        filepath = dateEdit + ".txt"
        if os.path.exists(filepath):
            with open(filepath,'r') as f: lines = f.readlines()
            for i,line in enumerate(lines): print(f"[{i+1}] {line.strip()}")
            try:
                num = int(input("\nNumber to modify: "))
                new_a = input("New activity: ")
                new_t = input("New time: ")
                lines[num-1] = f"\033[1;32mACTIVITY:\033[0m {new_a} | \033[1;34mTIME:\033[0m {new_t}\n"
                with open(filepath,'w') as f: f.writelines(lines)
                print("\033[1;32mUpdated!\033[0m")
            except: print("\033[1;31mError\033[0m")
    elif choose == '2':
        os.chdir(os.path.expanduser("~/Desktop"))
        nameF = input("Write here the name of your folder: ")
        os.chdir(nameF)
        dateEdit = input("Write here the DATE (ex: 15_12_25) or 'b' for back: ")
        filepath = dateEdit + ".txt"
        if os.path.exists(filepath):
            with open(filepath,'r') as f: lines = f.readlines()
            for i,line in enumerate(lines): print(f"[{i+1}] {line.strip()}")
            try:
                num = int(input("\nNumber to modify: "))
                new_a = input("New activity: ")
                new_t = input("New time: ")
                lines[num-1] = f"\033[1;32mACTIVITY:\033[0m {new_a} | \033[1;34mTIME:\033[0m {new_t}\n"
                with open(filepath,'w') as f: f.writelines(lines)
                print("\033[1;32mUpdated!\033[0m")
            except: print("\033[1;31mError\033[0m")
    time.sleep(2)

def RemoveProject():
    clear_screen()
    welcome()
    print("\033[1;36mREMOVE YOUR PROJECT\033[0m")
    print("[1] Documents | [2] Desktop")
    choose = input("\033[1;33m==> \033[0m")
    if choose.lower() == 'b': return
    elif choose == '1':
        os.chdir(os.path.expanduser("~/Documents"))
        nameF = input("Folder: ")
        os.chdir(nameF)
        nameP = input("Project file to delete (ex: project1.txt): ")
        if input(f"Are you sure? (y/n): ").lower() == 'y':
            if os.path.exists(nameP): os.remove(nameP)
            print("\033[1;31mProject removed\033[0m")
    elif choose == '2':
        os.chdir(os.path.expanduser("~/Desktop"))
        nameF = input("Folder: ")
        os.chdir(nameF)
        nameP = input("Project file to delete (ex: project1.txt): ")
        if input(f"Are you sure? (y/n): ").lower() == 'y':
            if os.path.exists(nameP): os.remove(nameP)
            print("\033[1;31mProject removed\033[0m")
    time.sleep(2)

def Remove():
    clear_screen()
    welcome()
    print("\033[1;36mREMOVE YOUR ACTIVITY\033[0m")
    print("[1] Documents | [2] Desktop")
    choose = input("\033[1;33m==> \033[0m")
    if choose.lower() == 'b': return
    elif choose == '1':
        os.chdir(os.path.expanduser("~/Documents"))
        nameF = input("Folder: ")
        os.chdir(nameF)
        data = input("DATE to clean: ")
        filepath = data + ".txt"
        if os.path.exists(filepath):
            with open(filepath,'r') as f: lines = f.readlines()
            for i, l in enumerate(lines): print(f"[{i+1}] {l.strip()}")
            kw = input("Keyword of activity to remove: ")
            lines = [l for l in lines if kw.lower() not in l.lower()]
            with open(filepath,'w') as f: f.writelines(lines)
            print("\033[1;32mDone. File updated.\033[0m")
    elif choose == '2':
        os.chdir(os.path.expanduser("~/Desktop"))
        nameF = input("Folder: ")
        os.chdir(nameF)
        data = input("DATE to clean: ")
        filepath = data + ".txt"
        if os.path.exists(filepath):
            with open(filepath,'r') as f: lines = f.readlines()
            for i, l in enumerate(lines): print(f"[{i+1}] {l.strip()}")
            kw = input("Keyword of activity to remove: ")
            lines = [l for l in lines if kw.lower() not in l.lower()]
            with open(filepath,'w') as f: f.writelines(lines)
            print("\033[1;32mDone. File updated.\033[0m")
    time.sleep(2)

def viewP():
    clear_screen()
    welcome()
    print("\033[1;36mVIEW PROJECT\033[0m")
    print("[1] Documents | [2] Desktop")
    choose = input("\033[1;33m==> \033[0m")
    if choose == '1':
        os.chdir(os.path.expanduser("~/Documents"))
        nameF = input("Folder: ")
        os.chdir(nameF)
        nameP = input("Project name (without .txt): ")
        filepath = nameP + ".txt"
        if os.path.exists(filepath):
            print(f"\n\033[1;34m--- Tasks for {nameP} ---\033[0m")
            with open(filepath,'r') as f: print(f.read() or "\033[1;31mEmpty\033[0m")
        else: print("\033[1;31mNot found\033[0m")
    elif choose == '2':
        os.chdir(os.path.expanduser("~/Desktop"))
        nameF = input("Folder: ")
        os.chdir(nameF)
        nameP = input("Project name (without .txt): ")
        filepath = nameP + ".txt"
        if os.path.exists(filepath):
            print(f"\n\033[1;34m--- Tasks for {nameP} ---\033[0m")
            with open(filepath,'r') as f: print(f.read() or "\033[1;31mEmpty\033[0m")
        else: print("\033[1;31mNot found\033[0m")
    input("\nPress Enter...")

def View():
    clear_screen()
    welcome()
    print("\033[1;36mVIEW ACTIVITY\033[0m")
    print("[1] Documents | [2] Desktop")
    choose = input("\033[1;33m==> \033[0m")
    if choose == '1':
        os.chdir(os.path.expanduser("~/Documents"))
        nameF = input("Folder: ")
        os.chdir(nameF)
        date = input("Date: ")
        filepath = date + ".txt"
        if os.path.exists(filepath):
            print(f"\n\033[1;34m--- Activities for {date} ---\033[0m")
            with open(filepath,'r') as f: print(f.read() or "\033[1;31mEmpty\033[0m")
        else: print("\033[1;31mNot found\033[0m")
    elif choose == '2':
        os.chdir(os.path.expanduser("~/Desktop"))
        nameF = input("Folder: ")
        os.chdir(nameF)
        date = input("Date: ")
        filepath = date + ".txt"
        if os.path.exists(filepath):
            print(f"\n\033[1;34m--- Activities for {date} ---\033[0m")
            with open(filepath,'r') as f: print(f.read() or "\033[1;31mEmpty\033[0m")
        else: print("\033[1;31mNot found\033[0m")
    input("\nPress Enter...")

def main():
    while True:
        clear_screen()
        welcome()
        print("\033[1;36m[A]\033[0m Activity mode")
        print("\033[1;36m[P]\033[0m Project mode")
        print("\033[1;31m[E] Exit\033[0m\n")
        choice_type = input("\033[1;33m==> \033[0m").lower()
        if choice_type == 'a':
            choice = MenuActivity()
            if choice == '1': Add()
            elif choice == '2': Edit()
            elif choice == '3': Remove()
            elif choice == '4': View()
        elif choice_type == 'p':
            choice = MenuProject()
            if choice == '1': CreateProject()
            elif choice == '2': AddORemoveTask()
            elif choice == '3': EditProject()
            elif choice == '4': viewP()
            elif choice == '5': RemoveProject()
        elif choice_type == 'e':
            print("\033[1;31mProgram terminated!\033[0m")
            time.sleep(1)
            break
        else:
            print("\033[1;31mInvalid Option!\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    main()