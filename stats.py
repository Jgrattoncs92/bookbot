def get_num_words(text):
    return len(text.split())

def count_characters(text):
    char_counts = {}
    text = text.lower()  # Convert text to lowercase

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_characters(char_counts):
    sorted_chars = sorted(
        [{"character": char, "count": count} for char, count in char_counts.items() if char.isalpha()],
        key=lambda x: x["count"],
        reverse=True
    )
    return sorted_chars
