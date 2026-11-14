def parse_data():
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
