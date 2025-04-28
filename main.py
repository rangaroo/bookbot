import sys
from stats import count_words, count_character_frequency, sort_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    character_frequency = count_character_frequency(text)
    sorted_list_of_characters = sort_list(character_frequency)
    print_report(book_path, num_words,sorted_list_of_characters)



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def print_report(book_path, num_words, sorted_list_of_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")  

    for char_dict in sorted_list_of_characters:
        char = char_dict["char"]
        num = char_dict["num"]

        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

main()