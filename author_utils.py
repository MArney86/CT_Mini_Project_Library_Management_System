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
    #get name from user
    #get biography from user
    #add author to author dictionary using name as key for quicker searching

def view_author(author_dict, name):
    #check name is in keys of dictionary
        #print details of author to user
    #tell user author doesn't exist if not in keys
        #offer to add
            #add_author()

def view_all_authors(author_dict):
    #check that there are authors in the dictionary
        #iterate through authors in dictionary
            #print details of author to user