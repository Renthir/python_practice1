# Step 1 - Input function

user_library = [{
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
},
    {
        "title": "Metro 2033",
        "author": "Dmitry Glukhovsky",
        "year": 2002,
        "rating": 4.4,
        "pages": 458
}
]

# Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def create_new_book():
#     print("Please input the details of the new book - ")
#     title = input("Title: ")
#     author = input("Author: ")
#     year = input("Year published: ")
#     rating = input("Rating out of 5: ")
#     pages = input("Pages: ")

#     book_dict = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dict

# print(create_new_book())

# Step 2 - Type conversion

# Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

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

    user_library.append(book_dict)


# print(create_new_book())
# Step 3 - Error handling

# Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
# done above


# Step 4 - if/elif/else

# Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
def search_by_string(by_what, term):
    books_found = []
    for book in user_library:
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
    print("Welcome to the home library!")
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
        print(user_library)
    else:
        print("Command not recognized. For possible commands, type 'help'")



# Step 5 - while loops

# Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

while running:
    main_menu()


