class Author:
    def __init__(self, name, bio):
        self.__name = name
        self.__biography = bio

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_biography(self):
        return self.__biography
    
    def set_biography(self, bio):
        self.__biography = bio

def add_author(author_dict):
    name = input("Please enter the name of the Author you wish to add: ").strip() #get name from user
    bio = input("Please enter a biography for the Author you wish to add: ").strip() #get biography from user
    author_dict[name.lower()] = Author(name, bio) #add author to author dictionary using name as key for quicker searching
    return name.lower()

def view_author_details(author_dict):
    while True:
        name = input("Please enter that name of the author you'd like to view: ").strip() #get name of author from operator
        if name.lower() in author_dict.keys(): #check name is in keys of dictionary
            display_author(author_dict, name) #display the author's information
            break #end loop
        else: #author doesn't exist in keys
            print("That Author's name is not in the library's list of authors.") #notify user that author is not in library
            choice = input("Would you like to add the Author? (yes/no): ").strip() #offer to add
            if choice == 'yes': #operator chooses to add
                add_author(author_dict) #add author
            else:
                break

def display_author(author_dict, name):
    print(f"\nName: {author_dict[name.lower()].get_name()}") #print author name to operator
    print(f"Biography: {author_dict[name.lower()].get_biography()}") #print author's biography to operator

def display_all_authors(author_dict):
    if author_dict: #check that there are authors in the dictionary
        for name in author_dict.keys(): #iterate through authors in dictionary
            display_author(author_dict, name) #print details of author to user
    else:
        print("There are currently no authors in the library records")