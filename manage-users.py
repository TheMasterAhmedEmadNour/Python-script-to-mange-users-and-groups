import subprocess   #importing subprocess module to run shell commands
###########################################################################################
# Function to run shell commands
def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
###########################################################################################
def add_user():
    username = input("Enter new username: ")
    result = subprocess.run(["id", username], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print(f"User {username} already exists on the system.   SADLY!  ")
        print ("Please try again and add a new user :)")
        add_user()
    else:
        print(f"User {username} does not exist.      that's great!")
        run_command(f"sudo useradd {username}")
        print(f"User {username} added successfully.")
###########################################################################################
def modify_user():
    username = input("Enter username to modify: ")
    result = subprocess.run(["id", username], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        new_shell = input("Enter new shell (e.g. /bin/bash): ")
        print(f"User {username} exists on the system.       that's great!")
        run_command(f"sudo usermod -s {new_shell} {username}")
        print(f"User {username} modified successfully.")
    else:
        print(f"User {username} does not exist.     SADLY!  ")
        print ("Please  try again and add vaild user :)")
        modify_user()
##########################################################################################
def delete_user():
    username = input("Enter username to delete: ")
    result = subprocess.run(["id", username], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:

        print(f"User {username} exists on the system.    that's great!")
        run_command(f"sudo userdel -r {username}")
        print(f"User {username} deleted successfully.")
    else:
        print(f"User {username} does not exist.         SADLY!  ")
        print ("Please  try again and add vaild user :)")
        delete_user()
##########################################################################################
def list_users():
    run_command("awk -F: '$3 >= 1000 && $3 < 60000 {print $1}' /etc/passwd")
##########################################################################################
def add_group():
    groupname = input("Enter new group name: ")
    group_test = subprocess.run(["getent", "group", groupname],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

    if group_test.returncode == 0:
        print(f"Group {groupname}  arleady exists on the system.    SADLY!  ")
        print ("Please try again and add a new group :)")
        add_group()
    else:
        print(f"Group {groupname} does not exist.       that's great!")
        run_command(f"sudo groupadd {groupname}")
        print(f"Group {groupname} added successfully.")
##########################################################################################
def modify_group():
    groupname = input("Enter group name to modify: ")
    group_test = subprocess.run(["getent", "group", groupname],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

    if group_test.returncode == 0:
        print(f"Group {groupname} exists on the system.     that's great!")
    else:
        print(f"Group {groupname} does not exist.   SADLY!  ")
        print("Please try again and add a valid group :)")
        modify_group()
    username = input("Enter username to add to the group: ")
    result = subprocess.run(["id", username], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print(f"User {username} exists on the system.   that's great!")

    else:
        print(f"User {username} does not exist.  SADLY!  ")
        print ("Please  try again and add vaild user :)")
        modify_group()
    run_command(f"sudo usermod -aG {groupname} {username}")
    print(f"User {username} added to group {groupname}.")
##########################################################################################
def delete_group():
    groupname = input("Enter group name to delete: ")
    group_test = subprocess.run(["getent", "group", groupname],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

    if group_test.returncode == 0:
        print(f"Group {groupname} exists on the system.     that's great!")
        run_command(f"sudo groupdel {groupname}")
        print(f"Group {groupname} deleted successfully.")
    else:
        print(f"Group {groupname} does not exist.   SADLY!  ")
        print("Please try again and add a valid group :)")
        delete_user()
##########################################################################################
def list_groups():
    run_command("awk -F: '$3 >= 1000 && $3 < 60000 {print $1}' /etc/group")
##########################################################################################
def disable_user():
    username = input("Enter username to disable: ")
    result = subprocess.run(["id", username], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print(f"User {username} exists on the system.   that's great!")
        run_command(f"sudo usermod -L {username}")
        print(f"User {username} disabled successfully.")
    else:
        print(f"User {username} does not exist. SADLY!  ")
        print ("Please  try again and add vaild user :)")
        disable_user()
##########################################################################################
def enable_user():
    username = input("Enter username to enable: ")
    result = subprocess.run(["id", username], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print(f"User {username} exists on the system.   that's great!")
        run_command(f"sudo usermod -U {username}")
        print(f"User {username} enabled successfully.")
    else:
        print(f"User {username} does not exist. SADLY!  ")
        print ("Please  try again and add vaild user :)")
        enable_user()
##########################################################################################
def change_password():
    username = input("Enter username to change password: ")
    result = subprocess.run(["id", username], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print(f"User {username} exists on the system.   that's great!")
        run_command(f"sudo passwd {username}")
        print(f"User {username} 's passsword changed successfully.")
    else:
        print(f"User {username} does not exist.     SADLY!  ")
        print ("Please  try again and add vaild user :)")
        change_password()
##########################################################################################
def about():
    print("User & Group Management Script\nCreated in Python.")
##########################################################################################
# Main menu loop
def main():
    while True:
        print("\n==== Main Menu ====")
        print("1.  Add User          =================ADDING user=======================")
        print("2.  Modify User       =================MODIFY user=======================")
        print("3.  Delete User       =================DELETE user=======================")
        print("4.  List Users        =================LIST users========================")
        print("5.  Add Group         =================CREATE group======================")
        print("6.  Modify Group      =================ADDING user to group==============")
        print("7.  Delete Group      =================DELETE group======================")
        print("8.  List Groups       =================LIST groups=======================")
        print("9.  Disable User      =================DISABLE user======================")
        print("10. Enable User       =================ENABLE user=======================")
        print("11. Change Password   =================CHANGE user password==============")
        print("12. About             =================ABOUT this script=================")
        print("0.  Exit              =================EXIT the script===================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            modify_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            list_users()
        elif choice == "5":
            add_group()
        elif choice == "6":
            modify_group()
        elif choice == "7":
            delete_group()
        elif choice == "8":
            list_groups()
        elif choice == "9":
            disable_user()
        elif choice == "10":
            enable_user()
        elif choice == "11":
            change_password()
        elif choice == "12":
            about()
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()