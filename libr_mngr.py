from colorama import Fore,Back,Style
import os
import json


# File where books will be stored
BOOKS = "library.json"

# Check if the books file exists, if not create an empty list
if not os.path.exists(BOOKS):
    with open(BOOKS, "w") as f:
        json.dump([], f)
#total=len(BOOKS)

def load_books():
    """Load books from the file"""
    with open(BOOKS, "r") as f:
        return json.load(f)
#fun=json.load(f)
#total=len(fun)

def save_books(books):
    """Save the books list to the file"""
    with open(BOOKS, "w") as f:
        json.dump(books, f, indent=4)
        

def add_book(title, author,year,genre,status):
    """Add a new book to the list"""
    books = load_books()
    book = {"title": title, "author": author,"Publication year":year,"Genre":genre,"Read":status}
    books.append(book)
    save_books(books)
    
    print(f" Book '{title}' by {author} published in {year } of genre {genre }added successfully. Reading Status: {status}  ")
    if status=="True":
        print(Fore.GREEN+"The book has been read")
        
    else:
        print(Fore.RED+"The book not been read yet")

def remove_book(title):
    """Remove a book by title"""
    books = load_books()
    books = [book for book in books if book["title"].lower() != title.lower()]
    save_books(books)
    print(f"Book '{title}' removed successfully.")

def list_books():
    """List all books"""
    books = load_books()
   
    if not books:
        print("No books available.")
    else:
        print("==== Books List ====")
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book['title']} by {book['author']}")
        print("====================")

#count the books
with open('library.json', 'r') as file:
    data = json.load(file)
total=len(data)

    

def search_books(query):
    """Search books by title or author"""
    books = load_books()
    results = [book for book in books if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]
    if results:
        print(f"Found {len(results)} result(s):")
        for book in results:
            print(Style.BRIGHT+f"- {book['title']} by {book['author']}")
    else:
        print("No books found matching your query.")

#percentage
with open('library.json', 'r') as file1:
    data1 = json.load(file1)
perc=(data1) and  (data)
print(Fore.LIGHTGREEN_EX+"Representation of data uptill now in dictionary form \n",perc)



def display_menu():
    """Display the menu options"""
    print(Fore.YELLOW+Back.WHITE+"==== ****MY PERSONAL LIBRARY**** ====")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search for a Book")
    print("4. Display all Books")
    print("5. Total books in Library")
    print("6. Complete details of available books in library in dictionary form")
    print("7. Exit")
    print("======================")

def main():
    """Main function to run the menu and handle user input"""
    while True:
        display_menu()
        
        choice = input("Please select an option (1-7): ")

        if choice == '1':
            title = str(input("Enter the title of the book: "))
            author = str(input("Enter the author of the book: "))
            year=int(input("Enter the publication year :  "))
            genre=str(input("Enter the genre:  "))
            status=input("Find reading status(Type True for yes / Type False for pending) : ")
            add_book(title, author,year,genre,status)
        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            remove_book(title)
        
        elif choice == '3':
            query = input("Enter the title or author to search for: ")
            search_books(query)
        elif choice == '4':
            list_books()
        elif choice == '5' :
            print(Fore.CYAN + "Total books in library are given as under: ")
            print(total)
        elif choice == '6' :
            print("Added books in library" , perc)
        elif choice == '7':
            print("closing Library...")
            break
        else:
            print("Try again!!")

if __name__ == "__main__":
    main()
