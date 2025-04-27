def count_words(text):
    words_arr = text.split()

    return len(words_arr)

def count_character_frequency(text):
    character_frequency = {}

    for char in text.lower():
        if char in character_frequency:
            character_frequency[char] += 1
        else:
            character_frequency[char] = 1
    
    return character_frequency

def sorted_list_of_dictionary(character_frequency):
    arr = []

    for char in character_frequency:
        arr.append(
            {
                "char": char,
                "num": character_frequency[char]
            }
        )
    
    return arr