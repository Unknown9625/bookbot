# main.py

from stats import get_num_words # Imports a function that was created in another document
from stats import get_character_count 
from stats import sorted_list

def get_book_text(path):
    with open(path) as f: # The 'with' statement creates a context manager that automatically closes the file when done
        return f.read() # f.read() reads the entire file content using a single string

def main():
    path = "books/frankenstein.txt" # This defines the relative path and tells Python to find a file starting from the current directory where the script is run, rather than using an absolute location in your file system
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