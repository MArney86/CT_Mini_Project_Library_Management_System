import genre_utils as gu
import datetime as dt
import user_utils as uu

class Book(GU.Genre):
    def __init__(self, name, descriptor, category, title, author, isbn, pubdate)
        self.__name = name
        self.__descriptor = descriptor
        self.__category = category
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = pubdate
        self.__status = True
    
    def get_title(self): #getter for __title
        return self.__title #return value of __title
    
    def set_title(self, title): #setter for __title
        self.__title = title #change value of __title

    def get_author(self): #getter for __author
        return self.__author #return value of __author
    
    def set_author(self, author): #setter for __author
        self.__author = author #change value of __author

    def get_isbn(self): #getter for __isbn
        return self.__isbn #return value of __isbn
    
    def set_isbn(self, isbn): #setter fro __isbn
        self.__isbn = isbn #change value of __isbn

    def get_publication_date(self): #getter for __publication_date
        return self.__publication_date #return value of __publication_date
    
    def set_publication_date(self, pubdate): #setter for __publication_date
        self.__publication_date = pubdate #change value of __publication_date

    def get_status(self): #return value of __status as either 'Available' or 'Borrowed'
        if self.get_status: #check if __status is True (available)
            return "Available"  #return "Available"
        else: #__status is False
            return "Borrowed" #return "Borrowed"
    
    def set_status_borrowed(self): #setter for setting __status to borrowed
        if not self.__status: #check if __status isn't already borrowed
            print("That book has already been borrowed") #notify operator that __status is already set to borrowed
        else: #__status is Available
            self.__status = False #change __status to borrowed

    def set_status_available(self): #setter for setting __status to Available
        if self.__status: #check if __status is already set to Available
            print("That book is already available") #notify operator of __status already being set to Available
        else: #__status is borrowed
            self.__status = True #change __status to available

def isbn_from_title(book_dict, title): #function to return the isbn of a book by its title
    found = false #initialize found flag
    found_list = [] #initialize list of books with the searched title
    for isbn, book in book_dict.items(): #iterate through the books in the book dictionary
        if book.get_title().lower() == title.lower(): #check title of iterated book ignoring capitalization
            found = True #set found flag to True
            found_list.append(isbn) #add isbn of found book to found list
        else: #no match
            continue #continue loop
    if found and len(found_list) == 1 #test if books found and there is only one in the list
        return found_list[0] #return value of isbn from found book
    elif found and len(found_list) > 1 #test if books are found and there are more than 1
        print(f"\nBooks with title {title} found:") #iterate through found books
        counter = 1 #counter to keep track of location for user choice 
        for book in found_list: #iterate through found list
            print(f'{counter}.: "{book_dict[book].get_title()}" by {book_dict[book].get_author()} published on {book_dict[book].get_publication_date().strftime("%B %d, %Y")}') #print details of book for user to choose from
            counter += 1 #update counter
        while True: #loop in case of invalid inputs
            choice = input(f'Please choose the number of the particular book with title "{title}" you were looking for') #ask user for their choice
            try: #error handling
                if int(choice) > 0 and int(choice) <= len(found_list): #verify valid choice
                    return found_list[int(choice) - 1] #return chosen isbn
                else: #invalid choice
                    print("That was not a valid choice. Please try again") #notify operator of invalid choice
            except TypeError: #invalid input type error
                print("Only inputs of the number of your choice accepted. Please try again") #notify operator of error
            except ValueError: #nonsensical number input error
                print("That input does not map to a number. Please try again") #notify operator of error
            except Exception: #general exception
                print("Unexpect error occurred. Please try again") #notify operator of error
    else: #no books found
        print("That title has returned no matching books") #notify operator that book is not found
        return False
    
def is_valid_date(user_date): #function to validate date inputs
    result = True #initialize returned value to true

    try: #error handling
        month_str, day_str, year_str = user_date.split('/') #split input date
        try: #more error handling
            dt.date(year = int(year_str), month = int(month_str), day = int(day_str)) #attempt to add values to a date object
        except ValueError: #value error from date() attempt
            result = False #return value of false
    except ValueError: #value error from split attempt
        result = False #return value of false

    return result #no errors, return true value

