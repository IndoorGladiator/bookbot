from stats import *

def get_book_text(book_filepath):
    return open(book_filepath).read()

def main():
    book = get_book_text("books/frankenstein.txt")
    words = count_words(book)
    print(f"{words} words found in the document")
    letters = count_letters(book)
    print(letters)

main()