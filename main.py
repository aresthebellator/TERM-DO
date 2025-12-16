# ===============================================
# TERM-DO
# Copyright (c) 2025 aresthebellator
# Versione: 1.0
#
# Questo programma è rilasciato sotto la licenza MIT.
# Per maggiori dettagli, vedi il file LICENSE.
# ===============================================
import os
import time


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
    print("-----------------------------------------------------------\n")
    print("\033[1;36mCHOSE A OPTION:\033[0m\n")
    
    print("[1] Add activity\n")
    print("[2] Edit activity\n")
    print("[3] Remove activity\n")
    print("[4] View all the activitys\n")
    print("[E] Exit\n")
    

    final_choose = input("==> ")

    if(final_choose == '1'):
        Add()

    elif (final_choose == '2'):
        Edit()
    
    
    elif final_choose == '3':
        Remove()
    
    elif(final_choose == '4'):
        View()
    
    
    
    
    elif(final_choose.lower() == 'e'):
        print("\033[1;31mProgram terminated!\033[0m")
        time.sleep(3)
        os.system("clear")
        return 0




def Add():
    
    ACTIVITY = True
    AGAIN = True
    
    while(ACTIVITY == True):

        print("DAY: (ex: 15_12_25)")
        data = input("==> ")
        AGAIN = True
        
        while(AGAIN == True):
                
                if os.path.exists(data+".txt"):

                    with open(data + ".txt", 'a') as f: 
                    
                        new_activity = input("Write the activity: ")
                        time_activity = input("At:  ")
                        
                        f.write("ACTIVITY:    "+new_activity + "        "+ "TIME:  " +  time_activity + "\n") 
                    
                        print("\033[1;32mActivity added!\033[0m\n")
                        print("\033[1;36mDo you wanna add other activity in this day? (y/n)\033[0m\n")
                        again = input("==> ")
                    
                        if(again.lower() == 'y'):
                            AGAIN = True
                    
                        else:
                            print("\033[1;36mChoose:\033[0m\n")
                            print("[1] Change day\n")
                            print("[2] back to menu\n'")
                            print("[E] Exit\n")
                            choose = input("==> ")
                            if (choose == '1'):
                                ACTIVITY = True
                                AGAIN = False 
                        
                            elif (choose == '2'):
                                os.system("clear")
                                Welcome()
                                Menu()
                            
                            elif (choose.lower() == 'e'):
                                print("\033[1;Program terminated! ")
                                ACTIVITY = False
                                AGAIN = False
                
                if not os.path.exists(data+".txt"):
                    print("\033[1;36mError,can't find the day:\033[0m\n")
                    print("Do you wanna create this day? (y/n)\n")
                    create = input("==> ")
                    if (create.lower() == 'y'):
                        with open(data +".txt", 'w'):
                            print("\n")
                            print(data, "Added! ")
                            ACTIVITY = False 
                            AGAIN = True
                        
                        
                    elif(create.lower() == 'n'):
                        print("\033[1;36mChoose:\033[0m\n")
                        print("[1] Change day\n")
                        print("[E] Exit\n")
                        choose = input("==> ")
                        if (choose == '1'):
                            ACTIVITY = True
                            AGAIN = True
                        elif(choose.lower() == 'e'):
                            ACTIVITY = False
                            AGAIN = False










def Edit():
    dateEdit = input("Enter the DATE you want to edit (e.g., 15_12_25): ")
    filepath = dateEdit + ".txt"

    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
        
        if not lines:
            print(f"\033[1;33mThe file {filepath} is empty. Nothing to edit.\033[0m")
            return

        print("\n### Actualy activities ###")
        for i, line in enumerate(lines):
            print(f"[{i + 1}] {line.strip()}")
        print("---------------------------\n")

        try:
            line_number = int(input("Enter the number of the activity you want to modify: "))
            
            if 1 <= line_number <= len(lines):
                index_to_edit = line_number - 1
                original_line = lines[index_to_edit].strip()
                
                print(f"\nActivity selected: {original_line}")
                
                print("\033[1;36mWhat do you want to modify?\033[0m")
                print("[1] Activity Description")
                print("[2] Activity Time")
                choice = input("==> ")
                
                time_start = original_line.find("TIME:")
                
                if time_start != -1:
                    current_activity = original_line[original_line.find("ACTIVITY:") + len("ACTIVITY:"):time_start].strip()
                    current_time = original_line[time_start + len("TIME:"):].strip()
                else:
                    current_activity = original_line
                    current_time = ""
                
                new_activity = current_activity
                new_time = current_time

                if choice == '1':
                    new_activity = input("Enter the new activity description: ")
                    print("\033[1;32mDescription updated!\033[0m")
                
                elif choice == '2':
                    new_time = input("Enter the new time (ex: 15:30): ")
                    print("\033[1;32mTime updated!\033[0m")
                
                else:
                    print("\033[1;31mInvalid choice. No changes applied.\033[0m")
                    return

                new_line = f"ACTIVITY:    {new_activity}        TIME:  {new_time}\n"
                lines[index_to_edit] = new_line

                with open(filepath, 'w') as file:
                    file.writelines(lines)
                
                print(f"\n\033[1;32mSuccessfully updated activity {line_number} in {filepath}.\033[0m")
                print(f"New line: {new_line.strip()}")

            else:
                print("\033[1;31mInvalid line number.\033[0m")

        except ValueError:
            print("\033[1;31mInvalid input. Please enter a number.\033[0m")
    else:
        print(f"\033[1;31mError: File '{filepath}' does not exist.\033[0m")

    

def Remove():
    dataRemove = input("DATE: ")
    filepath = dataRemove + ".txt"

    if os.path.exists(filepath):
        activity_remove = input("ACTIVITY: ")

        with open(filepath, 'r') as file:
            lines = file.readlines()

        lines_to_keep = []
        remove_count = 0

        for line in lines:
            if activity_remove.lower().strip() not in line.lower().strip():
                lines_to_keep.append(line)

            else:
                remove_count += 1

        with open(filepath,'w') as file:
            file.writelines(lines_to_keep)

        if remove_count > 0:
            print(f"\033[1;32mRemoved {remove_count} instance(s) of '{activity_remove}' from {filepath}\033[0m]")

        else:
            print(f"\033[1;33mNo activity matching '{activity_remove}' was found in {filepath}.\033[0m")

    else:
        print(f"\033[1;31mError: File '{filepath}' does not exist.\033[0m")


def View():
    date = input("DATE: ")
    if os.path.exists(date+".txt"):
        with open(date+".txt", 'r')as file:
            content = file.read()
            print(content)






def main():
    Welcome()
    Menu()


if __name__ == "__main__":
    main()
