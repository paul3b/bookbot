def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_dict = get_chars_dict(text)
    print(f"--- Begin report of {book_path} ---\n")
    print(f"{word_count} words found in document\n")
    for character, count in char_dict.items():
        print(f"The '{character}' was found {count} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars
            


main()