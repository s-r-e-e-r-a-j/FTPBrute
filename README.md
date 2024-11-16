


## FTPBrute - FTP & SFTP Brute Force Tool
FTPBrute is a powerful brute-forcing tool designed to test the security of FTP and SFTP servers by performing dictionary-based attacks. It helps security researchers, penetration testers, and ethical hackers to assess the robustness of authentication mechanisms by attempting to crack login credentials using customizable wordlists for both usernames and passwords.

This tool provides a user-friendly graphical interface that simplifies the process of running brute-force attacks against FTP and SFTP services, allowing users to test their servers’ security in a controlled environment.

## Key Features
- **Support for FTP & SFTP Protocols:** You can choose between FTP and SFTP for brute-forcing authentication credentials.
- **Custom Wordlist Support:** Easily load custom wordlists for usernames and passwords to tailor your attack.
- **Real-Time Output:** View attack progress in real-time, with detailed feedback about each attempt.
- **Success Detection:** The tool automatically stops once a successful login is found, saving time and resources.
- **Abort Attack:** The ability to stop the brute force attack at any time.
- **User-Friendly GUI:** The tool features a simple, intuitive graphical interface designed for ease of use.
## Requirements
To run FTPBrute, you will need Python 3.x and the following dependencies:

- `paramiko:` A library used for handling SFTP connections.
- `ftplib:` Python's built-in library for FTP connections.
- `tkinter:` Python's built-in GUI library for building the graphical user interface.
## Install Dependencies
To install the required dependencies, you can use the following command:

```bash
pip install paramiko
```
`ftplib` and `tkinter` are part of the standard Python library, so no installation is needed for them.

## Installation
1 **Clone the Repository:** Clone the FTPBrute repository to your local machine using Git:

bash
Copy code
git clone https://github.com/yourusername/FTPBrute.git
cd FTPBrute
Run the Script: To start the tool, run the Python script:

Copy code
python ftp_brute_force_tool.py
How to Use
Launch the Application: When you run the script, the graphical user interface (GUI) will open.

Set Target IP:

Enter the IP address of the FTP or SFTP server that you want to attack.
Select the Protocol:

Choose between FTP or SFTP by selecting the appropriate radio button.
Choose Wordlists:

Username Wordlist: Click on "Select Username Wordlist" to choose a text file containing possible usernames.
Password Wordlist: Similarly, click "Select Password Wordlist" to choose a text file with possible passwords.
Start the Attack:

Once you’ve filled in all the necessary fields, click "Start Brute Force" to begin the attack. The tool will start trying combinations of usernames and passwords and show the results in real time.
Stop the Attack:

If you need to stop the attack for any reason, click "Stop Brute Force".
Example Workflow
Open the tool and enter the target server's IP address.
Select FTP or SFTP as the protocol.
Choose your username and password wordlists from your local files.
Click Start Brute Force to begin the attack. The tool will display the progress, showing which combinations it is attempting.
Once a valid combination is found, it will be displayed, and the tool will stop the attack.
Example Screenshot

An example of FTPBrute in action.

Legal Disclaimer
FTPBrute is intended for use by security professionals and ethical hackers to test their own systems or systems they have explicit permission to test. Unauthorized use of this tool to attack systems without permission is illegal and unethical.

By using this tool, you agree that you are solely responsible for any actions performed. The author of this tool does not accept responsibility for any damages or legal consequences caused by the misuse of this tool.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
