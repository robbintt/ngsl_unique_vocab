"""
Demonstrate the open() builtin method and show some 
example of what we can do with the resulting object.
"""
import pickle
import csv

def make_wordfreq_dict(contents):
    """ return a lowercase word frequency dict from a raw string containing the text
    """
    words = contents.split()

    wordfreq_dict = dict()
    for word in words:
        word = word.lower()
        times = wordfreq_dict.get(word, 0) + 1
        wordfreq_dict[word] = times

    return wordfreq_dict


def filter_excluded_words(wordfreq_dict, words_to_filter):
    """ return a filtered wordfreq_dict 

    filter out any keys that are in words_to_filter
    """
    for word in words_to_filter:
        if word in wordfreq_dict.keys():
            del wordfreq_dict[word]

    return wordfreq_dict


if __name__ == "__main__":
    """
    this is like a main() method
    """

    source_file = "mm.txt"

    """
    # list of words in the ngsl
    with open('ngsl.pickle') as f:
        ngsl = pickle.load(f)
    """

    """
    with open('fullngsl.csv') as f:
        ngslraw = f.read()
    ngsl = ngslraw.split()
    """

    ngsl = ""
    with open('ngsl-lemma.csv') as f:
        ngslreader = csv.reader(f)
        for row in ngslreader:
            ngsl += ' '.join(row)
    ngsl = ngsl.split()
    ngsl = [word.lower() for word in ngsl]

    # document to analyze for vocabulary
    mode = 'r'
    with open(source_file, mode) as f:
        contents = f.read()

    wordfreq_dict = make_wordfreq_dict(contents)
    filtered_wordfreq_dict = filter_excluded_words(wordfreq_dict, ngsl)

    wordfreq_list = sorted([(v, k) for k, v in filtered_wordfreq_dict.iteritems()])[::-1]
    print wordfreq_list[0:20]

