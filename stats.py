def num_of_words(text):
    words = text.split()
    return len(words)
def num_of_characters(text: str) -> dict:
    letters = {}
    for char in text.lower():
        if char.isalpha():
            letters[char] = letters.get(char, 0) + 1
    return letters
def sort_on(letters):
    sorted_list = []
    for letter in letters:
        sorted_list.append((letter, letters[letter]))
    sorted_list.sort(reverse=True, key=lambda x: x[1])
    return sorted_list        