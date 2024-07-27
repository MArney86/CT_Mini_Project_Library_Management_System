import book_utils as bu
import author_utils as au
import genre_utils as gu
import user_utils as uu
import sys
import datetime as dt

library_books = {}
library_users = {}
library_authors = {}
library_genres = {}

def main():
    #preload for testing
    library_genres['fantasy'] = gu.Genre("Fantasy", "Fantasy Worlds", "Fiction")
    library_genres['political fiction'] = gu.Genre("Political Fiction", "Stories about worlds with different political structures", "Fiction")
    library_genres['biography'] = gu.Genre("Biography", "The stories of the lives of real people", "Non-fiction")
    library_genres['almanac'] = gu.Genre("Almanac", "A collection of facts and information", "Reference")
    library_genres['dictionary'] = gu.Genre("Dictionary", "A compendium of words and their definitions", "Reference")
    library_books['9780544003415'] = bu.Book("Fantasy", "Fantasy Worlds", "Fiction","Lord of the Rings", "J.R.R. Tolkien", "9780544003415", dt.date(2012, 8, 14))
    library_books['9781443434973'] = bu.Book("Political Fiction", "Stories about worlds with different political structures", "Fiction", "1984", "George Orwell", "9781443434973", dt.date(2014, 3, 25))
    library_books['9780345325815'] = bu.Book("Fantasy", "Fantasy Worlds", "Fiction", "The Silmarillion", "J.R.R. Tolkien", "9780345325815", dt.date(2002, 1, 1))
    library_books['9781510777606'] = bu.Book("Almanac", "A collection of facts and information", "Reference", "The World Almanac and Book of Facts 2024", "Sarah Janssen", "9781510777606", dt.date(2023, 11, 28))
    library_books['9780199571123'] = bu.Book("Dictionary", "A compendium of words and their definitions", "Reference", "Oxford Dictionary of English, 3rd Edition", "Oxford Languages", "9780199571123", dt.date(2010, 10, 19))
    library_books['9781451648539'] = bu.Book("Biography", "The stories of the lives of real people", "Non-fiction", "Steve Jobs", "Walter Isaacson", "9781451648539", dt.date(2011, 10, 24))
    library_authors["j.r.r. tolkien"] = au.Author("J.R.R. Tolkien", "J.R.R. Tolkien was born on 3rd January 1892. After serving in the First World War, he became best known for The Hobbit and The Lord of the Rings, selling 150 million copies in more than 40 languages worldwide. Awarded the CBE and an honorary Doctorate of Letters from Oxford University, he died in 1973 at the age of 81.")
    library_authors["george orwell"] = au.Author("George Orwell", "George Orwell (born June 25, 1903, Motihari, Bengal, India—died January 21, 1950, London, England) was an English novelist, essayist, and critic famous for his novels Animal Farm (1945) and Nineteen Eighty-four (1949). The latter of these is a profound anti-utopian novel that examines the dangers of totalitarian rule.")
    library_users['951473671328'] = uu.User("John Smith", "951473671328")
    library_users['321468132177'] = uu.User("Jane Doe", "321468132177")
    library_users['976131468354'] = uu.User("John Smith", "976131468354")


    while True: #loop in case of invalid input
        print("\nWelcome to the Library Management System!\n") #display main menu
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

    
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
    while True: #loop in case of invalid input
        print("\nBook Operations:") #display book operations menu
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Return to previous menu")

        choice = input("What would you like to do?: ") #get user choice
        if choice == '1': #chose to add book
            bu.add_book(library_books, library_genres) #add book
        elif choice == '2': #chose to borrow a book
            bu.borrow_book(library_users, library_books) #borrow book
        elif choice == '3': #chose to return a book
            bu.return_book(library_users, library_books) #return book
        elif choice == '4': #chose to search for a book
            bu.search_books(library_books) #search books
        elif choice == '5': #chose to display all books
            bu.display_all_books(library_books) #display all books
        elif choice == '6': #chose to leave
            break #end loop and function
        else: #invalid response
            print("Invalid choice. Please try again.") #notify user of invalid response


def user_menu():
    while True: #loop in case of invalid input
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Return to previous menu")

        choice = input("What would you like to do?: ").strip() #get user choice
        if choice == '1': #chose to add user
            uu.add_user(library_users) #add user
        elif choice == '2': #view a user's details
            uu.view_user_details(library_users, library_books) #view user details
        elif choice == '3': #display all users
            uu.display_all_users(library_users, library_books) #display all users
        elif choice == '4': #chose to leave
            break #end loop and function
        else: #invalid response
            print("Invalid choice. Please try again.") #notify user of invalid response

def author_menu():
    while True: #loop in case of invalid input
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Return to previous menu")

        choice = input("What would you like to do?: ").strip() #get user choice
        if choice == '1': #chose to add user
            au.add_author(library_authors) #add user
        elif choice == '2': #view a user's details
            au.view_author_details(library_authors) #view user details
        elif choice == '3': #display all users
            au.display_all_authors(library_authors) #display all users
        elif choice == '4': #chose to leave
            break #end loop and function
        else: #invalid response
            print("Invalid choice. Please try again.") #notify user of invalid response

def genre_menu():
    while True: #loop in case of invalid input
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Return to previous menu")

        choice = input("What would you like to do?: ").strip() #get user choice
        if choice == '1': #chose to add genre
            gu.add_genre(library_genres) #add genre
        elif choice == '2': #view a genre's details
            gu.view_genre_details(library_genres) #view genre details
        elif choice == '3': #display all genres
            gu.display_all_genres(library_genres) #display all genres
        elif choice == '4': #chose to leave
            break #end loop and function
        else: #invalid response
            print("Invalid choice. Please try again.") #notify user of invalid response

if __name__ == "__main__":
    main()