user_input = input("\nWhich volume of scripture would you like to learn more about? ")

max_chapters = -1
max_book = ""

with open("books_and_chapters.txt") as book_file:

    for line in book_file:
        clean_line = line.strip()

        parts = clean_line.split(":")

        book = parts[0]
        chapters = int(parts[1])
        scripture = parts[2]

        if scripture.lower() == user_input.lower():
            
            if chapters > max_chapters:
                max_chapters = chapters
                max_book = book

print(f"\nThe book with the most chapters in the {user_input.title()} is {max_book}")
print(f"It has {max_chapters} chapters\n")