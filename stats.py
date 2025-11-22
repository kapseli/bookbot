def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(items):
    return items[1]

def sort_character_count(char_count):
    # char_count.sort(reverse=True, key=lambda item: item[1])
    # return char_count
    return sorted(char_count.items(), key=lambda item: item[1], reverse=True)

def get_character_count(text):
    char_count: dict[str, int] = {}
    for char in text:
        char_lower = char.lower()
        char_count[char_lower] = char_count.get(char_lower, 0) + 1
    return char_count