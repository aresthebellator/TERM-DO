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

def Menu():   
    print("-----------------------------------------------------------")
    print("\033[1;36mCHOOSE AN OPTION:\033[0m\n")
    print("\033[1;36m[1]\033[0m Add activity")
    print("\033[1;36m[2]\033[0m Edit activity")
    print("\033[1;36m[3]\033[0m Remove activity")
    print("\033[1;36m[4]\033[0m View all the activities")
    print("\033[1;31m[E] Exit\033[0m\n")
    return input("==> ")

def Add():
    running_add = True
    while running_add:
        clear_screen()
        Welcome()
        print("\033[1;36mADD ACTIVITY\033[0m")
        data = input("DAY: (ex: 15_12_25) or 'b' to go back: ")
        
        if data.lower() == 'b':
            break

        filepath = data + ".txt"
        
        if not os.path.exists(filepath):
            print(f"\033[1;36mError, can't find the day: {data}\033[0m")
            create = input("Do you wanna create this day? (y/n): ")
            if create.lower() == 'y':
                with open(filepath, 'w'): pass
                print(f"{data} Created!")
                time.sleep(1)
            else:
                continue

        
        adding_items = True
        while adding_items:
            clear_screen()
            print(f"\033[1;36m--- Adding to {data} ---\033[0m]")
            new_activity = input("Write the activity: ")
            req_time = input("Have you a specific time for this activity? (y/n)")
            
            if req_time.lower() == 'y':
                time_activity = input("At: ")
                with open(filepath, 'a')as f:
                    f.write(f"ACTIVITY:    {new_activity}        TIME:  {time_activity}\n")
                print("\033[1;32mActivity added! \033[0m")
                again = input("\nDo you wanna add another activity in THIS day? (y/n): ")
                if again.lower() != 'y':
                    adding_items = False    
            
            elif req_time.lower() == 'n':
                time_activity = "NO TIME"
                with open(filepath,'a') as f:
                    f.write(f"ACTIVITY:    {new_activity}        TIME:  {time_activity}\n")
                print("\033[1;32mActivity added! \033[0m")
                again = input("\nDo you wanna add another activity in THIS day? (y/n): ")
                if again.lower() != 'y':
                    adding_items = False
            
            
        
        
        print("\n[1] Change day / [2] Back to menu")
        choice = input("==> ")
        if choice != '1':
            running_add = False

def Edit():
    clear_screen()
    Welcome()
    print("\033[1;36mEDIT ACTIVITY\033[0m")
    dateEdit = input("Enter the DATE you want to edit or press 'b' for back (e.g., 15_12_25): ")
    if dateEdit == 'b':
        return
    
    filepath = dateEdit + ".txt"

    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
        
        if not lines:
            print(f"\033[1;33mThe file {filepath} is empty.\033[0m")
            time.sleep(2)
            return

        print("\n### Actually activities ###")
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

def Remove():
    clear_screen()
    Welcome()
    print("\033[1;36mREMOVE YOUR ACTIVITY\033[0m")
    dataRemove = input("DATE of file to clean or press 'b' for back: ")
    
    if dataRemove.lower() == 'b':
        return 
    
    filepath = dataRemove + ".txt"

    if os.path.exists(filepath):
        with open(filepath,'r') as file:
            content = file.read()
            print(content)
        print("\n")
        activity_remove = input("Keyword of activity to remove: ")
        with open(filepath, 'r') as file:
            lines = file.readlines()

        lines_to_keep = [l for l in lines if activity_remove.lower() not in l.lower()]
    
        with open(filepath, 'w') as file:
            file.writelines(lines_to_keep)
    
        print(f"\033[1;32mDone. File updated.\033[0m")
        time.sleep(2) 
    
    else:   
        print("File not found.")
        time.sleep(2) 
            

    

def View():
    clear_screen()
    Welcome()
    print("\033[1;36mDATE TO WIEW\033[0m")
    date = input("Write here the date you need to wiew or press 'b' for back: ")
    if date == 'b':
        return
    
    if os.path.exists(date + ".txt"):
        clear_screen()
        print(f"\n\033[1;36m--- Activities for {date} ---\033[0m")
        with open(date + ".txt", 'r') as file:
            content = file.read()
            print(content if content else "\033[1;31mEmpty file.\033[0m")
    else:
        print("\033[1;31mFile not found.\033[0m")
    input("\nPress Enter to return to menu...")

def main():
    while True:
        clear_screen()
        Welcome()
        choice = Menu()

        if choice == '1':
            Add()
        elif choice == '2':
            Edit()
        elif choice == '3':
            Remove()
        elif choice == '4':
            View()
        elif choice.lower() == 'e':
            print("\033[1;31mProgram terminated!\033[0m")
            time.sleep(2)
            clear_screen()
            break
        else:
            print("Invalid Option!")
            time.sleep(1)

if __name__ == "__main__":
    main()
