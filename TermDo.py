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
    print("-"*28)
    print("\033[1;36m[1]\033[0m Create a project ")
    print("\033[1;36m[2]\033[0m Add task -- Remove task ")
    print("\033[1;36m[3]\033[0m Edit a project ")
    print("\033[1;36m[4]\033[0m View a project ")
    print("\033[1;36m[5]\033[0m Remove a project ")
    print("\033[1;31m[B]\033[0m Back to main menu ")
    return input("==> ")


def MenuActivity():
    clear_screen()
    welcome()
    print("\033[1;36m[1]\033 [0m Add activiy ")
    print("\033[1;36m[2]\033[0m Edit activiy ")
    print("\033[1;36m[3]\033 [0m Remove activiy ")
    print("\033[1;36m[4]\033 [0m View all activities ")
    print("\033[1;36m[B]\033 [0m Back to main menu ")
    return input("==> ")


def CreateProject():
    clear_screen()
    welcome()
    print("\033[1;36mCREATE PROJECT\033[0m")
    nameF = input("Write here the name of folder you want to create or press 'b' for back: ")
    if nameF.lower() == 'b':
        return
    if os.path.exists(nameF):
        print("Your folder is already exists.")
        return
    else:
        
        print("Write here the position you want the folder is gonna be placed or press 'b' for back: ")
        print("[1] Documents")
        print("[2] Desktop")
        print("[B] Back")
        p = input("==> ")
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
            print("You doesn't choose a correct option. Retry! ")
            

        
        
        if os.path.exists(nameF):
            print(f"{nameF} create succesfully")
        
        
        namefiletxt = input("Write here the name of your file txt: ")
        filepath = namefiletxt + ".txt"
        with open(filepath,'w') as f:
            pass
        print(f"{namefiletxt} Created!")
        print("Now you can choose EDIT PROJECT to add tasks.")
        time.sleep(1)
        
        

def AddORemoveTask():
    clear_screen()
    welcome()
    print("\033[1;36mCHOOSE:\033[0m")
    print("[1] ADD TASK")
    print("[2] REMOVE TASK")
    choose = input("==> ")
    
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
            os.chdir(nameFolder)
            nameFile = input("Write here the name of your file: ")
            filepath = nameFile + ".txt"
            if os.path.exists(filepath):
                with open(filepath,'a') as f:
                    while True:
                        nameT = input("Write the task here: ")
                        f.write(f"\033[1;32mTASK:\033[0m   {nameT}  \n")
                        choose = input("Do you want add new task? (y/n ")
                        if choose.lower() == 'n':
                            print("\033[1;36mTasks added!\033[0m")
                            time.sleep(2)
                            break
            if not os.path.exists(filepath):
                print("\033[1;31mPROJECT NAME INVALID\033[0m")
                time.sleep(2)
                return

        elif nameP == '2':
            os.chdir(os.path.expanduser("~/Desktop"))
            nameFolder = input("Write here the name of your folder: ")
            os.chdir(nameFolder)
            nameFile = input("Write here the name of your file: ")
            filepath = nameFile + ".txt"
            if os.path.exists(filepath):
                with open(filepath,'a') as f:
                    while True:
                        nameT = nameT = input("Write the task here: ")
                        f.write(f"\033[1;32mTASK:\033[0m   {nameT}   \n")
                        choose = input("Do you want add new task? (y/n): ")
                        if choose.lower() == 'n':
                            break

            if not os.path.exists(filepath):
                print("\033[1;31mPROJECT NAME INVALID\033[0m")
                time.sleep(2)
                return
    



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
                    print("File is empty.")

                else:
                    print("\nCurrent tasks:\n")
                    for i,line in enumerate(lines,start=1):
                        print(f"[{1}] {line.strip()}")

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

                        print("\nUpdated file content:\n")
                        for i,line in enumerate(lines_to_keep,start=1):
                            print(f"[{i}] {line.strip()}")
                    else:
                        print("\033[1;33mNo matching task found.\033[0m")

        
        
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
                    print("File is empty.")

                else:
                    print("\nCurrent tasks:\n")
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

                        print("\nUpdated file content:\n")
                        for i, line in enumerate(lines_to_keep, start=1):
                            print(f"[{i}] {line.strip()}")
                    else:
                        print("\033[1;33mNo matching task found.\033[0m")
                        
                    
