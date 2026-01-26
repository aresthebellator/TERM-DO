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
        print("[B] Back")
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
                    for i,line in enumerate(lines):
                        print(f"[{i+1}] {line.strip()}")
                        task_remove = input("\nKeyword of task to remove: ")
                        lines_to_keep = [l for l in lines if task_remove.lower() not in l.lower()]
                        with open(filepath,'w') as file:
                            file.writelines(lines_to_keep)
                        print("\033[1;32mDone. File updated- \033[0m")
        
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
                        
                    
                        
                        












def main():
    clear_screen()
    welcome()
    #CreateProject()
    AddORemoveTask()
    

if __name__ == '__main__':
    main()
