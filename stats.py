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

def sort_list(character_frequency):
    def sort_on(dict):
        return dict["num"]
    
    arr = []

    for char in character_frequency:
        arr.append(
            {
                "char": char,
                "num": character_frequency[char]
            }
        )
    
    arr.sort(reverse=True, key=sort_on)

    return arr