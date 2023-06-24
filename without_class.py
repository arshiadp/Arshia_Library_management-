# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 20:10:44 2023

@author: PBH
"""

import datetime

members = []
books = []
borrowed_books = {}

def generate_membership_id():
    # Generate a unique membership ID based on the number of members
    return len(members) + 1

def check_national_code(national_code):
    # Check if the given national code already exists in the library members
    for member in members:
        if member['national_code'] == national_code:
            print("Error: This national code already exists.")
            return False
    return True

def add_member():
    # Get the member information from the user and add a new member to the library if their national code is unique
    first_name = input("First name: ")
    last_name = input("Last name: ")
    national_code = input("National code: ")
    birth_date = input("Birth date (YYYY/MM/DD): ")
    address = input("Address: ")

    if not check_national_code(national_code):
        return

    member = {
        'first_name': first_name,
        'last_name': last_name,
        'national_code': national_code,
        'birth_date': birth_date,
        'address': address,
        'membership_id': generate_membership_id(),
        'membership_date': datetime.datetime.now()
    }
    members.append(member)

def add_book():
    # Get the book information from the user and add a new book to the library
    title = input("Title: ")
    author = input("Author: ")
    publication_year = int(input("Publication year: "))
    field = input("Field: ")

    book = {
        'title': title,
        'author': author,
        'publication_year': publication_year,
        'field': field,
        'library_id': len(books) + 1
    }
    books.append(book)

def borrow_book():
  # Get the member ID and book ID from the user and borrow a book if it is not already borrowed and both the member and the book exist in the library
  member_id = int(input("Member ID: "))
  book_id = int(input("Book ID: "))

  if book_id in borrowed_books:
      print("Sorry, this book is already borrowed.")
      return False
  else:
      for member in members:
          if member['membership_id'] == member_id:
              for book in books:
                  if book['library_id'] == book_id:
                      borrowed_books[book_id] = member_id
                      print(f"{book['title']} has been borrowed by {member['first_name']} {member['last_name']}.")
                      return True
      print("Sorry, either the member or the book was not found.")
      return False

def return_book():
  # Get the book ID from the user and return a borrowed book if it exists in the borrowed books list
  book_id = int(input("Book ID: "))

  if book_id in borrowed_books:
      del borrowed_books[book_id]
      print("The book has been returned successfully.")
      return True
  else:
      print("Sorry, this book was not borrowed.")
      return False

def search_book_by_title():
  # Get the book title from the user and search for books by their title (case-insensitive)
  title = input("Title: ")
  result = []
  for book in books:
      if title.lower() in book['title'].lower():
          result.append(book)
  return result

def search_book_by_field():
  # Get the book field from the user and search for books by their field (case-insensitive)
  field = input("Field: ")
  result = []
  for book in books:
      if field.lower() == book['field'].lower():
          result.append(book)
  return result

def show_all_members():
  # Print the list of all members along with their membership ID and other information
  for member in members:
      print(f"First name: {member['first_name']}")
      print(f"Last name: {member['last_name']}")
      print(f"National code: {member['national_code']}")
      print(f"Birth date: {member['birth_date']}")
      print(f"Address: {member['address']}")
      print(f"Membership ID: {member['membership_id']}")
      print(f"Membership date: {member['membership_date']}")
      print()

def show_all_books():
  # Print the list of all books along with their library ID and other information
  for book in books:
      print(f"Title: {book['title']}")
      print(f"Author: {book['author']}")
      print(f"Publication year: {book['publication_year']}")
      print(f"Field: {book['field']}")
      print(f"Library ID: {book['library_id']}")
      print()

def show_available_books():
  # Print the list of all available books that are not currently borrowed along with their library ID and other information
  for book in books:
      if book['library_id'] not in borrowed_books:
          print(f"Title: {book['title']}")
          print(f"Author: {book['author']}")
          print(f"Publication year: {book['publication_year']}")
          print(f"Field: {book['field']}")
          print(f"Library ID: {book['library_id']}")
          print()

def show_borrowed_books():
  # Print the list of all borrowed books along with the name of the member who borrowed them and other information
  for book_id, member_id in borrowed_books.items():
      for member in members:
          if member['membership_id'] == member_id:
              for book in books:
                  if book['library_id'] == book_id:
                      print(f"Title: {book['title']}")
                      print(f"Author: {book['author']}")
                      print(f"Borrowed by: {member['first_name']} {member['last_name']}")
                      print()

def main():
    while True:
        # Show the main menu and get the user's choice
        command = input("\nEnter a command (type 'help' to see the list of commands): ")

        if command == 'help':
            # Show the list of available commands
            print("\nList of available commands:")
            print("add_member - Add a new member to the library")
            print("add_book - Add a new book to the library")
            print("borrow_book - Borrow a book from the library")
            print("return_book - Return a borrowed book to the library")
            print("search_book_by_title - Search for books by their title")
            print("search_book_by_field - Search for books by their field")
            print("show_all_members - Show the list of all members")
            print("show_all_books - Show the list of all books")
            print("show_available_books - Show the list of all available books that are not currently borrowed")
            print("show_borrowed_books - Show the list of all borrowed books")
            print("exit - Exit the program")
        elif command == 'add_member':
            add_member()
        elif command == 'add_book':
            add_book()
        elif command == 'borrow_book':
            borrow_book()
        elif command == 'return_book':
            return_book()
        elif command == 'search_book_by_title':
            books = search_book_by_title()
            for book in books:
                print(f"\nTitle: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Publication year: {book['publication_year']}")
                print(f"Field: {book['field']}")
                print(f"Library ID: {book['library_id']}")
        elif command == 'search_book_by_field':
            books = search_book_by_field()
            for book in books:
                print(f"\nTitle: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Publication year: {book['publication_year']}")
                print(f"Field: {book['field']}")
                print(f"Library ID: {book['library_id']}")
        elif command == 'show_all_members':
            show_all_members()
        elif command == 'show_all_books':
            show_all_books()
        elif command == 'show_available_books':
            show_available_books()
        elif command == 'show_borrowed_books':
            show_borrowed_books()
        elif command == 'exit':
            break

if __name__ == '__main__':
    main()
