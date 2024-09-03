print()

with open("books.txt") as book_file:

    for book in book_file:
        clean_line = book.strip()
        print(clean_line)

print()