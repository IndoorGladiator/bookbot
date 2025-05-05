
def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_set = set(text.lower())
    letter_map = dict.fromkeys(letter_set, 0)
    for letter in text.lower():
        letter_map[letter] += 1
    return letter_map

def report(letters):
    letter_list = list()
    for key in letters:
        letter_list.append({"char" : key, "num": letters[key]})
    letter_list.sort(reverse = True, key=lambda k: k['num'])
    return letter_list

