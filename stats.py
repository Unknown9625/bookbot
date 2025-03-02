# stats.py

def get_num_words(text):
    return len(text.split()) # Counts the number of the words in the document by first splitting the text by each space and then using the len() function to count this amount

def get_character_count(text): # Creates a dictionary that tracks frequency of each lowercase character in text, using get() with default 0 to handle first occurrences
    character_count = {}

    for char in text.lower():
        character_count[char] = character_count.get(char, 0) + 1
    return character_count

def sorted_list(char_dict): # Converts a character count dictionary into a sorted list of dictionaries (each with 'char' and 'count' keys), ordered from highest to lowest count
    result = []

    for char, count in char_dict.items():
        char_count_dict = {"char": char, "count": count}
        result.append(char_count_dict)
    
    def sort_on(dict_item):
        return dict_item["count"]
    
    result.sort(reverse=True, key=sort_on)

    return result