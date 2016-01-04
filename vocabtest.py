"""
Demonstrate the open() builtin method and show some 
example of what we can do with the resulting object.
"""
import pickle

if __name__ == "__main__":
    """
    this is like a main() method
    """

    filename = "mm.txt"
    mode = 'r'

    # list of words in the ngsl
    with open('ngsl.pickle') as f:
        ngsl = pickle.load(f)
        print len(ngsl)

    with open(filename, mode) as f:

        contents = f.read()
        words = contents.split()
        print len(words)
