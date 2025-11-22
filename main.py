from stats import get_num_words, get_character_count, sort_character_count
import sys

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def print_book_stats(path):
    text = get_book_text(path)
    count = get_num_words (text)
    char_count = get_character_count(text)
    sorted_chars = sort_character_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char, num in sorted_chars:
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

def main():
    # path = "books/frankenstein.txt"
    
    # print(text)
    # print(sys.argv)
    # print(sys.argv)
    # Prints ['main.py']
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print_book_stats(path)
    
    

if __name__ == "__main__":
    main()