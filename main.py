def get_book_text(book_filepath):
    return open(book_filepath).read()

def count_words(text):
    return len(text.split())

def main():
    book = get_book_text("books/frankenstein.txt")
    words = count_words(book)
    print(f"{words} words found in the document")

main()