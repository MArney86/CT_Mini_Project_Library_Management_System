import genre_utils as GU
import datetime
import user_utils as UU

class Book(GU.Genre):
    def __init__(self, title, descriptor, category, author, isbn, pubdate)
        self.__name = title
        self.__descriptor = descriptor
        self.__category = category
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = pubdate
        self.__status = True

    def get_author(self):
        return self.__author
    
    def set_author(self, author):
        self.__author = author

    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_publication_date(self):
        return self.__publication_date
    
    def set_publication_date(self, pubdate):
        self.__publication_date = pubdate

    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        self.__status = status

def isbn_from_title(book_dict, title):
    #initialize found flag
    #initialize found list
        #iterate through books in dictionary
            #check that title matches
                #set found flag to true
                #add isbn to found list
            #name doesn't match
                #continue
        #if found and len(found list) == 1
            #return value of __isbn from found user
        #elif found and len(found list) > 1
            #print list of titles with attributed authors and isbn ask to choose a title
        #else
            #notify operator that book is not found

def add_book(book_dict):
    #get title from operator
    #get description from operator
    #get category from operator
    #get author from operator
    #get isbn from operator
    #get publication date from operator
    #create new book in book dictionary with isbn as identifier

def borrow_book(book_dict):
    #get user name or library id from operator
    #get title or isbn of book from operator
    #check status of book
    #if status is available (True)
        #user.add_borrowed(isbn)
        #book.set_status(False)
    #else
        #tell operator that that book is unavailable

def return_book(book_dict):
    #get user name or library id from operator
    #get book title or isbn from operator
    #check status of book
    #if status is unavailable(False)
        #user.remove_borrowed()
        #book.set_status(True)
    #else
        #notify operator that that book is already returned

def display_book(book_dict, isbn):
    #get book data from book dictionary with isbn
    #print to user the book data

def search_books(book_dict):
    #ask user what criteria they want to search
    #if name:
        #isbn_from_title()
        #display_book()
    #elif author:
        #iterate through books in dictionary
            #check that author matches
                #set found flag to true
                #add isbn to found list
             #author doesn't match
                #continue
        #if found and len(found list) == 1
            #display_book(isbn from found list)
        #elif found and len(found list) > 1
            #print list of titles with attributed authors and isbn ask to choose a title
            #display_book(isbn)
        #else
            #notify operator of author not being found
    #elif isbn
        #display_book(isbn)

def display_all_books(book_dict):
    #iterate through book dictionary
        #display_book(isbn key) 