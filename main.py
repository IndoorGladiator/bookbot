from stats import *

def get_book_text(book_filepath):
    return open(book_filepath).read()

def main():
    book = get_book_text("books/frankenstein.txt")
    report_book(book)

def report_book(book):
    print("----------- Word Count ----------")
    words = count_words(book)
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    letters = report(count_letters(book))
    for letter in letters:
        if letter["char"].isalpha():
            c = letter["char"]
            n = letter["num"]
            print(f"{c}: {n}")
        

main()