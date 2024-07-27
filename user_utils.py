import string
import random

class User:
    def __init__(self, name, id):
        self._name = name
        self._library_id = id
        self._borrowed = []

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_library_id(self):
        return self._library_id
    
    def set_library_id(self, id):
        self._library_id = id

    def get_borrowed(self):
        return self._borrowed
    
    def add_borrowed(self, book_dict, isbn):
        self._borrowed.append(isbn)
        print(f"{self._name}(ID:{self._library_id}) has borrowed {book_dict[isbn].get_name()} by {book_dict[isbn].get_author()}")

    def remove_borrowed(self, book_dict, isbn):
        if isbn in self._borrowed:
            self._borrowed.remove(isbn)
        else:
            print(f"That title was not borrowed by {self._name}")

def generate_library_id():
    id = ''.join(random.choices(string.digits, k=12))#generate randomized library id
    return id #return new library id

def add_user(user_dict):
    name = input("Please enter the name of the user you'd like to add: ").strip() #get new user's name
    id = generate_library_id() #generate new user's library id

    while True: #loop incase id already exists
        if id in user_dict.keys(): #check if id already in use
            id = generate_library_id
            break
        else: #id not already in use
            break #end loop

    user_dict[id] = User(name, id) #initialize new user to user dictionary with library id as key

def view_user_details(user_dict, book_dict):
    if user_dict: #check that user dictionary isn't empty
        while True: #loop in case of invalid input
            query = input("Please input the name or Library ID of the user you'd like to view: ").strip() #ask the operator for user name or library id
            if not query.isnumeric(): #check if input is not Library ID
                query = get_id_from_name(user_dict, query) #set query to the id associated with the name
                display_user(user_dict, book_dict, query) #print user details to operator
                break #end loop
            elif query.isnumeric(): #is library id
                display_user(user_dict, book_dict, query)#print user information to operator
                break #end loop
            else: #input is neither letters or numbers
                print("invalid input, please try again") #notify user of invalid input 

def display_user(user_dict, book_dict, id): 
    if id in user_dict.keys(): #check for user id in the user dictionary
        print(f"\nName: {user_dict[id].get_name()}") #print user name
        print(f"Library ID: {user_dict[id].get_library_id()}") #print user Library ID
        print("Currently borrowed books:") #header for borrowed books
        temp = user_dict[id].get_borrowed() #store the borrowed books list
        if temp: #check that list is not empty
            for book in temp: #iterate through the list
                print(f'"{book_dict[book].get_title()}" by {book_dict[book].get_author()}') #print the title and author of the book iterated
        else: #list is empty
            print("This user currently does not have any books borrowed.") #print that there are no borrowed books currently
        print("\n") #spacer for formatting
    else: #user id is not in the user dictionary
        print("The user id you provided is not in use by any users") #notify operator of lack of user with that id

        
def display_all_users(user_dict, book_dict):
    if user_dict:
        for id, user in user_dict.items(): #iterate through users in the dictionary
            print(f"\nName: {user_dict[id].get_name()}") #print user name
            print(f"Library ID: {user_dict[id].get_library_id()}") #print user Library ID
            print("Currently borrowed books:") #header for borrowed books
            temp = user_dict[id].get_borrowed() #store the borrowed books list
            if temp: #check that list is not empty
                for book in temp: #iterate through the list
                    print(f'"{book_dict[book].get_title()}" by {book_dict[book].get_author()}') #print the title and author of the book iterated
            else: #list is empty
                print("This user currently does not have any books borrowed.") #print that there are no borrowed books currently
    else:
        print("There are currently no users registered at the library")

def get_id_from_name(user_dict, name):
    found = False #initialize found flag
    found_list = [] #initialize found list
    for id, user in user_dict.items(): #iterate through users in dictionary
        if name.lower() == user.get_name().lower(): #check that name matches
            found = True #set found flag to true
            found_list.append(id) #add library id to found list
        else: #name doesn't match
            continue #continue
    if found and len(found_list) == 1: #check that we found users and that there is only 1
        return found_list[0] #return value of __library_id from found user
    elif found and len(found_list) > 1: #found and more than 1 user
        for id in found_list: #iterate through the list
            print(f"Name: {user_dict[id].get_name()}") #print user name
            print(f"Library ID: {user_dict[id].get_library_id()}") #print the library id
        while True:
            choice = input("Please input the Library ID of the user you were looking for: ").strip()
            if choice in found_list:
                return choice
            else:
                print("Invalid choice. Please Try again")
    else: #no found users
            print("That name does not have a Library ID") #notify operator that user is not found