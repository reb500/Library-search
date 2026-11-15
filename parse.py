def parse_data(data=None, book_number=None):
    b_dictionary = {}
    books = data["docs"]
    for book in books:
        title = book["title"]
        author = book["author_name"]
        first_publish_year = book["first_publish_year"]
        subject = title.split()
        key = book["key"]
        b_dictionary[key] = title, author, first_publish_year, subject
    return b_dictionary

    if book_number is not None:
        item_in_booklist = books[book_number]
        title = item_in_booklist["title"]
        author = item_in_booklist["author"]
        first_publish_year = item_in_booklist["first_publish_year"]
        return title, author, first_publish_year
