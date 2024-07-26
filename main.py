def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_counts = count_char(text)
    sorted_report = create_sorted_report(char_counts)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("Characters found in the document:")

    print_report(sorted_report)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    char_dict = {}
    lowered_text = text.lower()
    for t in lowered_text:
        if t.isalpha():  # We only care about alphabet characters
            if t not in char_dict:
                char_dict[t] = 1  # Initialize count for new character
            else:
                char_dict[t] += 1  # Increment count for existing character
    return char_dict

def create_sorted_report(char_dict):
    report_list = [{"char": key, "count": value} for key, value in char_dict.items()]
    report_list.sort(key=lambda x: x["count"], reverse=True)
    return report_list

def print_report(report_list):
    for item in report_list:
        print(f"The '{item['char']}' character was found {item['count']} times.")

main()
