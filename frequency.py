""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import requests
import nltk
import pickle
import string

Frankenstein_text = requests.get('http://www.gutenberg.org/ebooks/84.txt.utf-8').text

f = open('Frankenstein_text.pickle', 'wb')
pickle.dump(Frankenstein_text, f)
f.close()

#Load data from a file (will be part of your data processing script)
input_file = open('Frankenstein_text.pickle', 'rb')
reloaded_copy_of_texts = pickle.load(input_file)

def process_file(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    file_name = file_name[200:]
    hist = dict()
    line = file_name.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1
    return hist

hist = process_file(reloaded_copy_of_texts)


def get_top_n_words(word_list):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t
t = get_top_n_words(hist)
for freq, word in t[:99]:
    print(word,freq)

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
