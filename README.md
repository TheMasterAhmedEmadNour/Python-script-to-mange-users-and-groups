# Python-script-to-mange-users-and-groups
# User & Group Management Script

## Overview  
This is a **Python script** designed to simplify the management of users and groups on Linux systems.  
It provides an **interactive menu-driven interface**, allowing system administrators to perform common user and group management tasks without having to manually type shell commands.  

---

## Features  
### User Management  
- Add a new user  
- Modify user details (e.g., change default shell)  
- Delete a user  
- Disable/Enable a user account  
- Change user password  
- List existing users  

### Group Management  
- Create a new group  
- Add a user to a group  
- Delete a group  
- List existing groups  

### Additional  
- Validates if a user or group exists before performing actions  
- Simple interactive main menu for easy navigation  



---

## Requirements  
- Python 3.x  
- Linux system (Ubuntu, Debian, CentOS, etc.)  
- Sudo privileges to run system-level commands  

---

## Usage  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/manage-users.git
   cd manage-users
   
2. Run Script  
    ```
    python3 manage-users.py
3. Output
  Enter your choice: 1
  Enter new username: omda
  User omda does not exist. that's great!
  User omda added successfully.
