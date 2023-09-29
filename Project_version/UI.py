import os
import subprocess
import tkinter as tk
from tkinter import filedialog, ttk

# Global variable to store the selected file path
selected_file_path = ""
save_file_path = ""
save_file_path_decrypt = ""

encrypt_fpath = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\ENCRYPT\\Encrypt_main.py"
decrypt_fpath = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\DECRYPT\\Decrypt_main.py"

filetypes = [
        ("Text files", "*.txt"),
        ("Java", "*.java"), ("C/C++", "*.cpp"),
        ("Python", "*.py"), ("Julia", "*.jl"),
        ("All files", "*.*"),
    ]

# Function to execute the encryption or decryption program
def execute_program1(program_path, additional_args=None):
    try:
        command = ["python", program_path]
        if additional_args is not None:
            command.extend(additional_args)
        # Capture the subprocess's return code (exit status)
        completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return completed_process.returncode
    except Exception as e:
        print(f"Error executing program: {e}")
        return 1  # Return a non-zero exit code to indicate an error (modify as needed)

# Function to handle the encryption button click
def encrypt():
    global selected_file_path, save_file_path  # Access the global variables
    file_path = file_entry.get()

    if os.path.exists(file_path):
        selected_file_path = file_path  # Store the file path in the global variable
        save_file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",  # Default extension
            filetypes=filetypes,
        )
        if save_file_path:
            exit_status = execute_program1(encrypt_fpath, [selected_file_path, save_file_path])
            if exit_status == 0:
                print("File encrypted successfully and saved at:", save_file_path)
                status_label.config(text="File encrypted successfully and saved at: " + save_file_path, foreground="green")
            else:
                print("Error: Encryption process encountered an error.")
                status_label.config(text="Error: Encryption process encountered an error.", foreground="red")
        else:
            status_label.config(text="File not saved.", foreground="red")
    else:
        status_label.config(text="File not found!", foreground="red")

# Function to handle the "Decrypt and Save" button click
def decrypt_and_save():
    global selected_file_path_decrypt, save_file_path_decrypt # Access the global variables
    key = key_entry.get()
    file_path = file_entry_decrypt.get()

    if os.path.exists(file_path):
        selected_file_path_decrypt = file_path
        # Verify the key
        keypath = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\common\\Decrypt_keys.txt"
        valid_key = False
        with open(keypath) as file1:
            for line in file1:
                if key == line.strip():
                    valid_key = True
                    break
        if valid_key:
            status_label.config(text="Decryption key Valid", foreground="green")
            save_file_path_decrypt = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=filetypes,
            )
            if save_file_path_decrypt:
                exit_status = execute_program1(decrypt_fpath, [selected_file_path_decrypt, save_file_path_decrypt])
                if exit_status == 0:
                    print("File decrypted successfully and saved at:", save_file_path_decrypt)
                    status_label.config(text="File decrypted successfully and saved at: " + save_file_path_decrypt, foreground="green")
                else:
                    print("Error: Decryption process encountered an error.")
            else:
                status_label.config(text="File not saved.", foreground="red")
        else:
            status_label.config(text="Decryption key Invalid", foreground="red")
    else:
        status_label.config(text="File not found!", foreground="red")

#---------------------------------------------------------------#

# Function to display a tooltip when hovering over a widget
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="lightyellow", relief="solid", borderwidth=0.5)
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

# Create the main window
window = tk.Tk()
window.title("Encryption and Decryption")
window.geometry("570x360")  # Set initial window size

# Use the 'vista' theme
style = ttk.Style()
style.theme_use("vista")

# Create two sections - Encrypt and Decrypt
encrypt_frame = ttk.LabelFrame(window, text="Encrypt Section", padding=10)
encrypt_frame.pack(padx=10, pady=10, fill="both", expand=True)

decrypt_frame = ttk.LabelFrame(window, text="Decrypt Section", padding=10)
decrypt_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Function to open the file dialog and clear the file_entry
def browse_and_clear():
    file_entry.delete(0, tk.END)  # Clear the text field
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.insert(0, file_path)

# Encrypt Section
file_label = ttk.Label(encrypt_frame, text="Enter file path:")
file_label.grid(row=0, column=0, padx=5, pady=5)

file_entry = ttk.Entry(encrypt_frame, width=50)
file_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = ttk.Button(encrypt_frame, text="Browse", command=lambda: browse_and_clear())
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Add a tooltip for the Browse button in the Encrypt Section
Tooltip(browse_button, " Browse and select \n any plaintext file for encryption ")

encrypt_button = ttk.Button(encrypt_frame, text="Encrypt and Save As", command=encrypt)
encrypt_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Add a tooltip for the Encrypt button in the Encrypt Section
Tooltip(encrypt_button, " Initiate Encryption and \n Save your file preferably with a new name. ")

# Decrypt Section
key_label = ttk.Label(decrypt_frame, text="Enter decryption key:")
key_label.grid(row=0, column=0, padx=5, pady=5)

key_entry = ttk.Entry(decrypt_frame, width=50)
key_entry.grid(row=0, column=1, padx=5, pady=5)

# Function to open the file dialog for decryption and fill the text field
def browse_decrypt():
    file_entry_decrypt.delete(0, tk.END)  # Clear the text field
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    if file_path:
        file_entry_decrypt.insert(0, file_path)
        decrypt_button.config(state=tk.NORMAL)  # Enable the "Decrypt and Save" button

def verify_key():
    key = key_entry.get()
    keypath = r"C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\common\\Decrypt_keys.txt"
    valid_key = False

    # Check if the key is valid
    with open(keypath) as file1:
        for line in file1:
            if key == line.strip():
                valid_key = True
                break

    if valid_key:
        status_label.config(text="Decryption Key Valid", foreground="green")
        decrypt_button.config(state=tk.NORMAL)
    else:
        status_label.config(text="Decryption Key Invalid", foreground="red")
        decrypt_button.config(state=tk.DISABLED)

verify_button = ttk.Button(decrypt_frame, text="Verify Key", command=verify_key)
verify_button.grid(row=0, column=2, padx=5, pady=5)

# Add a tooltip for the Verify button in the Decrypt Section
Tooltip(verify_button, " Enter the Decryption Key \n as shared by the Encryptor ")

file_label_decrypt = ttk.Label(decrypt_frame, text="Select file to decrypt:")
file_label_decrypt.grid(row=1, column=0, padx=5, pady=5)

file_entry_decrypt = ttk.Entry(decrypt_frame, width=50)
file_entry_decrypt.grid(row=1, column=1, padx=5, pady=5)

browse_button_decrypt = ttk.Button(decrypt_frame, text="Browse", command=browse_decrypt)
browse_button_decrypt.grid(row=1, column=2, padx=5, pady=5)

# Add a tooltip for the Browse button in the Decrypt Section
Tooltip(browse_button_decrypt, " Browse and select \n an encrypted file for decryption ")

decrypt_button = ttk.Button(decrypt_frame, text="Decrypt and Save As", command=decrypt_and_save, state=tk.DISABLED)
decrypt_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Add a tooltip for the Decrypt button in the Decrypt Section
Tooltip(decrypt_button, " Initiate Decryption and \n Save your file preferably with a new name ")

status_label = ttk.Label(window, text="", foreground="red")
status_label.pack(padx=5, pady=5, fill="x")

# Start the GUI main loop
window.mainloop()