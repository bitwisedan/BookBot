def num_of_words(text):
    words = text.split()
    return len(words)
def num_of_characters(text):
    letters = {'æ':0, 'â':0, 'ê':0, 'ë':0, 'ô':0, 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for char in text.lower():
        if char in letters:
            letters[char] += 1
    return letters
def sort_on(letters):
    sorted_list = []
    for letter in letters:
        sorted_list.append((letter, letters[letter]))
    sorted_list.sort(reverse=True, key=lambda x: x[1])
    return sorted_list        