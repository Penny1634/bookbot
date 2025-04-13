from stats import count_book_word, count_time_char, sort_time_char
import sys
def get_book_text(book):
    try:
        with open(book) as f:
            result = f.read()
    except Exception as e:
        print(e)
    return result

def main():
    if len(sys.argv)< 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text=get_book_text(book)
    count = count_book_word(text)
    char_count = count_time_char(text)
    sorted_char_count = sort_time_char(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char in sorted_char_count:
        print(f"{char["letter"]}: {char["count"]}")
    print("============= END ===============")
main()