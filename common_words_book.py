import requests
import string

def save_book(url="https://www.gutenberg.org/cache/epub/11/pg11.txt"):
    """
    Download a book fromo a URL and save it to book.txt
    :param url: the url of the book
    :return: None
    """
    r = requests.get(url)
    with open("book.txt", "w") as f:
        f.write(r.text)
    # if using the with construct, there is no need to close!!
    # this is the same thing:
    # f = open("book.txt", "w")
    # f.write(r.text)
    # f.close()


# save_book()
def count_words(filename="book.txt"):
    """
    count the words in the book
    :param filename:
    :return: a dictionary
    """
    words_dict = {}
    with open("book.txt", "r") as f:
        for line in f:
            # remove punctuation from the line
            for p in string.punctuation:
                line = line.replace(p, "")
            line_words = line.split()
            for word in line_words:
                words_dict[word] = words_dict.get(word, 0) + 1
    return words_dict


words_dict = count_words()
# print(words_dict)
print(len(words_dict))
freq_list = list(words_dict.values())
# print(freq_list)
freq_list.sort(reverse=True)
print(f"10 most common frequencies are: {freq_list[:10]}")
for freq in freq_list[:10]:
    for key in words_dict:
        if words_dict[key] == freq:
            print(f"word: '{key}' shows up {freq} times")
            # break