def add_book(book_dict, genre_dict):
    title = input("Please enter the title of the book you'd like to add: ") #get title from operator
    author = input("Please enter the Author of the book you'd like to add: ")#get author from operator
    isbn = input("Please enter the ISBN for the book you'd like to add: ")#get isbn from operator

    while True: #loop incase of invalid inputs
        pub_date = input("Please enter the publication date of the book you'd like to add (MM/DD/YYYY format): ") #get publication date from operator
        if is_valid_date(pub_date): #check that input is valid
            pub_date = dt.date(pub_date) #add publication date as date object
            break #end loop
        else: #invalid input
            print("Invalid date, please try again") #notify operator and continue loop

    while true: #loop incase of invalid inputs
        print("Please choose a genre for the book: ") #ask user for the book genre
        if genre_dict: #ensure there are already genres in the genre dictionary
            for genre in genre_dict.keys(): #iterate through genre names as keys in genre dictionary
                print(genre_dict[genre].get_name()) #print the iterated genre
            choice = input("Please input the genre of the book you're adding to the library: ") #get chosen genre from operator
            if choice.lower in genre_dict.keys(): #check that the user input is in genre dictionary
                name = genre_dict[choice.lower()].get_name() #set name placeholder
                description = genre_dict[choice.lower()].get_description() #set descriptor placeholder
                category = genre_dict[choice.lower()].get_category() #set category placeholder
                break #end loop
            else: #chosen genre is not in genre dictionary
                print("That genre isn't in the list of available genres. Please add genre to continue adding book.") #notify operator and ask them to add genre to dictionary
                gu.add_genre(genre_dict) #add genre to the genre dictionary then continue loop
        else: #no genres in dictionary
            print("There are no genres added to the library currently. Please add genre to continue adding book.") #notify operator and ask them to add genre to dictionary
            gu.add_genre(genre_dict) #add genre to the genre dictionary then continue loop
    book_dict[isbn] = Book(name, description, category, title, author, isbn, pub_date) #create new book in book dictionary with isbn as identifier

def borrow_book(user_dict, book_dict):
    user = input("Please enter the name or Library ID of the user checking out the book") #get user name or library id from operator
    query = input("Please enter the ISBN or title of the book you'd like to borrow: ") #get title or isbn of book from operator
    if user.isalnum() and not query.isnumeric():
        user = get_id_from_name(user_dict, user)

    if query.isalnum() and not query.isnumeric():
        query = isbn_from_title(book_dict, query)
    
    if book_dict[query].get_status(): #check status of book is available
        user_dict[user].add_borrowed(book_dict, query) #add book to user's borrow list
        book_dict[query].set_status_borrowed()#change book status to borrowed
        print(f'"{book_dict[query].get_title()}' has been borrowed by user {user_dict[user].get_name()}) #notify operator of success of borrowing title
    else: #status borrowed
        print(f'"{book_dict[query].get_title()}" is already borrowed out') #notify operator that that book is unavailable

def return_book(book_dict):
    user = input("Please enter the name or Library ID of the user checking out the book") #get user name or library id from operator
    query = input("Please enter the ISBN or title of the book you'd like to borrow: ") #get title or isbn of book from operator
    if user.isalnum() and not query.isnumeric():
        user = get_id_from_name(user_dict, user)

    if query.isalnum() and not query.isnumeric():
        query = isbn_from_title(book_dict, query)

    if not book_dict[query].get_status(): #check status of book is not available
        user_dict[user].remove_borrowed(book_dict, query) #remove book from user's borrow list
        book_dict[query].set_status_available()#change book status to available
        print(f'"{book_dict[query].get_title()}' has been borrowed by user {user_dict[user].get_name()}) #notify operator of success of returning title
    else: #status available
        print(f'"{book_dict[query].get_title()}" is already returned/available') #notify operator that that book is already returned/available

