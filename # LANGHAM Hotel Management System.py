# LANGHAM Hotel Management System
# Author: Sujan B K
# Description: Console-based hotel room management system with File I/O
# Date: 2025-06-16

import os
from datetime import datetime

# Dictionary to store room details
rooms = {}

# File name 
STUDENT_ID = "850003525" 
DATA_FILE = f"LHMS_{850003525}.txt"

# ---------------- MENU FUNCTIONS ----------------

def display_menu():
    print("\nLANGHAM Hotel Management System")
    print("1. Add Room")
    print("2. Delete Room")
    print("3. Display Room Details")
    print("4. Allocate Room")
    print("5. Display Room Allocation Details")
    print("6. Billing and Deallocation")
    print("7. Save Room Allocation to File")
    print("8. Display Room Allocation from File")
    print("9. Backup and Clear Allocation File")
    print("0. Exit Application")

# ---------------- BASIC OPERATIONS ----------------

def add_room():
    room_no = input("Enter Room Number: ")
    if room_no in rooms:
        print("Room already exists!")
    else:
        room_type = input("Enter Room Type (Single/Double/Deluxe): ")
        features = input("Enter Room Features (e.g. TV, AC, Free WiFi): ")
        rooms[room_no] = {
            "type": room_type,
            "features": features,
            "status": "Available",
            "customer": None,
            "bill": 0
        }
        print(f"Room {room_no} added successfully.")

def delete_room():
    room_no = input("Enter Room Number to Delete: ")
    if room_no in rooms:
        del rooms[room_no]
        print(f"Room {room_no} deleted successfully.")
    else:
        print("Room not found!")

def display_room_details():
    if not rooms:
        print("No rooms available.")
    else:
        for room_no, data in rooms.items():
            print(f"\nRoom No: {room_no}")
            print(f"Type: {data['type']}")
            print(f"Features: {data['features']}")
            print(f"Status: {data['status']}")

def allocate_room():
    room_no = input("Enter Room Number to Allocate: ")
    if room_no in rooms:
        if rooms[room_no]["status"] == "Available":
            customer = input("Enter Customer Name: ")
            rooms[room_no]["customer"] = customer
            rooms[room_no]["status"] = "Occupied"
            print(f"Room {room_no} successfully allocated to {customer}.")
        else:
            print("Room is already occupied.")
    else:
        print("Room not found!")

def display_allocation_details():
    allocated = False
    for room_no, data in rooms.items():
        if data["status"] == "Occupied":
            allocated = True
            print(f"\nRoom No: {room_no}")
            print(f"Allocated to: {data['customer']}")
    if not allocated:
        print("No rooms are currently allocated.")

def billing_deallocation():
    room_no = input("Enter Room Number to Deallocate: ")
    if room_no in rooms and rooms[room_no]["status"] == "Occupied":
        try:
            days = int(input("Enter number of days stayed: "))
            rate_per_day = 200
            total_bill = days * rate_per_day
            customer = rooms[room_no]["customer"]
            print(f"Customer: {customer}")
            print(f"Total Bill: ${total_bill}")
            rooms[room_no]["customer"] = None
            rooms[room_no]["status"] = "Available"
            rooms[room_no]["bill"] = 0
            print(f"Room {room_no} is now deallocated and available.")
        except ValueError:
            print("Invalid input. Days must be a number.")
    else:
        print("Room not found or is not occupied.")

# ---------------- FILE I/O OPERATIONS ----------------

def save_allocation_to_file():
    try:
        with open(DATA_FILE, "w") as file:
            for room_no, data in rooms.items():
                line = f"{room_no},{data['type']},{data['features']},{data['status']},{data['customer'] or 'None'}\n"
                file.write(line)
        print(f"Room data saved to {DATA_FILE}")
    except IOError:
        print("Error saving to file.")

def display_allocation_from_file():
    if not os.path.exists(DATA_FILE):
        print("Data file does not exist.")
        return
    try:
        with open(DATA_FILE, "r") as file:
            content = file.read()
            print("\n--- Room Allocation Data from File ---")
            print(content)
    except IOError:
        print("Error reading file.")

def backup_and_clear_file():
    if not os.path.exists(DATA_FILE):
        print("Main data file does not exist.")
        return
    try:
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"LHMS_{STUDENT_ID}_Backup_{now}.txt"
        with open(DATA_FILE, "r") as original_file:
            data = original_file.read()
        with open(backup_filename, "a") as backup_file:
            backup_file.write(data)
        # Clear the original file
        open(DATA_FILE, "w").close()
        print(f"Data backed up to {backup_filename} and original file cleared.")
    except IOError:
        print("Error during backup or clearing.")

def exit_application():
    print("Thank you for using LANGHAM Hotel Management System.")
    exit()

# ---------------- MAIN PROGRAM ----------------

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (0–9): ")
        if choice == "1":
            add_room()
        elif choice == "2":
            delete_room()
        elif choice == "3":
            display_room_details()
        elif choice == "4":
            allocate_room()
        elif choice == "5":
            display_allocation_details()  # <-- Fixed the syntax error here
        elif choice == "6":
            billing_deallocation()
        elif choice == "7":
            save_allocation_to_file()
        elif choice == "8":
            display_allocation_from_file()
        elif choice == "9":
            backup_and_clear_file()
        elif choice == "0":
            exit_application()
        else:
            print("Invalid choice. Please enter a number between 0 and 9.")

# Run the system
if __name__ == "__main__":
    main()
