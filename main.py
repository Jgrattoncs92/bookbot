import sys
from stats import get_num_words, count_characters, sort_characters

def main():
    # Check if a file path argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Read the file path from the command line argument
    book_path = sys.argv[1]

    try:
        with open(book_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found.")
        sys.exit(1)

    # Process the text
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)

    # Print character frequencies
    for item in sorted_chars:
        print(f"{item['character']}: {item['count']}")

if __name__ == "__main__":
    main()

