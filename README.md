## Safety-Island: Your Personal Island for Secure Confidential Data Storage

Safety-Island is a secure solution for safely storing your confidential data, such as passwords, personal information, secret keys, etc.

Key features:

• Local storage: Your data is stored only on your device, without access to cloud services.

• Strong encryption: Uses advanced symmetric encryption for maximum security.

• Single master password: Remember only one password to access all your data.

• Easy to use: Intuitive interface makes it easy to add, edit and manage your data.

• Free and open source: Available to everyone without restrictions.

How it works:

1. Create a master password: When you first launch Safety-Island, you will need to set a master password.
2. Add your data: Enter the category name, information, and any additional text you want to save.
3. Save changes: Your data will be encrypted and saved locally.
4. Access data: Enter your master password to access your data.

Benefits of Safety-Island:

• Enhanced security: Local storage and strong encryption protect your data from unauthorized access.

• Simplified data management: Remembering only one master password instead of multiple passwords is easier and more convenient.

• Confidentiality: Your data never leaves your device.

Additional features:

• Random password generation: Create secure passwords for your accounts.

• Cross-platform support: Available on different platforms, such as Windows, Linux and macOS.

Safety-Island is a reliable and convenient solution for those who care about the security of their data.



## How to install the application

1. Downloading:

* Click the "Code" button in the top right corner of this page.
* Select "Download ZIP" to download the project archive.

2. Unpacking:

* Unzip the downloaded ZIP archive to a convenient location on your computer.

3. Opening the project:

* Open the folder containing the unpacked project.
* Find the begin folder inside the project.

4. Running the terminal:

* Open the terminal (Command Prompt on Windows, Terminal on macOS/Linux).
* Navigate to the begin folder using the command cd <path to begin folder>.

5. Installing dependencies:

* In the terminal, enter the following command:
    
    pip install pyinstaller
    
    * This command will install the necessary pyinstaller package for building the application.

6. Building the application:

* In the terminal, enter the following command:
    
    pyinstaller --onefile --icon=icon.ico --noconsole shell.py
    
    * This command will start the application building process.
    * --onefile will create a single executable file for the application.
    * --icon=icon.ico will set the icon for the application (replace icon.ico with the name of your icon).
    * --noconsole will hide the console window when the application starts.

7. Moving the application:

* After building is complete, find the dist folder inside the begin folder.
* Inside the dist folder, find the application's executable file (usually called shell.exe on Windows, shell on macOS/Linux).
* Move this file from the dist folder to the begin folder.

8. Running the application:

* Find the application's executable file in the begin folder.
* Double-click it to run the application.

9. Creating a shortcut (for Windows):

* Right-click on the application's executable file.
* Select "Create shortcut".
* Move the shortcut to a convenient location on your desktop or in the "Start" menu.

Done! Now you can launch the application from the created shortcut.

Stay tuned!