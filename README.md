## FTPBrute - FTP, SFTP & FTPS Brute Force Tool
FTPBrute is a powerful GUI-based brute-forcing tool designed to brute-force FTP, SFTP, and FTPS servers by performing dictionary-based attacks.

This tool provides a user-friendly graphical interface that simplifies the process of running brute-force attacks against FTP, SFTP, and FTPS services.

## Legal Disclaimer
FTPBrute is intended for use by security professionals and ethical hackers to test their own systems or systems they have explicit permission to test. Unauthorized use of this tool to attack systems without permission is illegal and unethical.

By using this tool, you agree that you are solely responsible for any actions performed. The author of this tool does not accept responsibility for any damages or legal consequences caused by the misuse of this tool.

## Key Features
- **Support for FTP, SFTP & FTPS Protocols:** You can choose between FTP, SFTP, and FTPS for brute-forcing authentication credentials.
- **Custom Port Support:** Optionally, specify custom ports for FTP (default is 21), SFTP (default is 22), and FTPS (default is 21) if the target uses non-standard ports.
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
- `ssl:` A built-in Python library for FTPS connections.
## Install Dependencies
To install the required dependencies, you can use the following command:

```bash
pip install paramiko
```
`ftplib`, `tkinter`, and `ssl` are part of the standard Python library, so no installation is needed for them.

## Installation
1. **Clone the Repository:**
   
 Clone the FTPBrute repository to your local machine using Git:
   
```bash
git clone https://github.com/s-r-e-e-r-a-j/FTPBrute.git
```
2. **Navigate to the FTPBrute directory**
 
```bash
cd FTPBrute
```
3. **Navigate to the FTPBrute directory**
```bash
cd FTPBrute
```
4. **Install the tool:**
   
```bash
sudo python3 install.py
```
Then type `y`to install.

5. **Run the tool**:
   
```bash
ftpbrute
```
## How to Use
1. **Launch the Tool:**

- When you run the Tool, the graphical user interface (GUI) will open.
  
2. **Set Target IP:**

- Enter the `IP address` of the FTP, SFTP, or FTPS server that you want to attack.
  
3. **Select the Protocol:**

- Choose between `FTP`, `SFTP`, or `FTPS` by selecting the appropriate radio button.
  
4. **Optional Port (If Needed):**

- If the FTP, SFTP, or FTPS server uses a non-standard port, you can optionally specify the port number in the "Port" field.
  
- The default port for FTP is 21, for SFTP is 22, and for FTPS is 21, but you can enter a custom port if necessary.
  
5. **Choose Wordlists:**

- **Username Wordlist:** Click on "Select Username Wordlist" to choose a text file containing possible usernames.
- **Password Wordlist:** Similarly, click "Select Password Wordlist" to choose a text file with possible passwords.
  
6. **Start the Attack:**

- Once you’ve filled in all the necessary fields, click "Start Brute Force" to begin the attack. The tool will start trying combinations of usernames and passwords and show the results in real time.
  
7. **Stop the Attack:**

- If you need to stop the attack for any reason, click "Stop Brute Force".
  
## Example Workflow
1. Open the tool and enter the target server's IP address.
2. Select `FTP`, `SFTP`, or `FTPS `as the protocol.
3. (Optional) Enter a custom port if the FTP, SFTP, or FTPS server uses a non-standard port. The default ports are 21 for FTP, 22 for SFTP, and 990 for FTPS.
4. Choose your username and password wordlists from your local files.
5. Click` Start Brute Force` to begin the attack. The tool will display the progress, showing which combinations it is attempting.
6. Once a valid combination is found, it will be displayed, and the tool will stop the attack.
Example Screenshot

## An example of FTPBrute in action.

![VirtualBox_klinux9_09_02_2025_20_44_17](https://github.com/user-attachments/assets/346c5cdc-da92-4a86-9a2e-fd20a572a903)


## Uninstallation
To uninstall the tool, navigate to the FTPBrute directory and run:

```bash
sudo python3 install.py
```
Then enter `n` to uninstall.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

