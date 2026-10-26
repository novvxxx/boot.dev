def word_count(text: str) -> int:
    return len(text.split())

def get_characters_count(text: str) -> dict[str, int]:
    characters_count = {}

    for char in text.lower():
        if char not in characters_count:
            characters_count[char] = 1
            continue
        characters_count[char] += 1

    return characters_count 

def sort_on(characters_count: tuple[str, int]) -> int:
    return characters_count[1]

def chars_dict_to_sorted_list(chars_dict: dict[str, int]):
    chars_list = []
    for char in chars_dict:
        count = chars_dict[char]
        chars_list.append((char, count))
    
    sorted_chars_list = sorted(chars_list, reverse=True, key=sort_on)
    return sorted_chars_list
