import re


def display(dictionary):
    print("Results: ")
    for index, (key, value) in enumerate(dictionary.items()):
        value_string = (
            str(value)
            .replace("'", "")
            .replace("]", "")
            .replace("(", "")
            .replace(")", "")
            .replace("[", "")
        )
        fields = value_string.split(",")
        print(
            f"\nIndex:{index}\nTitle: {fields[0]}\nAuthor:{fields[1]}\nYear Published:{fields[2]}"
        )


def return_book_list(dictionary):
    book_list = []
    for index, (key, value) in enumerate(dictionary.items()):
        book_list.append((key, value))
    return book_list
