# 🔐 Password Manager CLI

A secure and lightweight **Command-Line Password Manager** written in Python.  
This program allows you to **store, list, and remove your account credentials** locally in a JSON file — protected by a **master password lock system**.

No external dependencies. 100% Python Standard Library.  
Works on **Windows**, **macOS**, and **Linux**.

---

## 🧠 Project Overview

This project provides a simple, privacy-focused password manager that runs entirely in your terminal.

### 💡 How It Works
1. When you run the program for the **first time**, it asks you to create a **master password**.  
   This password protects your entire database and is stored **securely as a hash**, not as plain text.  
2. Every time you launch the program afterward, you must enter that password before you can access your saved accounts.  
3. You can then use the app to:
   - ➕ Add new accounts (with site, username, and password)
   - 📋 List all stored accounts
   - ❌ Remove any account you no longer need

All data is stored locally in a file called **`Passwords.json`**, and your master password hash is stored in **`master.json`**.

---

## 🚀 Features

✅ **Master Password Lock** – You set it once, and it’s required every time you open the app.  
✅ **Interactive and CLI Modes** – Use a menu interface or command-line arguments.  
✅ **Local JSON Storage** – Lightweight and simple, no external database.  
✅ **Data Safety** – Master password is stored as a SHA-256 hash, never as plain text.  
✅ **Cross-Platform Support** – Works anywhere Python runs.

---

## 📦 Project Structure

PasswordManager/
│
├── main.py # Main Python script
├── Passwords.json # Stores account data (auto-created)
├── master.json # Stores hashed master password
└── README.md # Documentation

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Saadatnejad2004/Password-Manager.git
cd Password-Manager
```
2️⃣ Run the Program
Simply run:
```bash
python main.py
```
🔒 Master Password Setup (First Time)
When you run the program for the first time:

No master password found! Let's create one.
Create a master password: ****
Confirm it: ****
Master password set successfully!
The program will create a file called master.json that securely stores a hashed version of your master password.
From now on, every time you start the program, you’ll see:

Enter your master password: ****
Access granted ✅
If you enter it incorrectly 3 times, the program exits for security.

## 💻 How to Use
The Password Manager works in two different modes:

🧭 1. Interactive Mode
Run the program without arguments:
```bash
python main.py
```
You’ll see:

Options: /add  /list  /remove  /quit
➕ Add a New Account
Choose /add and enter:

Enter your Account's Place: Instagram
Enter your Username: amir
Enter your Password: myPass123
Added; You have an Account in Instagram as amir with myPass123 as your password
📋 List All Accounts
Choose /list to view your saved accounts:

1 - Instagram | User: amir & Pass: myPass123
2 - Gmail | User: myemail@gmail.com & Pass: secret456
❌ Remove an Account
Choose /remove and type the account’s index number:

Enter the Index number: 1
Removed your account in: Instagram
🚪 Quit the Program
Choose /quit to exit the app.

🧾 Example Run

Enter your master password: ****
Access granted ✅

Options: /add  /list  /remove  /quit
Choose an action: add
Enter your Account's Place: GitHub
Enter your Username: amir-hs
Enter your Password: mySecurePass
Added; You have an Account in GitHub as amir-hs with mySecurePass as your password.


🧩 Future Improvements
🔐 Encrypt stored passwords (not just hash the master password)

🧱 Add password strength checking

☁️ Optional cloud or local encryption key support

⚙️ Generate random passwords automatically

🧑‍💻 Author
Amir Hossein Saadatnejad
💻 Passionate about Python, System Programming, and Secure Software Design.
⭐ Feel free to fork, star, and contribute to this project!

📜 License
This project is open-source under the MIT License.
You are free to use, modify, and distribute it — just give proper credit.

🌟 Show your support
If you found this helpful, please give the repository a ⭐ star on GitHub to help others find it!
