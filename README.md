# Password_Manager_Application

Overview:
This Password Manager is a Python application with a graphical user interface (GUI) built using the Tkinter module. It allows users to generate, save, and retrieve passwords for different websites. The application securely stores passwords in a JSON file and provides easy access through a simple and intuitive interface.

Features:
1. Password Generation: Generates strong, random passwords with a mix of letters, numbers, and symbols.
2. Save Passwords: Saves passwords along with the associated website and email/username to a local JSON file.
3. Retrieve Passwords: Retrieves saved passwords for specific websites.
4. User-Friendly Interface: Easy-to-use interface for managing your passwords.
   
How It Works:

Password Generation:
1. Click the "Generate Password" button.
2. A random password is generated and displayed in the password entry field.
   
Save Password:
1. Enter the website name, email/username, and password.
2. Click the "Add" button to save the data.
3. The details are saved in a local JSON file (data.json).
   
Retrieve Password:
1. Enter the website name in the website entry field.
2. Click the "search" button.
3. If the website exists in the data, the email/username and password are displayed in a message box.
