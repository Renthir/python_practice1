### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def write_book(book):    
    with open('library.txt', 'a') as database:
        database.write(f'{book["title"]}, {book["author"]}, {book["year"]}, {book["rating"]}, {book["pages"]}\n')

### Step 2 - Read data from a .txt
def get_library():
    with open('library.txt', 'r') as database:
        file = database.readlines()[1:]

        library = []
        for line in file:
            title, author, year, rating, pages = line.split(', ')

            book_dict = {
                'title': title,
                'author': author,
                'year': year,
                'rating': rating,
                'pages': pages.replace('\n','')
            }
            library.append(book_dict)

    return library

## Now take your previously create function which prints info about all the books in your library, 
# but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def create_new_book():
    print("Please input the details of the new book - ")
    title = input("Title: ")
    author = input("Author: ")
    try:
        year = int(input("Year published: "))
    except:
        year = int(input("Please type a number for the year: "))

    try:
        rating = float(input("Rating out of 5: "))

    except:
        rating = float(input("Please type a number for the rating: "))

    try:
        pages = int(input("Pages: "))
    except:
        pages = int(input("Please type a number for pages: "))

    book_dict = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    write_book(book_dict)

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def search_by_string(by_what, term):
    library = get_library()
    books_found = []
    for book in library:
        if term.lower() in book[by_what].lower():
            books_found.append(book)
    return books_found

def search():
    by_what = input("Would you like to search by title or by author: ")
    term = input(f"Please enter the {by_what} of the book you're looking for: " )
    books = search_by_string(by_what, term)
    if not books:
        print('No Results')
    else:
        print(books)

running = True

def main_menu():
    print("\nWelcome to the home library!")
    command = input("Please enter a command to proceed: ").lower()
    if command == "help":
        print('Commands include: add, search, books, exit, help')
    elif command == 'add':
        create_new_book()
    elif command == 'search':
        search()
    elif command == 'exit':
        global running 
        running= False
    elif command == 'books':
        print(get_library())
    else:
        print("Command not recognized. For possible commands, type 'help'")


if __name__ == '__main__':
    while running:
        main_menu()