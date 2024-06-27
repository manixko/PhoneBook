import os
import time as tm

'''
CRUD 
Create, Read, Update, Delete
'''

class Address:
    def __init__(self, city, street, alley, zipcode) -> None:
        self.city = city
        self.street = street
        self.alley = alley
        self.zipcode = zipcode

    def __str__(self) -> str:
        return f"Adrress = {self.city}-{self.street}-{self.alley} , Zipcode = {self.zipcode} "

class Category:
    def __init__(self, category) -> None:
        self.category = category

    def __str__(self) -> str:
        return f"{self.category} "


class Contact_Info:
    def __init__(self, phone_number = " ") -> None:
        self.phone_number = phone_number
        self._email = " "
    
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, num):
        if len(num) == 11:
            self._phone_number = num
            print("phone number added")
            tm.sleep(1)
            os.system("cls")
        else:
            self._phone_number = " "
            print("phone number must be 11 character")
            tm.sleep(1)
            os.system("cls")
            

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        import re as r
        regex = "[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if r.match(regex, email):
            self._email = email
        else:
            print("email is not valid")
            self._email = "empty@mail.com"

class Person:
    def __init__(self,id, first_name, last_name, category, contact_info) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.category = Category(category)
        self.contact_info = Contact_Info(contact_info)
        self.address = None

    def __str__(self) -> str:
        return f"contact id = {self.id}\nfirst name = {self.first_name} , last name = {self.last_name}\
            \nphone number = {self.contact_info.phone_number}\
            \ncategory = {self.category}\
            \nemail = {self.contact_info.email}\
            \n{self.address} "


class Phone_Book:
    records = []

    def Create():
        id = len(Phone_Book.records)+1
        first_name = input("please enter first name :")
        last_name = input("please enter last name :")
        print("please choose your category\n(1)family\n(2)friend\n(3)coleague\n(4)others")
        category = input("please choose one option :")
        if category == "1":
            category = "family"
        elif category == "2":
            category = "friend"
        elif category == "3":
            category = "coleague"
        elif category == "4":
            category = "others"
        contact_info = input("please enter number :")
        obj = Person(id, first_name, last_name, category, contact_info)
        question = input("do you want to create adddress for your contact (yes/no):")
        if question == "yes" or question == "y":
            city = input("please enter city :")
            street = input("please enter street :")
            alley = input("please enter alley :")
            zipcode = input("please enter zipcode :")
            obj.address = Address(city, street, alley, zipcode) 
        else:
            obj.address = Address(" ", " ", " ", " ")
        question2 = input("do you want to add an email (yes/no):")
        if question2 == "yes" or question2 == "y":
            email = input("please enter a valid email :")
            obj.contact_info.email = email
        else:
            obj.contact_info.email = "empty@mail.com"


        print("your contact successfully added")
        Phone_Book.records.append(obj)

    def Search(info):
        result = " "
        for contact in Phone_Book.records:
            if info == contact.first_name:
                result = contact
                break
        if result == " ":
            print("contact not found")
        else:
            print("-"*22)
            print(result)
            print("-"*22)


    

    def ShowAll():
        if len(Phone_Book.records)>0:
            for contacts in Phone_Book.records:
                print(contacts)
                print("-"*22)
        else:
            print("there is no contact !")

    def Update(mark):
        error = " "
        for contact in Phone_Book.records:
            if mark == contact.first_name:
                error = "done"
                print((Phone_Book.records[contact.id]))
                print("(1) first name ")
                print("(2) last name ")
                print("(3) phone number ")
                print("(4) email ")
                print("(5) address ")
                print("(0) exit ")
                Q = input("Which option do want to update :")
                exit = 2
                while exit != 0:
                    if Q == "1":
                        new_first_name = input("please enter new first name :")
                        (Phone_Book.records[contact.id]).first_name = new_first_name
                        break
                    elif Q == "2":
                        new_last_name = input("please enter new last name :")
                        (Phone_Book.records[contact.id]).last_name = new_last_name
                        break
                    elif Q == "3":
                        new_phone_number = input("please enter new phone number :")
                        (Phone_Book.records[contact.id]).contact_info.phone_number = new_phone_number
                        break
                    elif Q == "4":
                        new_email = input("please enter new email :")
                        (Phone_Book.records[contact.id]).contact_info.email = new_email
                        break
                    elif Q == "5":
                        os.system("cls")
                        print("(1) city")
                        print("(2) street")
                        print("(3) alley")
                        print("(4) zipcode")
                        print("(5) exit")
                        Qe = input("please choose an option :")
                        exits = 2
                        while exits != 0:
                            if Qe == "1":
                                new_city = input("please enter new city for address :")
                                (Phone_Book.records[contact.id]).address.city = new_city
                                break
                            elif Qe == "2" :
                                new_street = input("please enter new street for address :")
                                (Phone_Book.records[contact.id]).address.street = new_street
                                break
                            elif Qe == "3" :
                                new_alley = input("please enter new ally for address :")
                                (Phone_Book.records[contact.id]).address.alley = new_alley
                                break
                            elif Qe == "4" :
                                new_zipcode = input("plaese enter new zipcode for address :")
                                (Phone_Book.records[contact.id]).address.zipcode = new_zipcode
                                break
                            elif Qe == "6" :
                                exits = 0
                                break
                        break
                    elif Q == "0":
                        exit = 0
                        break
                print("contact successfully updated")
        if error == " ":
            print("contact does not exist")


    def Reomve(info):
        for contact in Phone_Book.records:
            if info == contact.first_name:
                id = contact.id 
                del Phone_Book.records[id]
                print("contact successfully deleted")
                break
            else:
                print("there is something wrong")






# menu

def text():
    print("-"*22)
    print("(1) create contact")
    print("(2) search contact")
    print("(3) delete contact")
    print("(4) show all contacts")
    print("(5) update contact")
    print("(0) exit")
    print("-"*22)

def menu():
    exit = 0
    while exit != 2:
        text()
        num = input("choose an option :")
        if num == "1":
            os.system("cls")
            print("| Create a contact |")
            Phone_Book.Create()
            tm.sleep(2)
            os.system("cls")
        elif num == "2":
            os.system("cls")
            print("| Search a contact |")
            name = input("Please enter contact name :")
            Phone_Book.Search(name)
            Q = input("Do you want to back to menu? (yes/no):")
            if Q == "yes" or Q == "y":
                os.system("cls")
            else:
                exit = 2
        elif num == "3":
            os.system("cls")
            print("| Remove a contact |")
            Q = input("Which contact do want to remove(enter name) :")
            Phone_Book.Reomve(Q)
            tm.sleep(2)
            os.system("cls")
        elif num == "4":
            os.system("cls")
            print("| Show all contact |")
            Phone_Book.ShowAll()
            Q = input("Do you want to back to menu? (yes/no):")
            if Q == "yes" or Q == "y":
                os.system("cls")
            else:
                exit = 2
        elif num == "5":
            os.system("cls")
            print("| Update a contact |")
            mark = input("please enter your contact name :")
            Phone_Book.Update(mark)
            tm.sleep(2)
            os.system("cls")
        elif num == "0":
            exit = 2
        
menu()