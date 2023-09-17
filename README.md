# VAULT

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-8.6-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3.3-blue)
![Pillow](https://img.shields.io/badge/Pillow-8.2.0-blue)

This is a simple password manager application built using Python and the Tkinter library. It allows you to manage and store your usernames and passwords securely.

## Features
- Add new passwords.
- Update existing passwords.
- Delete passwords.
- Copy passwords to clipboard.
- Toggle password visibility.
- Pagination for managing a large number of passwords.

## Prerequisites
Before running the application, make sure you have the following libraries installed:
- Tkinter
- Pandas
- Pillow (PIL)

You can install these libraries using pip:

```bash
pip install tk
pip install pandas
pip install pillow
```

## Usage

1. Run the application using Python:
   ```bash
   python main.py
   ```
2. Click the "Log in" button to access the password manager.
3. Inside the password manager, you can perform the following actions:

    - Add New Password: Click the "Add" button to create a new password entry. Enter the username and password, then click "Save" to add it to the list.

    - Update Password: Select a password entry, click the "Update" button to modify the username or password, then click "Save" to update it.

    - Delete Password: Select a password entry and click the "Delete" button to remove it from the list.

    - Copy Password: Click the copy icon next to a password entry to copy the password to your clipboard.

    - Toggle Password Visibility: Click the eye icon next to a password entry to toggle the visibility of the password.

    - Pagination: If you have many passwords, use the "Previous" and "Next" buttons to navigate through the pages of passwords.

## Data Storage

The passwords are stored in a CSV file named `data.csv` in the `./img/` directory. The application uses the Pandas library to read and write data to this CSV file. Passwords are stored in a tabular format with columns for usernames and passwords.

The structure of the `data.csv` file is as follows:

```csv
user,pass
username1,password1
username2,password2
username3,password3
# ...
```
## Disclaimer

This password manager is for educational purposes only. It is intended for learning and demonstration purposes and should not be used for storing sensitive or critical passwords. The security of the application may not meet the standards required for safeguarding highly sensitive information.

Use it responsibly and at your own risk. Always exercise caution and consider using reputable, secure password management solutions for important or sensitive data.

## Note

Please note that this is a basic password manager and is not suitable for storing sensitive or critical passwords. Be aware that data loss or security breaches can occur, so make sure to keep backups of your passwords and consider using dedicated, secure password management software for important and sensitive information.
