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
    #ask user for name of genre
    #ask user for description of genre
    #ask user for category (Fiction, Non-fiction, Reference, Periodicals)

def view_genre(genres_dict, genre_name):
    #get that genre from the dictionary
    #print the genre's details to the user

def view_all_genres(genres_dict):
    #iterate trhough the genres (values) in the dictionary
    #print the genre details to user