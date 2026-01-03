import sys
from stats import get_book_text, get_word_count, get_letter_count, sort_on, modify_dict, print_sorted_dict

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")

    filepath = sys.argv[1]

    print(f"Analyzing book found at {filepath}")

    print("--------- Character Count -------")
    booktext = get_book_text(filepath)
    print(f"Found {get_word_count(booktext)} total words")
    print("--------- Character Count -------")
    letter_dict = get_letter_count(booktext)

    modified_dict = modify_dict(letter_dict)
    
    modified_dict.sort(reverse=True, key=sort_on)

    print_sorted_dict(modified_dict)

    print("============= END ===============")

main()