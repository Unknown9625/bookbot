# main.py

import sys

from stats import get_num_words, get_character_count, sorted_list  # Imports a function that was created in another document

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def get_book_text(path):
    with open(path) as f: # The 'with' statement creates a context manager that automatically closes the file when done
        return f.read() # f.read() reads the entire file content using a single string

def main():
    text = get_book_text(path) # Calls back our get_book_text function to retrieve the content of the book
    num_words = get_num_words(text) 
    
    char_dict = get_character_count(text)
    sorted_chars = sorted_list(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        char = item["char"]
        count = item["count"]
        if char.isalpha(): # Only prints alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

main() # This line executes the main function when the script is run directly (as opposed to being imported by another script)