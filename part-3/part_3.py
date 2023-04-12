my_books = [{
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

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called,
# and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below


def book_stuff(book_dict):
    return f"{book_dict['title']} was written by {book_dict['author']} in {book_dict['year']}. It is {book_dict['pages']} pages long and has a rating of {book_dict['rating']}."


# print(book_stuff(my_books[1]))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below


def book_title(book_dict):
    return book_dict['title']


def book_author(book_dict):
    return book_dict['author']


def book_year(book_dict):
    return book_dict['year']


def book_rating(book_dict):
    return book_dict['rating']


def book_pages(book_dict):
    return book_dict['pages']


# print(book_title(my_books[1]))
# print(book_author(my_books[1]))
# print(book_year(my_books[1]))
# print(book_rating(my_books[1]))
# print(book_pages(my_books[1]))


# Finally, create at least three new functions that might be useful as we expand our home library app.
# Perhaps thing of a way you could accept additional arguments when the function is called?
# Also, imagine you have a list filled with dictionaries like above.

# Code below
def search_by_title(term):
    books_found = []
    for book in my_books:
        if term.lower() in book['title'].lower():
            books_found.append(book)
    return books_found

def search_by_what(by_what, term):
    match by_what.lower():
        case 'title':
            return search_by_title(term)
        case 'author':
            pass  #these would contain the other search functions. THinking back on this I could probably just adjust the search_by_title function to include all of these without too much hassle, 
                  #but what i learned about match cases will be useful so i'll leave it here
        case 'year':
            pass
        case 'rating':
            pass
        case 'pages':
            pass
        case _:
            pass

def search():
    by_what = input("What attribute would you like to search for? ")
    term = input(f"Please enter the {by_what} of the book you're looking for? " )
    books = search_by_what(by_what, term)
    if not books:
        print('Nothing found under that title')
    else:
        print(books)

search()