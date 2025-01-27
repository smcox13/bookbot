def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered = get_lower_case(text)
    char_count = get_count_chars(lowered)
    print(f"{num_words} words found in the document")
    print(f"Character breakdown: {char_count}")



def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_lower_case(text):
    lowered = text.lower()
    return lowered

def get_count_chars(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


main()
