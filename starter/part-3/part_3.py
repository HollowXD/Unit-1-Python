my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book_list = [
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
        "rating": 5,
        "pages": 223
    },
    {
        "title": "Chainsaw Man",
        "author": "Tatsuki Fujimoto",
        "year": 2019,
        "rating": 4.8,
        "pages": 192
    },
    {
        "title": "Percy Jackson The Lightning Thief",
        "author": "Rick Riordan",
        "year": 2005,
        "rating": 4.3,
        "pages": 377
    }
]
# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_parser(dictionary):
    book_content = f"The title of this book is {dictionary['title']}, written by {dictionary['author']}. The book was published in {dictionary['year']}, having {dictionary['pages']} pages. Audiences have rated it {dictionary['rating']}."
    return book_content

print(book_parser(my_book))


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def get_book_title(dictionary):
    book_title = dictionary["title"]
    return book_title

def get_book_author(dictionary):
    book_author = dictionary["author"]
    return book_author

def get_book_year(dictionary):
    book_year = dictionary["year"]
    return book_year

def get_book_rating(dictionary):
    book_rating = dictionary["rating"]
    return book_rating

def get_book_pages(dictionary):
    book_pages = dictionary["pages"]
    return book_pages

print(get_book_title(my_book))
print(get_book_author(my_book))
print(get_book_year(my_book))
print(get_book_rating(my_book))
print(get_book_pages(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def get_set_of_authors(dictionary_list):
    author_set = set()

    for dictionary in dictionary_list:
        author_set.add(dictionary["author"])

    return author_set

def get_total_pages(dictionary_list):
    total_pages = 0

    for dictionary in dictionary_list:
        total_pages += dictionary["pages"]

    return total_pages

def book_parser_from_list(dictionary_list):
    for dictionary in dictionary_list:
        print(book_parser(dictionary))

print(get_set_of_authors(my_book_list))
print(get_total_pages(my_book_list))
book_parser_from_list(my_book_list)