def display_book(book_dict, isbn):
    if isbn in book_dict.keys():
        print(f"\n Title: {book_dict[isbn].get_name()}")
        print(f"Author {book_dict[isbn].get_author()}")
        print(f"Genre: {book_dict[isbn].get_name()}")
        print(f"ISBN: {book_dict[isbn].get_isbn()}:")
        print(f"Publication Date: {book_dict[isbn].get_publication_date()}") #print book data to operator
    else:
        print("The title chosen to display does not exist")

def search_books(book_dict):
    while True: #loop in case of invalid input
        choice = input("\nSearch criteria choices:\n1. By Book Title\n2. By Book Author\n3. By ISBN\n4. By Genre\n5. Return to previous menu\nWhich criteria would you like to search for a book by?: ") #ask user what criteria they want to search
        
        if choice == '1': #search by title
            query = input("Please input the title you are searching for: ").strip() #get title to search from operator
            query = isbn_from_title(book_dict, query) #convert title to isbn
            display_book(book_dict, query) #display the title chosen by the operator
            break #end loop
        
        elif choice == '2': #search by author
            query = input("What is the name of the Author you'd like to search for books from?") #get author to search from operator
            found = False #initialize found flag
            found_list = [] #initialize list of found books
            for isbn, book in book_dict.items(): #iterate through books in dictionary
                if book.get_author().lower() == query.lower:#check that author matches
                    found = True #set found flag to true
                    found_list.append(isbn) #add isbn to found list
                else: #author doesn't match
                    continue #continue
            if found and len(found_list) == 1: #check that titles found and there is only one
                display_book(book_dict, found_list[0])
            elif found and len(found_list) > 1: #titles found and more than one
                print(f"Titles available from author {query}:") #heading for found titles
                for book in found_list: #iterate found books
                    print(f'"{book_dict[book].get_title()}" by {book_dict[book].get_author()}, ISBN: {book_dict[book].get_isbn()}') #print title with attributed authors and isbn 
                book_choice = input("Please enter the ISBN of the title you wish to view: ").strip() #ask to choose a title
                display_book(book_dict, book_choice) #display the chose title
            else: #none found
                print("There were no books by that author found in the library") #notify operator of author not being found
        
        elif choice == '3': #search isbn
            query = input("Please input the ISBN of the title you're searching for: ").strip() #get ISBN from operator
            display_book(book_dict, query) #display_book(isbn)
        
        elif choice == '4': #seach by Genre
            query = input("Please enter the genre you'd like to search for: ").strip()
            found = False #found flag initialized to false
            found_list = [] #found list initialized
            for isbn, book in book_dict.items():#iterate through books
                if book.get_name().lower == query.lower() #check for genre name in book
                    found = True#set found flag to true
                    found_list.append(isbn)#add isbn to found list
                else: #no match
                    continue#continue
            if found and len(found_list) == 1: #check that titles found and there is only one
                display_book(found_list[0]) #display book in list
            elif found and len(found_list) > 1:
                print(f"Titles available in genre {query}:") #heading for found titles
                for book in found_list: #iterate found books
                    print(f'"{book_dict[book].get_title()}" by {book_dict[book].get_author()}, ISBN: {book_dict[book].get_isbn()}') #print title with attributed authors and isbn 
                book_choice = input("Please enter the ISBN of the title you wish to view: ").strip() #ask to choose a title
                display_book(book_dict, book_choice) #display the chose title#print list of titles with attributed authors and isbn to choose title
            else: #none found
                print(f"There were no books found in the genre {query}")

        elif choice == '5': #leave
            break
        
        else:
            print("That was an invalid choice. Please try again")

def display_all_books(book_dict):
    print("\n Books in the library: ")
    for book in book_dict.values(): #iterate through book dictionary
        print(f" Title: {book_dict[isbn].get_name()}")
        print(f"Author {book_dict[isbn].get_author()}")
        print(f"Genre: {book_dict[isbn].get_name()}")
        print(f"ISBN: {book_dict[isbn].get_isbn()}:")
        print(f"Publication Date: {book_dict[isbn].get_publication_date()}\n") #print book data to operator#display_book(isbn key)