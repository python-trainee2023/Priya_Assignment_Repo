# author_name=input("Enter the author's name: ")
def search_by_author (author_name):
    try:
        with open("book.txt", "r") as file:
            books_written_by_author = []

            for line in file:
                book_data = line.strip.split(",")
                if len(book_data) == 2 and author_name.lower() in book_data[0].lower():
                    books_written_by_author.append(book_data[1])

                    if books_written_by_author:
                        print("Books By: ", author_name)
                        for book in books_written_by_author:
                            print(book)
                        else:
                            print("No books found", author_name)
    except FileNotFoundError:
        print("The 'book.txt' file was not found")

author_name = input("Enter the author's name: ")
search_by_author(author_name)

