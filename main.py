from stats import get_book_text, get_word_count, get_letter_count

def main():

    filepath = "books/frankenstein.txt"
    booktext = get_book_text(filepath)
    print(f"Found {get_word_count(booktext)} total words")
    print(get_letter_count(booktext))
main()