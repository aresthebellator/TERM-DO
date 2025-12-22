# ===============================================
# TERM-DO
# Copyright (c) 2025 aresthebellator
# Versione: 1.1 (Fixed)
# ===============================================
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def Welcome():
    print("""\033[1;33m
████████╗███████╗██████╗ ███╗   ███╗      ██████╗  ██████╗ 
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║      ██╔══██╗██╔═══██╗
   ██║   █████╗  ██████╔╝██╔████╔██║█████╗██║  ██║██║   ██║
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║╚════╝██║  ██║██║   ██║
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║      ██████╔╝╚██████╔╝
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═════╝  ╚═════╝
    \033[0m""")

def MenuProject():
    clear_screen()
    Welcome()
    print("-----------------------------------------------------------")
    print("\033[1;36m[1]\033[0m Create a project ")
    print("\033[1;36m[2]\033[0m Edit a project ")
    print("\033[1;36m[3]\033[0m View a project ")
    print("\033[1;36m[4]\033[0m Remove a project ")
    print("\033[1;31m[B]\033[0m Back to main menu ")
    return input("==> ")

def MenuActivity():   
    clear_screen()
    Welcome()
    print("-----------------------------------------------------------")
    print("\033[1;36mCHOOSE AN OPTION:\033[0m\n")
    print("\033[1;36m[1]\033[0m Add activity")
    print("\033[1;36m[2]\033[0m Edit activity")
    print("\033[1;36m[3]\033[0m Remove activity")
    print("\033[1;36m[4]\033[0m View all activities")
    print("\033[1;31m[B]\033[0m Back to main menu ")
    return input("==> ")

def CreateProject():
    clear_screen()
    Welcome()
    print("\033[1;36mCREATE PROJECT\033[0m")
    name = input("Write the name of the project: ")
    filepath = name + ".txt"
    if os.path.exists(filepath):
        print("The project already exists! Try selecting EDIT PROJECT.")
        time.sleep(1)
        return
    
    with open(filepath, 'w') as f:
        pass
    print(f"{name} Created!")
    print("Now you can choose EDIT PROJECT to add tasks.")
    time.sleep(1)

def Add():
    running_add = True
    while running_add:
        clear_screen()
        Welcome()
        print("\033[1;36mADD ACTIVITY\033[0m")
        data = input("DAY (ex: 15_12_25) or 'b' to go back: ")
        
        if data.lower() == 'b':
            break

        filepath = data + ".txt"
        
        if not os.path.exists(filepath):
            print(f"\033[1;31mError, can't find the day: {data}\033[0m")
            create = input("Do you want to create this day? (y/n): ")
            if create.lower() == 'y':
                with open(filepath, 'w') as f: pass
                print(f"{data} Created!")
                time.sleep(1)
            else:
                continue

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

            with open(filepath, 'a') as f:
                f.write(f"ACTIVITY:    {new_activity}        TIME:  {time_activity}\n")
            print("\033[1;32mActivity added!\033[0m")
            
            again = input("\nDo you want to add another activity to THIS day? (y/n): ")
            if again.lower() != 'y':
                adding_items = False    
        
        print("\n[1] Change day / [2] Back to menu")
        choice = input("==> ")
        if choice != '1':
            running_add = False