def Add():
    running_add = True
    while running_add:
        clear_screen()
        welcome()
        print("\n\033[1;36mADD ACTIVITY\033[0m")
        print("Write here the position of your folder or press 'b' to go back: ")
        print("[1] Documents")
        print("[2] Desktop")
        choose = input("==> ")
        if choose.lower() == 'b':
            return
        elif choose == 1:
            os.chdir(os.path.expanduser("~/Documents"))
            nameF = input("Write here the name of your folder: ")
            os.chdir(nameF)
            data = input("DAY (ex: 15_12_25): ")
            filepath = data + ".txt"
            if not os.path.exists(filepath):
                print(f"\033[1;31mError, can't find the day: {data}\033[0m")
                create = input("Do you want to create this day? (y/n): ")
                if create.lower() == 'y':
                    with open(filepath,'w') as f: 
                        pass
                        print(f"{data} Created!")
                        time.sleep(1)
                else:
                    continue
                adding_items = True
                while adding_items:
                    clear_screen()
                    print(f"\033[1;36m--- Adding to {data} ---\033[0m")
                    new_activity = input("Write the activity: ")
                    req_time = input("Do you have a specific time for this activity? (y/n): ")
                    if req_time.lower() == 'y':
                        time_activity = input("At: ")
                    else:
                        time_activity = "NO TIME"

                    with open(filepath,'a') as f:
                        f.write(f"ACTIVITY:    {new_activity}       TIME:    {time_activity}\n")
                    print("\033[1;32mActivity added!\033[0m")
                    again = input("\nDo you want to add another activity to THIS day? (y/n): ")
                    if again.lower != 'y':
                        adding_items = False

                print("\n[1] Change day / [2] Back to menu")
                choice = input("==> ")
                if choiche != '1':
                    running_add = False
        
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
                    with open(filepath,'w') as f: 
                        pass
                        print(f"{data} Created!")
                        time.sleep(1)
                else:
                    continue
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
                    with open(filepath,'a')as f:
                        f.write(f"ACTIVITY:     {new_activity}     TIME:     {time_activity}\n")
                    print("\033[1;32mActivity added! \033[0m")
                    again = input("\nDo you want to add another activity THIS day? (y/n): ")
                    if again.lower() != 'y':
                        adding_items = False

                print("\n[1] Change day / [2] Back to menu")
                choice = input("==> ")
                if choice != '1':
                    running_add = False


def EditProject():
    clear_screen()
    welcome()
    print("\033[1;36mEDIT PROJECT\033[0m")
    print("Write here the position of your folder or press 'b' to go back: ")
    print("[1] Documents")
    print("[2] Desktop")
    choose = input("==> ")
    if choose.lower() == 'b':
        return
    elif choose == '1':
        os.chdir(os.path.expanduser("~/Documents"))
        nameF = input("Write here the name of your folder: ")
        os.chdir(nameF)
        nameproject = input("Enter the name of the project or press 'b' for back: ")
        if nameproject.lower() == 'b':
            return
        filepath = nameproject + ".txt"
        if os.path.exists(filepath):
            with open(filepath,'r')as file:
                lines = file.readlines()

            if not lines:
                print(f"\033[1;33mThe Project {filepath} is empty. \033[0m")
                add = input("Do you want add something? (y/n): ")
                if add.lower() == 'y':
                    while True:
                        new_task = input("Enter the new task: ")
                        with open(filepath,'w')as file:
                            file.write(f"TASK:  {new_task}\n")
                            choose = input("Do you want add new task? (y/n): ")
                            if choose.lower() == 'n':
                                print("\033[1;32mTasks added!\033[0m")
                                break
            else:
                print("\n### YOUR TASKS ###")
                for i, line in enumerate(lines):
                    print(f"[{i+1}] {line.strip()}")

                    try:
                        line_number = int(input("\nEnter the number of the activity to modify: "))
                        if 1 <= line_number <= len(lines):
                            index_to_edit = line_number - 1
                            new_task = input("Write here the tasks: ")
                            lines[index_to_edit] = f"TASK: {new_task}\n"
                            with open(filepath,'w')as file:
                                file.writelines(lines)
                            print("\033[1;32mUpdated!\033[0m")
                        else:
                            print("Invalid number")
                    except ValueError:
                        print("Invalid input")
        else:
            print("File not found")
        time.sleep(2)

    elif choose == '2':
        os.chdir(os.path.expanduser("~/Desktop"))
        nameF = input("Write here the name of your folder: ")
        os.chdir(nameF)
        nameproject = input("Enter the name of the project or press 'b' for back: ")
        if nameproject.lower() == 'b':
            return
        filepath = nameproject + ".txt"
        if os.path.exists(filepath):
            with open(filepath,'r')as file:
                lines = file.readlines()

            if not lines:
                print(f"\033[1;33mThe Project {filepath} is empty. \033[0m")
                add = input("Do you want add something? (y/n): ")
                if add.lower() == 'y':
                    while True:
                        new_task = input("Enter the new task: ")
                        with open(filepath,'w')as file:
                            file.write(f"TASK:  {new_task}\n")
                            choose = input("Do you want add new task? (y/n): ")
                            if choose.lower() == 'n':
                                print("\033[1;32mTasks added!\033[0m")
                                break
            else:
                print("\n### YOUR TASKS ###")
                for i, line in enumerate(lines):
                    print(f"[{i+1}] {line.strip()}")

                    try:
                        line_number = int(input("\nEnter the number of the activity to modify: "))
                        if 1 <= line_number <= len(lines):
                            index_to_edit = line_number - 1
                            new_task = input("Write here the tasks: ")
                            lines[index_to_edit] = f"TASK: {new_task}\n"
                            with open(filepath,'w')as file:
                                file.writelines(lines)
                            print("\033[1;32mUpdated!\033[0m")
                        else:
                            print("Invalid number")
                    except ValueError:
                        print("Invalid input")
        else:
            print("File not found")
        time.sleep(2)

