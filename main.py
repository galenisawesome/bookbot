def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found in the document\n")

    char_dict = count_letters(text)
    for record in char_dict:
        if record.isalpha():
            print(f"The '{record}' character was found {char_dict[record]} times")

    print("--- End report---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    char_dict = {}
    for letter in text.lower():
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1
    return char_dict

main()