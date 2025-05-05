
def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_set = set(text.lower())
    letter_map = dict.fromkeys(letter_set, 0)
    for letter in text.lower():
        letter_map[letter] += 1
    return letter_map