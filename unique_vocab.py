"""
Take a text document and filter the ngsl words out, then sort by word frequency.

Used to identify an author's unique vocabulary

Tends to also get tons of proper nouns.
"""
import pprint
import csv

PUNCTUATION = '\'";:,.?!'

MANUAL_WORD_FILTER = [  "i'll",
        "thou" ]


def make_wordfreq_dict(contents):
    """ return a lowercase word frequency dict from a raw string containing the text
    """
    words = contents.split()

    wordfreq_dict = dict()
    for word in words:
        word = word.lower().strip()
        word = word.strip(PUNCTUATION)
        times = wordfreq_dict.get(word, 0) + 1
        wordfreq_dict[word] = times

    return wordfreq_dict


def filter_excluded_words(wordfreq_dict, words_to_filter, MANUAL_FILTER=MANUAL_WORD_FILTER):
    """ return a filtered wordfreq_dict 

    filter out any keys that are in words_to_filter
    """
    words_to_filter.extend(MANUAL_FILTER)
    for word in words_to_filter:
        if word in wordfreq_dict.keys():
            del wordfreq_dict[word]

    return wordfreq_dict


if __name__ == "__main__":
    """
    """

    source_file = "sources/complete-shakespeare.txt"

    ngsl_source = "ngsl/ngsl-lemma.csv"

    ngsl = ""
    with open(ngsl_source) as f:
        ngslreader = csv.reader(f)
        for row in ngslreader:
            ngsl += ' '.join(row)
    ngsl = ngsl.split()
    ngsl = [word.lower() for word in ngsl]

    with open(source_file) as f:
        contents = f.read()

    wordfreq_dict = make_wordfreq_dict(contents)
    filtered_wordfreq_dict = filter_excluded_words(wordfreq_dict, ngsl)

    wordfreq_list = sorted([(v, k) for k, v in filtered_wordfreq_dict.iteritems()])[::-1]
    pprint.pprint(wordfreq_list)
