import string

banlist_chars = string.punctuation + string.whitespace

def main():
    #initialising
    book_path = "books/frankenstein.txt"
    text = open("books/frankenstein.txt").read()

    #create set of unique lowercase chars
    lower_case_text = text.lower()
    set_of_characters = set(lower_case_text)
    set_of_characters = list(sorted(set_of_characters))

    #init dict
    dict_of_chars = {}
    for character in set_of_characters:
        if character not in banlist_chars:
            dict_of_chars[character] = 0

    #calculations
    dict_of_chars = count_chars(lower_case_text, dict_of_chars)
    char_list = create_list(dict_of_chars)
    char_list.sort(reverse=True, key=sort_on)

    #printing report
    print("---------- BEGIN REPORT ----------")
    print("\n")
    print(f"{count_words(text)} words are in Frankenstein.")
    print("\n")
    for dictionary in char_list:
        print(f"{dictionary['char']} occurs {dictionary['num']} times")
    print("\n")
    print("---------- END REPORT ----------")

def sort_on(dictionary):
    return dictionary['num']

def create_list(dictionary):
    char_list = []
    for elements in dictionary:
        char_list.append({"char":elements, "num":dictionary[elements]})
    return char_list

def count_words(text):
    words_count = text.split()
    return len(words_count)

def count_chars(text, dictionary):
    for character in text:
        if character not in banlist_chars:
            dictionary[character] += 1
    return dictionary

main()

#def get_book_text(path):
#    with open(path) as f:
#        return f.read()
#def convert_lower(text):
#    return text.lower()
