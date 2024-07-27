import book_utils as bu
import author_utils as au
import genre_utils as gu
import user_utils as uu
import sys

library_books = {}
library_users = {}
library_authors = {}
library_genres = {}

def main():
    print("Welcome to the Library Management System!\n") #display main menu
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Genre Operations")
    print("5. Quit")

    while True: #loop in case of invalid input
        choice = input("What would you like to do? ").strip() #get user's choice
        if choice == '1': #chose book operations
            book_menu() #load the book menu
        elif choice == '2': #chose user operations
            user_menu() #load the user menu
        elif choice == '3': #chose author operations
            author_menu() #load the author menu
        elif choice == '4': #chose genre operations
            genre_menu() #load the genre menu
        elif choice == '5': #chose to quit
            sys.exit("Thank you for using the Library Management System") #exit program to system/terminal prompt
        else: #invalid response
            print("Invalid choice. Please try again.") #notify user of invalid response
            
def book_menu():
    print("Book Operations:") #display book operations menu
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    print("6. Return to previous menu")

    while True: #loop in case of invalid input
        choice = input("What would you like to do?: ").strip() #get user choice
        if choice == '1': #chose to add book
            bu.add_book(library_books, library_genres) #add book
        if choice == '2': #chose to borrow a book
            bu.borrow_book(library_users, library_books) #borrow book
        if choice == '3': #chose to return a book
            bu.return_book(library_users, library_books) #return book
        if choice == '4': #chose to search for a book
            bu.search_books(library_books) #search books
        if choice == '5': #chose to display all books
            bu.display_all_books(library_books) #display all books
        if choice == '6': #chose to leave
            break #end loop and function
        else: #invalid response
            print("Invalid choice. Please try again.") #notify user of invalid response


def user_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    print("4. Return to previous menu")

    while True: #loop in case of invalid input
        choice = input("What would you like to do?: ").strip() #get user choice
        if choice == '1': #chose to add user
            uu.add_user(library_users) #add user
        if choice == '2': #view a user's details
            uu.view_user_details(library_users, library_books) #view user details
        if choice == '3': #display all users
            uu.display_all_users(library_users, library_books) #display all users
        if choice == '4': #chose to leave
            break #end loop and function
        else: #invalid response
            print("Invalid choice. Please try again.") #notify user of invalid response

def author_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    print("4. Return to previous menu")

    while True: #loop in case of invalid input
        choice = input("What would you like to do?: ").strip() #get user choice
        if choice == '1': #chose to add user
            au.add_author(library_authors) #add user
        if choice == '2': #view a user's details
            au.view_author_details(library_authors) #view user details
        if choice == '3': #display all users
            au.display_all_authors(library_authors) #display all users
        if choice == '4': #chose to leave
            break #end loop and function
        else: #invalid response
            print("Invalid choice. Please try again.") #notify user of invalid response

def genre_menu():
    print("Genre Operations:")
    print("1. Add a new genre")
    print("2. View genre details")
    print("3. Display all genres")
    print("4. Return to previous menu")

    while True: #loop in case of invalid input
        choice = input("What would you like to do?: ").strip() #get user choice
        if choice == '1': #chose to add genre
            gu.add_genre(library_genres) #add genre
        if choice == '2': #view a genre's details
            gu.view_genre_details(library_genres) #view genre details
        if choice == '3': #display all genres
            gu.display_all_genres(library_genres) #display all genres
        if choice == '4': #chose to leave
            break #end loop and function
        else: #invalid response
            print("Invalid choice. Please try again.") #notify user of invalid response

if __name__ == "__main__":
    main()