def Edit():
    clear_screen()
    welcome()
    print("\033[1;36mEDIT ACTIVITY\033[0m")
    print("Write here the position of your folder or press 'b' to go back: ")
    print("[1] Documents")
    print("[2] Desktop")
    choose = input("==> ")
    if choose.lower() == 'b':
        return
    elif choose == '1':
        os.chdir(os.path.expanduser("~/Documents"))
        nameF = input("Write here the name of your folder: ")
        os.chdir(nameF)
        dateEdit = input("Write here the DATE you want to edit or press 'b' for back: ")
        if dateEdit.lower() == 'b':
            return
        filepath = dateEdit +".txt"
        if os.path.exists(filepath):
            with open(filepath,'r')as file:
                lines = file.readlines()
            if not lines:
                print(f"\033[1;33mThe file {filepath} is empty.\033[0m")
                time.sleep(2)
                return
            print("\n### Current activities ###")
            for i,line in enumerate(lines):
                print(f"[{i+1}] {line.strip()}")
            try:
                line_number = int(input("\nWrite here the number of activity to modify: "))
                if 1<= line_number <= len(lines):
                    index_to_edit = line_number - 1
                    new_activity = input("Enter new description: ")
                    new_time = input("Enter new time: ")
                    lines[index_to_edit] = f"ACTIVITY:    {new_activity}        TIME:  {new_time}\n"
                    with open(filepath, 'w') as file:
                        file.writelines(lines)
                    print("\033[1;32mUpdated!\033[0m")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Invalid input.")
        else:
            print("File not found.")
        time.sleep(2)
    elif choose == '2':
        os.chdir(os.path.expanduser("~/Desktop"))
        nameF = input("Write here the name of your folder: ")
        os.chdir(nameF)
        dateEdit = input("Write here the DATE you want to edit or press 'b' for back: ")
        if dateEdit.lower() == 'b':
            return
        filepath = dateEdit +".txt"
        if os.path.exists(filepath):
            with open(filepath,'r')as file:
                lines = file.readlines()
            if not lines:
                print(f"\033[1;33mThe file {filepath} is empty.\033[0m")
                time.sleep(2)
                return
            print("\n### Current activities ###")
            for i,line in enumerate(lines):
                print(f"[{i+1}] {line.strip()}")
            try:
                line_number = int(input("\nWrite here the number of activity to modify: "))
                if 1<= line_number <= len(lines):
                    index_to_edit = line_number - 1
                    new_activity = input("Enter new description: ")
                    new_time = input("Enter new time: ")
                    lines[index_to_edit] = f"ACTIVITY:    {new_activity}        TIME:  {new_time}\n"
                    with open(filepath, 'w') as file:
                        file.writelines(lines)
                    print("\033[1;32mUpdated!\033[0m")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Invalid input.")
        else:
            print("File not found.")
        time.sleep(2)

def RemoveProject():
    clear_screen()
    welcome()
    print("\033[1;36mREMOVE YOUR PROJECT\033[0m")
    print("[1] Documents")
    print("[2] Desktop")
    choose = input("Write here the position of your folder or press 'b' for back: ")
    if choose.lower() == 'b':
        return
    elif choose == '1':
        os.chdir(os.path.expanduser("~/Documents"))
        nameF = input("Write here the name of your folder: ")
        os.chdir(nameF)
        nameP = input("Write here the name of the project: ")
        delete = input(f"Are you sure you want delete {nameP} (y/n): " )
        if delete.lower() == 'y':
            os.system(f'rm -rf {nameP}')
            print("\033[1;36mProject removed successfully\033[0m")
            time.sleep(3)
        else:
            return

def Remove():
    clear_screen()
    welcome()
    print("\033[1;36mREMOVE YOUR ACTIVITY\033[0m")
    print("[1] Documents")
    print("[2] Desktop")
    choose = input("Write here the position of your folder or press 'b' for back: ")
    if choose.lower() == 'b':
        return
    elif choose == '1':
        os.chdir(os.path.expanduser("~/Documents"))
        nameF = input("Write here the name of your folder: ")
        os.chdir(nameF)
        dataRemove = input("DATE of file to clean: ")
        filepath = dataRemove + ".txt"
        if os.path.exists(filepath):
            with open(filepath,'r') as file:
                lines = file.readlines()
            if not lines:
                print("File is empty.")
            else:
                for i, line in enumerate(lines):
                    print(f"[]")




def main():
    clear_screen()
    welcome()
    
    

if __name__ == '__main__':
    main()
