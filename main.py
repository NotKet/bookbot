from stats import get_num_words, get_num_of_each_char, sorted_chars
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    print("Usage: python3 main.py <path_to_book>")

    if len(sys.argv) < 2:
        sys.exit(1)

    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    num_of_chars = get_num_of_each_char(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    
    sorted = sorted_chars(num_of_chars)

    for item in sorted:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()