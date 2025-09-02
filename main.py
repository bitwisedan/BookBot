from stats import num_of_words
from stats import num_of_characters
from stats import sort_on

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    filepath = "books/frankenstein.txt" 
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