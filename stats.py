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