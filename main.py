from stats import num_of_words
from stats import num_of_characters
from stats import sort_on

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    filepath = "books/frankenstein.txt" 
    characters = num_of_characters(get_book_text(filepath))
    #print(f"{num_of_words(get_book_text(filepath))} words found in the document")
    #print(characters)
    print(sort_on(characters))

main()