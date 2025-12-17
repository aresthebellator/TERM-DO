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
    print("[1] Add activity")
    print("[2] Edit activity")
    print("[3] Remove activity")
    print("[4] View all the activities")
    print("[E] Exit\n")
    return input("==> ")

def Add():
    running_add = True
    while running_add:
        clear_screen()
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

        # Sottociclo per aggiungere più attività allo stesso giorno
        adding_items = True
        while adding_items:
            clear_screen()
            print(f"--- Adding to {data} ---")
            new_activity = input("Write the activity: ")
            time_activity = input("At: ")
            
            with open(filepath, 'a') as f:
                f.write(f"ACTIVITY:    {new_activity}        TIME:  {time_activity}\n")
            
            print("\033[1;32mActivity added!\033[0m")
            again = input("\nDo you wanna add another activity in THIS day? (y/n): ")
            if again.lower() != 'y':
                adding_items = False
        
        # Dopo aver finito con un giorno
        print("\n[1] Change day / [2] Back to menu")
        choice = input("==> ")
        if choice != '1':
            running_add = False

def Edit():
    clear_screen()
    dateEdit = input("Enter the DATE you want to edit (e.g., 15_12_25): ")
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
    dataRemove = input("DATE of file to clean: ")
    filepath = dataRemove + ".txt"

    if os.path.exists(filepath):
        activity_remove = input("Keyword of activity to remove: ")
        with open(filepath, 'r') as file:
            lines = file.readlines()

        lines_to_keep = [l for l in lines if activity_remove.lower() not in l.lower()]
        
        with open(filepath, 'w') as file:
            file.writelines(lines_to_keep)
        
        print(f"\033[1;32mDone. File updated.\033[0m")
    else:
        print("File not found.")
    time.sleep(2)

def View():
    clear_screen()
    date = input("\033[1;36mDATE to view:\033[0m")
    if os.path.exists(date + ".txt"):
        print(f"\n--- Activities for {date} ---")
        with open(date + ".txt", 'r') as file:
            content = file.read()
            print(content if content else "Empty file.")
    else:
        print("File not found.")
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