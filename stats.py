def get_book_text(filepath):
        
        with open(filepath) as f:
            
            file_contents = f.read()
        
        return file_contents

def get_word_count(booktext):

    return len(booktext.split())

def get_letter_count(booktext):

    letter_dict = {}

    for letter in booktext.lower():

        if letter not in letter_dict:
            
            letter_dict[letter] = 1

        else:

            letter_dict[letter] += 1
    
    return letter_dict

def sort_on(items):

    return items["num"]

def modify_dict(letter_dict):

    char_list = []

    for letter in letter_dict:
        new_dict = {}

        if letter.isalpha():
            count = letter_dict[letter]
            new_dict["char"] = letter
            new_dict["num"] = count
            char_list.append(new_dict)

    return char_list

def print_sorted_dict(modified_dict):
    
    for letter_dict in modified_dict:
        char = letter_dict["char"]
        num = letter_dict["num"]
        print(f"{char}: {num}")
    return