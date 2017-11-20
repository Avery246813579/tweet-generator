#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):

    def __init__(this, word_list=None):
        super(Listogram, this).__init__()  # Initialize this as a new list
        this.types = 0  
        this.tokens = 0  
        this.word_freq = list()

        if word_list is not None:
            for word in word_list:
                this.add_count(word)

    def add_count(this, word, count=1):
        does_not_exist = True

        for word_value in this.word_freq:
            if word == word_value[0]:
                word_value[1] += count
                does_not_exist = False
                this.tokens += 1

        if does_not_exist: 
            this.word_freq.append([word, 1])
            this.tokens += count
            this.types += 1
        

    def frequency(this, word):
        index = 0
        
        for item in this.word_freq:
            if item[0] == word:
                return this.word_freq[index][1]
            index += 1


    def __contains__(this, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        pass
        # for word_val in this.word_freq:
        #     # if word == 

    # def _index(this, target):
    #     """Return the index of entry containing given target word if found in
    #     this histogram, or None if target word is not found."""
    #     # TODO: Implement linear search to find index of entry with target word


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram.word_freq))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
