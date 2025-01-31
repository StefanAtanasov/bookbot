def main():
    path = './books/frankenstein.txt'
    with open(path) as f:
        file_contents = f.read()

    word_count = words_count(file_contents)
    char_counts = count_characters(file_contents)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    alpha_counts = {char: count for char, count in char_counts.items() if char.isalpha()}
    sorted_chars = sorted(alpha_counts.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")
def words_count(file_contents):
    return len(file_contents.split())

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

main()