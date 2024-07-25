def main():

    bookPath = "books/frankenstein.txt"
    text = get_book_path(bookPath)
    count = count_words(text)
    
    print(text)
    print(f"{count} words in the text")
    print(report(count_char(text)))


def get_book_path(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def count_char(text):
    char_dict = {}
    loweredText = text.lower()
    for t in text:
        if t not in char_dict:
            char_dict[t] = 0
        else:
            char_dict[t] += 1
    return char_dict

def report(dictionary):
    reportList = []
    for key, value in dictionary.items():
        if key.isalpha():
            newDict = {key: value}
            reportList.append(newDict)

    for d in reportList:
        for key, value in d.items():
            print(f"{key} was found {value} times")


main()
