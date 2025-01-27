def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered = get_lower_case(text)
    char_count = get_count_chars(lowered)
    char_list = get_char_list(char_count)
    get_report(book_path, num_words, char_list)
    #print(f"{num_words} words found in the document")
    #print(f"Character breakdown: {char_count}")
    #print(char_list)



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

def sort_on(dict):
    return dict["num"]

def get_char_list(char_count):
    char_list = []
    for c in char_count:
        if c.isalpha() == True:
            char_info = {"letter" : c, "num" : char_count[c]}
            char_list.append(char_info)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def get_report(book_path, words, char_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()
    for c in char_list:
        print(f"The '{c["letter"]}' letter was found {c["num"]} times")
    print("--- End report ---")
    return


main()
