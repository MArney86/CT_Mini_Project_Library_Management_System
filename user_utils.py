class User:
    def __init__(self, name, id):
        self.__name = name
        self.__library_id = id
        self.__borrowed = []

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_library_id(self):
        return self.__library_id
    
    def set_library_id(self, id):
        self.__library_id = id

    def get_borrowed(self):
        return self.__borrowed
    
    def add_borrowed(self, book_name):
        self.__borrowed.append(book_name)

    def remove_borrowed(self, book_name)
        if book_name in self.__borrowed:
            self.__borrowed.remove(book_name)
        else:
            print(f"That title was not borrowed by {self.__name}")

def generate_library_id():
    #generate randomized library id
    #return new library id

def add_user(user_dict):
    #get new user's name
    #generate new user's library id
    #initialize new user to user dictionary with library id as key

def view_user_details(userdict):
    #check that user dictionary isn't empty
        #ask the operator for user name or library id
        #check if input is name of user or library id
        #if is library id
            #access user from dictionary
            #print user information to operator
        #if is user name
            #initialize found flag
            #initialize found list
            #iterate through users in dictionary
                #check that name matches
                    #set found flag to true
                    #add library id to found list
                #name doesn't match
                    #continue
            #if found and len(found list) == 1
                #print user details to operator
            #elif found and len(found list) > 1
                #print list of user name with attributed library ids and ask to choose a library id
            #else
                #notify operator that user is not found

def display_all_users(userdict):
    #iterate through users in the dictionary
        #print user's details to operator