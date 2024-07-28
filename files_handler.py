import book_utils as bu
import author_utils as au
import genre_utils as gu
import user_utils as uu
import datetime as dt
import os
import sys

class File_Handler():
    def __init__(self, user_file, genre_file, book_file, author_file):
        self._user_path = user_file
        self._genre_path = genre_file
        self._book_path = book_file
        self._author_path = author_file

    def save_genres(self, genres_dict):
        while True:
            try:
                with open(self._genre_path,"w") as genrefile:
                    lines = []
                    for key, genre in genres_dict.items():
                        temp = f'{key}::{genre.get_name()}::{genre.get_description()}::{genre.get_category()}\n'
                        lines.append(temp)
                    try:
                        genrefile.writelines(lines)
                        break
                    except (IOError, OSError):
                        print("\033[7mUnexpected IOError: attempt file access again?\033[0m")
                        choice = input("(yes/no): ")
                        if choice == 'yes' or 'y':
                            continue
                        else:
                            print("\033[7mUnable to save genres.\033[0m")
                            break
            except (FileNotFoundError, PermissionError, OSError):
                print("\033[7mUnable to access file for writing: attempt accessing file again?\033[0m")
                choice = input('(yes/no): ')
                if choice == 'yes' or 'y':
                    continue
                else:
                    print(f"\033[7mUnable to open {self._genre_path} to save genres.\033[0m")


    def save_books(self, books_dict):
        while True:
            try:
                with open(self._book_path,"w") as bookfile:
                    lines = []
                    for key, book in books_dict.items():
                        temp = f'{key}::{book.get_title()}::{book.get_author()}::{book.get_isbn()}::{book.get_publication_date().strftime("%Y/%m/%d")}::{book.get_status()}::{book.get_name()}\n'
                        lines.append(temp)
                    try:    
                        bookfile.writelines(lines)
                        break
                    except (IOError, OSError):
                        print("\033[7mUnexpected IOError: attempt file access again?\033[0m")
                        choice = input("(yes/no): ")
                        if choice == 'yes' or 'y':
                            continue
                        else:
                            print("\033[7mUnable to save books.\033[0m")
                            break
            except (FileNotFoundError, PermissionError, OSError):
                print("\033[7mUnable to access file for writing: attempt accessing file again?\033[0m")
                choice = input('(yes/no): ')
                if choice == 'yes' or 'y':
                    continue
                else:
                    print(f"\033[7mUnable to open {self._book_path} to save books.\033[0m")

    def save_authors(self, authors_dict):
        while True:
            try:
                with open(self._author_path,"w") as authorfile:
                    lines = []
                    for key, author in authors_dict.items():
                        temp = f'{key}::{author.get_name()}::{author.get_biography()}\n'
                        lines.append(temp)
                    try:
                        authorfile.writelines(lines)
                        break
                    except (IOError, OSError):
                        print("\033[7mUnexpected IOError: attempt file access again?\033[0m")
                        choice = input("(yes/no): ")
                        if choice == 'yes' or 'y':
                            continue
                        else:
                            print("\033[7mUnable to save authors.\033[0m")
                            break
            except (FileNotFoundError, PermissionError, OSError):
                print("\033[7mUnable to access file for writing: attempt accessing file again?\033[0m")
                choice = input('(yes/no): ')
                if choice == 'yes' or 'y':
                    continue
                else:
                    print(f"\033[7mUnable to open {self._author_path} to save authors.\033[0m")

    def save_users(self, users_dict):
        while True:
            try:
                with open(self._user_path,"w") as userfile:
                    lines = []
                    for key, user in users_dict.items():
                        temp = f'{key}::{user.get_name()}::{user.get_library_id()}'
                        if len(user.get_borrowed()) > 0:
                            for book in user.get_borrowed():
                                temp = temp + f'::{book}'
                            temp = temp + '\n'
                        else:
                            temp = temp + '::none\n'
                        lines.append(temp)
                    try:
                        userfile.writelines(lines)
                        break
                    except (IOError, OSError):
                        print("\033[7mUnexpected IOError: attempt file access again?\033[0m")
                        choice = input("(yes/no): ")
                        if choice == 'yes' or 'y':
                            continue
                        else:
                            print("\033[7mUnable to save users.\033[0m")
                            break
            except (FileNotFoundError, PermissionError, OSError):
                print("\033[7mUnable to access file for writing: attempt accessing file again?\033[0m")
                choice = input('(yes/no): ')
                if choice == 'yes' or 'y':
                    continue
                else:
                    print(f"\033[7mUnable to open {self._user_path} to save users.\033[0m")

    def load_authors(self, authors_dict):
        while True:
            try:
                if not os.path.isfile(self._author_path):
                    with open(self._author_path, 'x') as authorfile:
                        authorfile.write("")
                    break
                else:
                    with open(self._author_path,'r') as author_file:
                        lines = author_file.readlines()
                        for line in lines:
                            buffer = line.split("::")
                            if len(buffer) == 3:
                                authors_dict[buffer[0]] = au.Author(buffer[1],buffer[2][:-1])
                    break
            except (FileNotFoundError, PermissionError, IOError, OSError):
                print("\033[7mUnable to access file for writing: attempt accessing file again?\033[0m")
                choice = input('(yes/no): ')
                if choice == 'yes' or 'y':
                    continue
                else:
                    print(f"\033[7mUnable to open {self._author_path} to load authors.\033[0m")

    def load_genres(self, genres_dict):
        while True:
            try:
                if not os.path.isfile(self._genre_path):
                    with open(self._genre_path, 'x') as genrefile:
                        genrefile.write("")
                    break
                else:
                    with open(self._genre_path,'r') as genres_file:
                        lines = genres_file.readlines()
                        for line in lines:
                            buffer = line.split('::')
                            if len(buffer) == 4:
                                genres_dict[buffer[0]] = gu.Genre(buffer[1],buffer[2], buffer[3][:-1])
                        break
            except (FileNotFoundError, PermissionError, IOError, OSError):
                print("\033[7mUnable to access file for writing: attempt accessing file again?\033[0m")
                choice = input('(yes/no): ')
                if choice == 'yes' or 'y':
                    continue
                else:
                    print(f"\033[7mUnable to open {self._genre_path} to load genres.\033[0m")

    def load_books(self, books_dict, genre_dict):
        while True:
            try:
                if not os.path.isfile(self._book_path):
                    with open(self._book_path, 'x') as bookfile:
                        bookfile.write("")
                    break
                else:
                    with open(self._book_path,'r') as books_file:
                        lines = books_file.readlines()
                        for line in lines:
                            buffer = line.split('::')
                            if len(buffer) == 7:
                                buffer[6] = buffer[6][:-1]

                                t_year, t_month, t_day = buffer[4].split("/")
                                buffer[4] = dt.date(int(t_year), int(t_month), int(t_day))

                                if buffer[5] == 'Available':
                                    buffer[5] = True
                                elif buffer[5] == 'Borrowed':
                                    buffer[5] = False
        
                                description = genre_dict[buffer[6].lower()].get_description()
                                category = genre_dict[buffer[6].lower()].get_category()

                                books_dict[buffer[0]] = bu.Book(buffer[6], description, category, buffer[1], buffer[2], buffer[3], buffer[4], buffer[5])
                        break
            except (FileNotFoundError, PermissionError, IOError, OSError):
                print("\033[7mUnable to access file for writing: attempt accessing file again?\033[0m")
                choice = input('(yes/no): ')
                if choice == 'yes' or 'y':
                    continue
                else:
                    print(f"\033[7mUnable to open {self._book_path} to load books.\033[0m")

    def load_users(self, user_dict):
        while True:
            try:
                if not os.path.isfile(self._user_path):
                    with open(self._user_path, 'x') as userfile:
                        userfile.write("")
                    break
                else:
                    with open(self._user_path,"r") as userfile:
                        lines = userfile.readlines()
                        for line in lines:
                            buffer = line.split('::')
                            buffer[len(buffer) - 1] = buffer[len(buffer) - 1][:-1]
                            if len(buffer) == 4:
                                user_dict[buffer[0]] = uu.User(buffer[1],buffer[2])
                            elif len(buffer) > 4:
                                borrowed = []
                                for x in range(3,len(buffer)):
                                    borrowed.append(buffer[x])
                                user_dict[buffer[0]] = uu.User(buffer[1],buffer[2])
                                user_dict[buffer[0]].set_borrowed(borrowed)
                            else:
                                continue
                        break
            except (FileNotFoundError, PermissionError, IOError, OSError):
                print("\033[7mUnable to access file for writing: attempt accessing file again?\033[0m")
                choice = input('(yes/no): ')
                if choice == 'yes' or 'y':
                    continue
                else:
                    print(f"\033[7mUnable to open {self._user_path} to load users.\033[0m")
        

    def update_users(self, user_dict, key):
        while True:
            try:
                with open(self._user_path,'a') as user_file:
                    temp = f'{key}::{user_dict[key].get_name()}::{user_dict[key].get_library_id()}\n'
                    try:
                        user_file.write(temp)
                        break
                    except (IOError, OSError):
                        print("\033[7mUnexpected IOError: attempt file access again?\033[0m")
                        choice = input("(yes/no): ")
                        if choice == 'yes' or 'y':
                            continue
                        else:
                            print("\033[7mUnable to update users.\033[0m")
                            break
            except (FileNotFoundError, PermissionError, OSError):
                print("\033[7mUnable to access file for writing: attempt accessing file again?\033[0m")
                choice = input('(yes/no): ')
                if choice == 'yes' or 'y':
                    continue
                else:
                    print(f"\033[7mUnable to open {self._user_path} to update users.\033[0m")

    def update_authors(self, authors_dict, key):
        while True:
            try:
                with open(self._author_path, 'a') as author_file:
                    temp = f'{key}::{authors_dict[key].get_name()}::{authors_dict[key].get_biography()}\n'
                    try:
                        author_file.write(temp)
                        break
                    except (IOError, OSError):
                        print("\033[7mUnexpected IOError: attempt file access again?\033[0m")
                        choice = input("(yes/no): ")
                        if choice == 'yes' or 'y':
                            continue
                        else:
                            print("\033[7mUnable to update authors.\033[0m")
                            break
            except (FileNotFoundError, PermissionError, OSError):
                print("\033[7mUnable to access file for writing: attempt accessing file again?\033[0m")
                choice = input('(yes/no): ')
                if choice == 'yes' or 'y':
                    continue
                else:
                    print(f"\033[7mUnable to open {self._author_path} to update authors.\033[0m")

    def update_genres(self, genres_dict, key):
        while True:
            try:
                with open(self._genre_path, 'a') as genre_file:
                    temp = f'{key}::{genres_dict[key].get_name()}::{genres_dict[key].get_description()}::{genres_dict[key].get_category()}\n'
                    try:
                        genre_file.write(temp)
                        break
                    except (IOError, OSError):
                        print("\033[7mUnexpected IOError: attempt file access again?\033[0m")
                        choice = input("(yes/no): ")
                        if choice == 'yes' or 'y':
                            continue
                        else:
                            print("\033[7mUnable to update genres.\033[0m")
                            break
            except (FileNotFoundError, PermissionError, OSError):
                print("\033[7mUnable to access file for writing: attempt accessing file again?\033[0m")
                choice = input('(yes/no): ')
                if choice == 'yes' or 'y':
                    continue
                else:
                    print(f"\033[7mUnable to open {self._genre_path} to update genres.\033[0m")

    def update_books(self, books_dict, key):
        while True:
            try:
                with open(self._book_path, 'a') as book_file:
                    temp = f'{key}::{books_dict[key].get_title()}::{books_dict[key].get_author()}::{books_dict[key].get_isbn()}::{books_dict[key].get_publication_date().strftime("%Y/%m/%d")}::{books_dict[key].get_status()}::{books_dict[key].get_name()}\n'
                    try:
                        book_file.write(temp)
                        break
                    except (IOError, OSError):
                        print("\033[7mUnexpected IOError: attempt file access again?\033[0m")
                        choice = input("(yes/no): ")
                        if choice == 'yes' or 'y':
                            continue
                        else:
                            print("\033[7mUnable to update books.\033[0m")
                            break
            except (FileNotFoundError, PermissionError, OSError):
                print("\033[7mUnable to access file for writing: attempt accessing file again?\033[0m")
                choice = input('(yes/no): ')
                if choice == 'yes' or 'y':
                    continue
                else:
                    print(f"\033[7mUnable to open {self._book_path} to update books.\033[0m")

    def reload_all(self, author_dict, book_dict, genre_dict, user_dict):
        author_dict.clear()
        book_dict.clear()
        genre_dict.clear()
        user_dict.clear()

        self.load_authors(author_dict)
        self.load_genres(genre_dict)
        self.load_books(book_dict,genre_dict)
        self.load_users(user_dict)

    def save_all(self, author_dict, book_dict, genre_dict, user_dict):
        self.save_authors(author_dict)
        self.save_books(book_dict)
        self.save_genres(genre_dict)
        self.save_users(user_dict)

    def load_all(self, author_dict, book_dict, genre_dict, user_dict):
        if os.path.isfile(self._author_path) and os.path.isfile(self._book_path) and os.path.isfile(self._genre_path) and os.path.isfile(self._user_path):
            self.load_authors(author_dict)
            self.load_genres(genre_dict)
            self.load_books(book_dict, genre_dict)
            self.load_users(user_dict)
        else:
            if not os.path.isfile(self._author_path) and not os.path.isfile(self._book_path) and not os.path.isfile(self._genre_path) and not os.path.isfile(self._user_path):
                self.load_authors(author_dict)
                self.load_genres(genre_dict)
                self.load_books(book_dict, genre_dict)
                self.load_users(user_dict)
            else:
                print("\033[7mUnable to locate all data files: Cancelling loading of save files. Please close program and restore files if you want to use Library Mangagement System with previously input information\033[0m")
                while True: #loop in case of valid input
                    choice = input("Options for continuing:\n1. Delete all save files and start from empty state\n2.Quit Library Management System and investigate/restore save files\n Please enter your choice: ")

                    if choice == '1':
                        if os.path.exists(self._author_path):
                            os.remove(self._author_path)
                        if os.path.exists(self._book_path):
                            os.remove(self._book_path)
                        if os.path.exists(self._genre_path):
                            os.remove(self._genre_path)
                        if os.path.exists(self._user_path):
                            os.remove(self._user_path)
                        
                        self.load_authors(author_dict)
                        self.load_genres(genre_dict)
                        self.load_books(book_dict, genre_dict)
                        self.load_users(user_dict)
                        break
                    elif choice == '2':
                        sys.exit("Library Management System now closing for Investigation/Restoration of save files")
                    else:
                        print("Invalid choice: Please try again")