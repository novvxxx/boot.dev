import sys
from stats import *

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()

def print_report(path: str, words_count: int, chars_count: list[tuple(str, int)]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for char in chars_count:
        if not char[0].isalpha():
            continue
        print(f"{char[0]}: {char[1]}")
    print("============= END ===============")

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    content = get_book_text(path)
    num_words = word_count(content)
    chars_dict = get_characters_count(content)
    chars_list = chars_dict_to_sorted_list(chars_dict)
    print_report(path, num_words, chars_list)

main()