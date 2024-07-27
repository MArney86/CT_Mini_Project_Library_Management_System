class Genre:
    def __init__(self, name, descriptor, category):
        self.__name = name
        self.__descriptor = descriptor
        self.__category = category

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_description(self):
        return self.__descriptor
    
    def set_description(self, description):
        self.__descriptor = description

    def get_category(self):
        return self.__category
    
    def set_category(self, category):
        self.__category = category


def add_genre(genres_dict):
    name = input("Please enter the Genre name : ") #ask user for name of genre
    description = input("Please enter a description for the Genre: ") #ask user for description of genre
    while True: #loop in case of invalid input
        category = ("Please enter the category (Fiction, Non-fiction, Reference, Periodicals) of the Genre: ").strip() #ask user for category (Fiction, Non-fiction, Reference, Periodicals)
        if category == "Fiction" or category == "Non-fiction" or category == "Reference" or category == "Periodicals": #check that a valid category was entered
            genres_dict[name.lower()] = Genre(name, description, category) #add new genre to genre dictionary using the name as a key for quicker searching
            break #end loop
        else:
            print("That category is invalid. Please enter a valid category")

def view_genre(genres_dict, name):
    if name.lower() in genres_dict.keys(): #check name is in dictionary keys
        print(f"\nName: {genres_dict[name.lower()].get_name()}") #print genre name to operator
        print(f"Description: {genres_dict[name.lower()].get_description()}") #print description to operator 
        print(f"Category: {genres_dict[name.lower()].get_category()}") #print category to operator
    else: #genre doesn't exist in keys
        print("That genre is not in the library's list of genres.") #notify user that genre is not in library
        choice = input("Would you like to add the genre? (yes/no): ").strip() #offer to add
        if choice == 'yes': #operator chooses to add
            add_genre(genres_dict) #add genre

def view_all_genres(genres_dict):
    if genres_dict: #verify that there are genres in dictionary
        for name in genres_dict.keys(): #iterate through the genres in the dictionary
            view_genre(genres_dict, name)#print the genre details to user