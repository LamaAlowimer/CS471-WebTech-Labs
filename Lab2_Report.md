# Django and Basic Git operations (Lab 2): 

**Student Name:** لمى العويمر 
**Student ID:** 432205254
**Course:** Web Technologies (CS471)  

---

## 1. Pre-lab Preparation
* Verified that Python 3.7+ is installed and upgraded the PIP package manager.
* Ensured Git is installed and generated the necessary SSH keys for secure command-line authentication.

## 2. Part 1: Django Web Development Framework

### Task 1: Environment Setup
<img width="500" alt="image" src="https://github.com/user-attachments/assets/037cc5af-1e72-43ab-81e0-e3979a73d739" />

### Task 2: Project Creation
<img width="500" alt="image" src="https://github.com/user-attachments/assets/149ddd84-7790-4c5d-8641-1949fba37064" />

### Task 3: Application Configuration
* Built the required internal structure by creating `apps/`, `apps/template/`, and `apps/static/` directories within the project ROOT folder.
* Generated two internal module services inside the `apps` directory: `bookmodule` and `usermodule`.
* Modified the configuration files (`apps.py`) for both modules to accurately reflect their new directory paths: `apps.bookmodule` and `apps.usermodule`.
* Registered the newly created modules by adding them to the `INSTALLED_APPS` array in the `libraryproject/settings.py` file.
* Restarted the server to verify that the complete configuration works as intended.

---

## 3. Part 2: Git System & Remote Connection

### Task 1: Local Repository Initialization
* Navigated to the ROOT folder of the Django application and initialized a local Git repository using `git init`.
* Created a `.gitignore` file to exclude compiled Python files, cache directories (like `__pycache__`), environment folders (`env/`, `venv/`), and logs from being tracked by version control.
* Staged the `.gitignore` file and created the first commit with the message "add ignore file".

### Task 2: Remote Repository Integration
* Configured the global Git settings with the required username and email credentials.
* Generated an Ed25519 SSH key and added it to the `ssh-agent` for secure communication with the remote server.
* Linked the local repository to the online remote repository using the `git remote add origin` command.
* Fetched the origin data and pushed the local commits to the `main` branch of the remote repository.
* Verified the successful upload of all project files by checking the online repository.
