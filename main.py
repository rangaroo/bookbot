from stats import count_words, count_character_frequency

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)

    print(f"{num_words} words found in the document")
    print(count_character_frequency(text))

main()