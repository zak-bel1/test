import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if "@uca.ac.ma" not in username or password == "":
        messagebox.showerror("Error", "Please enter both username and password.")
        return
    
    # Placeholder for authentication logic (e.g., check against a database)
    print(f"Username: {username}, Password: {password}")
    messagebox.showinfo("Success", "Login successful!")

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")  # Hide password input
password_entry.pack(pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Run the application
root.mainloop()
