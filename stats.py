def count_words(text):
    words_arr = text.split()

    return len(words_arr)

def count_character_frequency(text):
    frequency_dictionary = {}

    for char in text.lower():
        if char in frequency_dictionary:
            frequency_dictionary[char] += 1
        else:
            frequency_dictionary[char] = 1
    
    return frequency_dictionary