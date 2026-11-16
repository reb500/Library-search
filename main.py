import sys
from parse import *

from fetch import *

from display import *


def main():
    while True:
        options = ["1", "2", "3"]

        try:
            user_choice = input(
                "Select an Option:\n1. Search Library\n2. Saved Books\n3. Exit\n"
            )

        except ValueError:
            print("Invalid input. Select a number from the menu.")
            break

        if user_choice not in options:
            raise ValueError("Select and option: 1, 2 or 3 ")
            continue

        if user_choice == "1":
            user_query = input(
                "Type in your search by author, title or subject:\n"
            ).strip()
            book_dict = parse_data(fetch_data(user_query))
            if book_dict == "No Search results try again.":
                break
            else:
                display(book_dict)
            save_book = input(
                "\nDo you want to save a book?\nIf so, what is the books enumeration?\notherwise type exit.:  "
            )
            try:
                save_book = int(save_book)

            except ValueError:
                print("Can't convert text to an integer.")
                continue
            print(f" Saving book, # {save_book}")
            book_list = return_book_list(book_dict)
            saved_books.append(book_list[save_book])
            print(saved_books)

        elif user_choice == "2":
            print(saved_books)
            user_exit = input("Type exit to return to the menu.").strip().lower()
            if user_exit == "exit":
                continue
        elif user_choice == "3":
            print("Exiting program...Bye")
            sys.exit(0)
        else:
            continue


if __name__ == "__main__":
    print("\nRunning Library-search program")
    saved_books = []
    main()
