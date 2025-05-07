from stats import *
import sys

def get_book_text(book_filepath):
    return open(book_filepath).read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    report_book(book)
    sys.exit(0)

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