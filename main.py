import sys
from parse import *

from fetch import *

from display import *


def main():
    while True:
        options = ["1", "2", "3"]
        saved_books = []
        try:
            user_choice = input(
                "Select an Option:\n 1. Search Library\n 2. Saved Books\n 3. Exit\n"
            )

        except ValueError:
            print("Invalid input. Select a number from the menu.")
            continue
        if user_choice not in options:
            raise ValueError("Select and option: 1, 2 or 3 ")
            continue

        if user_choice == "1":
            user_query = input(
                "Type in your search by author, title or subject\n"
            ).strip()
            book_dict = parse_data(fetch_data(user_query))
            display(book_dict)
            save_book = input(
                "Do you want to save a book?\n If so, what is the books enumeration?\n otherwise type exit."
            )
            if isinstance(save_book, int) and not isinstance(save_book, str):
                print(f" Saving book, {save_book}")
                saved_books.append(parse_data(save_book - 1))

        elif user_choice == "2":
            print(saved_books)
            user_exit = input("Type exit to exit.").strip().lower()
            if user_exit == "exit":
                continue
        elif user_choice == "3":
            print("Exiting program...Bye")
            sys.exit(0)
        else:
            continue


main()
