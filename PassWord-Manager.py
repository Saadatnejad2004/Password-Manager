import os
import sys
import json
import argparse


PASSWORDS = "Passwords.json"

def load_passwords():
    if not os.path.exists(PASSWORDS):
        return []
    with open(PASSWORDS, "r") as f:
        return json.load(f)
    
def save_passwords(passes):
    with open(PASSWORDS, "w") as f:
        return json.dump(passes, f, indent = 2)
    
def add_passwords(place, username, password):
    My_Passes = load_passwords()
    My_Passes.append({"Place" : place, "Username" : username, "Password": password})
    save_passwords(My_Passes)
    print(f"\nAdded; You have an Account in {place} as {username} with {password} as your password")

def list_passwords():
    My_Passes = load_passwords()
    if not My_Passes:
        print("No PassWords yet")
        return
    
    for i , p in enumerate(My_Passes, 1):
        print()
        print(f"{i} - {p['Place']} | User:{p['Username']} & Pass:{p['Password']}")

def remove_passwords(index):
    My_Passes = load_passwords()

    if 0 <= index < len(My_Passes):
        removed = My_Passes.pop(index)
        save_passwords(My_Passes)

        print(f"Removed your account in: {removed['Place']}")

    else:
        print("Invalid number")

def main():

    while True:
        print("\nOptions: /add  /list  /remove  /quit")
        action = input("Choose an action: ").strip().lower()

        if action == 'quit':
            break
        
        elif action == 'add':
            plc = input("Enter your Account's Place: ")
            user = input("Enter your Username: ")
            pasw = input("Enter your Password: ")
            add_passwords(plc, user, pasw)
        
        elif action == 'list':
            list_passwords()
        
        elif action == 'remove':
            try:
                idx = int(input("Enter the Index number: "))
                remove_passwords(idx - 1)
            except ValueError:
                print("Invalid Index")
        else:
            print("Invalid Action")

def CLI():

    parser = argparse.ArgumentParser(description = "Write and save your Usernames and Passwords here")
    subparsers = parser.add_subparsers(dest = "command")

    # Add
    add_parser = subparsers.add_parser("add", help = "Add an Username and its Password")
    add_parser.add_argument("place", type = str, help = "write the name of site/app you have registerd")
    add_parser.add_argument("username", type = str, help = "write the username")
    add_parser.add_argument("password", type = int, help = "write the password")

    # List
    list_parser = subparsers.add_parser("list", help = "Show all the accounts")

    # Remove
    remove_parser = subparsers.add_parser("remove", help = "Remove the acounts out of Database")
    remove_parser.add_argument("index", type = int, help = "Write the Index number of your Account")

    args = parser.parse_args()

    if args.command == "add":
        add_passwords(args.place, args.username, args.password)
    elif args.command == "list":
        list_passwords()
    elif args.command == "remove":
        remove_passwords(args.index - 1)
    else:
        parser.print_help()


if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        CLI()
    else:
        main()