def EditProject():
    clear_screen()
    Welcome()
    print("\033[1;36mEDIT PROJECT\033[0m")
    nameproject = input("Enter the name of the project or press 'b' for back: ")
    if nameproject.lower() == 'b':
        return

    filepath = nameproject + ".txt"

    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()

        if not lines:
            print(f"\033[1;33mThe Project {filepath} is empty.\033[0m")
            add = input("Do you want to add something? (y/n): ")
            if add.lower() == 'y':
                new_task = input("Enter the new task: ")
                with open(filepath, 'w') as file:
                    file.write(f"TASK:  {new_task}\n")
                print("\033[1;32mTask added!\033[0m")
        else:
            print("\n### YOUR TASKS ###")
            for i, line in enumerate(lines):
                print(f"[{i + 1}] {line.strip()}")

            try:
                line_number = int(input("\nEnter the number of the activity to modify: "))
                if 1 <= line_number <= len(lines):
                    index_to_edit = line_number - 1
                    new_task = input("Enter the new task: ")
                    lines[index_to_edit] = f"TASK:  {new_task}\n"
                    with open(filepath, 'w') as file:
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
    Welcome()
    print("\033[1;36mEDIT ACTIVITY\033[0m")
    dateEdit = input("Enter the DATE you want to edit or 'b' for back (e.g., 15_12_25): ")
    if dateEdit.lower() == 'b':
        return
    
    filepath = dateEdit + ".txt"

    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
        
        if not lines:
            print(f"\033[1;33mThe file {filepath} is empty.\033[0m")
            time.sleep(2)
            return

        print("\n### Current activities ###")
        for i, line in enumerate(lines):
            print(f"[{i + 1}] {line.strip()}")
        
        try:
            line_number = int(input("\nEnter the number of the activity to modify: "))
            if 1 <= line_number <= len(lines):
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
    Welcome()
    print("\033[1;36mREMOVE TASK IN YOUR PROJECT\033[0m")
    nameP = input("Enter the name of the project or press 'b' for back: ")
    if nameP.lower() == 'b':
        return

    filepath = nameP + ".txt"
    if os.path.exists(filepath):
        with open(filepath,'r') as file:
            lines = file.readlines()
        
        if not lines:
            print("File is empty.")
        else:
            for i, line in enumerate(lines):
                print(f"[{i+1}] {line.strip()}")
            
            task_remove = input("\nKeyword of task to remove: ")
            lines_to_keep = [l for l in lines if task_remove.lower() not in l.lower()]
            with open(filepath, 'w') as file:
                file.writelines(lines_to_keep)
            print("\033[1;32mDone. File updated.\033[0m")
    else:
        print("File not found.")
    time.sleep(2)

def Remove():
    clear_screen()
    Welcome()
    print("\033[1;36mREMOVE YOUR ACTIVITY\033[0m")
    dataRemove = input("DATE of file to clean or press 'b' for back: ")
    
    if dataRemove.lower() == 'b':
        return 
    
    filepath = dataRemove + ".txt"

    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()

        if not lines:
            print("File is empty.")
        else:
            for i, line in enumerate(lines):
                print(f"[{i+1}] {line.strip()}")
            
            activity_remove = input("\nKeyword of activity to remove: ")
            lines_to_keep = [l for l in lines if activity_remove.lower() not in l.lower()]
            with open(filepath, 'w') as file:
                file.writelines(lines_to_keep)
            print("\033[1;32mDone. File updated.\033[0m")
    else:   
        print("File not found.")
    time.sleep(2) 

def ViewP():
    clear_screen()
    Welcome()
    print("\033[1;36mVIEW YOUR PROJECT\033[0m")
    nameP = input("Write the name of project to view or press 'b' for back: ")
    
    if nameP.lower() == 'b':
        return
    filepath = nameP + ".txt"
    if os.path.exists(filepath):
        clear_screen()
        print(f"\n\033[1;31m--- Tasks for {nameP} ---\033[0m")
        with open(filepath,'r') as file:
            content = file.read()
            print(content if content else "\033[1;31mEmpty file.\033[0m")
    else:
        print("\033[1;31mFile not found.\033[0m")
    input("\nPress Enter to return...")

def View():
    clear_screen()
    Welcome()
    print("\033[1;36mDATE TO VIEW\033[0m")
    date = input("Write the date you need to view or press 'b' for back: ")
    if date.lower() == 'b':
        return
    
    filepath = date + ".txt"
    if os.path.exists(filepath):
        clear_screen()
        print(f"\n\033[1;36m--- Activities for {date} ---\033[0m")
        with open(filepath, 'r') as file:
            content = file.read()
            print(content if content else "\033[1;31mEmpty file.\033[0m")
    else:
        print("\033[1;31mFile not found.\033[0m")
    input("\nPress Enter to return...")

def main():
    while True:
        clear_screen()
        Welcome()
        print("[A] Activity mode")
        print("[P] Project mode")
        print("\033[1;31m[E] Exit\033[0m\n")
        choice_type = input("==> ").lower()
        
        if choice_type == 'a':
            choice = MenuActivity()
            if choice == '1': Add()
            elif choice == '2': Edit()
            elif choice == '3': Remove()
            elif choice == '4': View()
        elif choice_type == 'p':
            choice = MenuProject()
            if choice == '1': CreateProject()
            elif choice == '2': EditProject()
            elif choice == '3': ViewP()
            elif choice == '4': RemoveProject()
        elif choice_type == 'e':
            print("\033[1;31mProgram terminated!\033[0m")
            time.sleep(1)
            clear_screen()
            break
        else:
            print("Invalid Option!")
            time.sleep(1)

if __name__ == "__main__":
    main()