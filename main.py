from stats import num_of_words
from stats import num_of_characters
from stats import sort_on
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if sys.argv.__len__() < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    characters = num_of_characters(get_book_text(filepath))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words(get_book_text(filepath))} total words")
    print("--------- Character Count -------")
    for letter, count in sort_on(characters):
        if count > 0:
            print(f"{letter}: {count}")
    print("============= END ===============")

main()