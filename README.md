# 📞 Phone Book CLI App (Python)

A simple command-line phone book application built in Python using Object-Oriented Programming (OOP) principles. It supports basic CRUD operations: Create, Read, Update, and Delete contacts.

## ✨ Features

- 📇 Create new contacts with full information (name, phone, email, address, category)
- 🔍 Search for contacts by first name
- ✏️ Update contact details (including nested fields like address or email)
- 🗑️ Delete contacts from the list
- 📋 Display all saved contacts
- ✅ Built-in validation for phone numbers and emails
- 💾 Temporary in-memory data storage (no database or file persistence yet)

## 🧱 Project Structure

### Main Classes:
- **`Address`** – Stores contact's city, street, alley, and zipcode
- **`Category`** – Represents a contact category (family, friend, colleague, others)
- **`Contact_Info`** – Manages phone number and email with validation
- **`Person`** – Represents each contact with full details
- **`Phone_Book`** – Core class managing the list of contacts and all operations

## 🚀 How to Run

1. Make sure Python 3 is installed.
2. Save the code in a file, for example: `phonebook.py`
3. Run the app using your terminal or command prompt:
```bash
python phonebook.py
