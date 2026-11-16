def parse_data(data=None, book_number=None):
    b_dictionary = {}
    books = data["docs"]
    for book in books:
        title = book.get("title", None)
        author = book.get("author_name", None)
        first_publish_year = book.get("first_publish_year", None)
        subject = title.split()
        key = book.get("key")
        b_dictionary[key] = title, author, first_publish_year, subject
    if not books:
        return "No Search results try again."
    else:
        return b_dictionary

    if book_number is not None:
        item_in_booklist = books[book_number]
        title = item_in_booklist["title"]
        author = item_in_booklist["author"]
        first_publish_year = item_in_booklist["first_publish_year"]
        return title, author, first_publish_year
