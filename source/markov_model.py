from dictogram import Dictogram 
from pprint import pprint
import random, sys
    

class Markov(object):


    def __init__(self, word_list):
        self.types = self.make_types(word_list)
        self.types_counts = self.make_types_counts(word_list)


    def make_types(self, word_list):
        front_words_dict = self.check_front_word(word_list)
        # pprint(front_words_dict)

        types = {}
        for word in front_words_dict:
            # pprint(word)
            types[word] = self.create_dictogram(front_words_dict[word])
            # pprint(types)
            # pprint(types[word])
        pprint(types)
        return types


    def create_dictogram(self, types):
        dicto = dict()
        # print("\n\ntypes: {}".format(types))

        for word in types:
            if word not in dicto:
                dicto[word] = 1
            else:
                dicto[word] += 1
            
        return dicto


    def count_sorter(self, dicto):
        recurrents, count = [], []

        for word in dicto:
            num = dicto[word]

            if num not in recurrents:
                recurrents.append(num)
                num_list = (num, [word])
                count.append(num_list)
            else:
                for index in count:
                    if num == index[0]:
                        index[1].append(word)

        return sorted(count)


    def make_types_counts(self, word_list):
        types_counts = {}

        for word in self.types:
            types_counts[word] = self.count_sorter(self.types[word])
        
        return types_counts
    

    def check_front_word(self, word_list):
        front_words_dict = dict()
        body_length = len(word_list)

        for counter in range(-1, body_length):
            if counter == -1:
                word = "start"
                word_next = word_list[counter + 1]
            elif counter == body_length - 1:
                word = word_list[counter]
                word_next = "stop"
            else:
                word = word_list[counter]
                word_next = word_list[counter + 1]

            if word not in front_words_dict:
                front_words_dict[word] = [word_next]
            else:
                front_words_dict[word].append(word_next)

        return front_words_dict


    def select_word_length(self, num_of_words):
        words_selected = []
        word = "start"

        for _ in range(0, num_of_words):
            word_selected = self.select_word(word)
            
            if word_selected == "stop":
                break
            else:
                words_selected.append(word_selected)
                word = word_selected

        # print(words_selected)
        return words_selected


    def select_word(self, word):
        frequency_distribution = self.calculate_frequency_distribution()
        # print(frequency_distribution)

        if word in frequency_distribution:
            freq = frequency_distribution[word]
            # print(freq)
            rand_num = random.random()

            for j in range(0, len(freq)):
                print("freq length: {}".format(len(freq)))

                if rand_num < freq[j]:
                    # print(rand_num)
                    print(self.types_counts[word][j][1])
                    # print(len(self.types_counts[word][j][1]))
                    test_dummy = random.randint(0, len(self.types_counts[word][j][1]) - 1)
                    # print(test_dummy)
                    rand_num = test_dummy
                    word_selected = self.types_counts[word][j][1][rand_num]
                    # print(word_selected)
                    return word_selected
                # else:
                #     pass


    def calculate_frequency_distribution(self):
        frequency_distribution = dict()
        # print(self.types_counts)

        for word in self.types_counts:
            frequency_distribution[word] = self.distribute_calculator(self.types[word], self.types_counts[word])
            # print(frequency_distribution[word])
        
        # print(frequency_distribution)
        return frequency_distribution


    def distribute_calculator(self, total_tokens, histogram):
        tokens = 0
        # print(total_tokens)
        # print(histogram)

        for k, words in histogram:
            # print(k)
            # print(words)
            tokens = (k * len(words))
            # print(tokens)

        freqs, sum_freqs = [], 1

        for ind in range(tokens):
            sum_freqs += ind/len(total_tokens)
            freqs.append(sum_freqs)
            # print(freqs)
        
        # print("break\n\n")
        return freqs
    

    def generate_sentence(self, word_list):
        # print(word_list)
        sentence = " ".join(word_list)
        # sentence[0] = sentence[0].upper()
        sentence += "."
        return sentence


def main():
    # f = open("the_count_of_monte_cristo.txt", "r").read()
    # word_list = test_sentence.split()

    test_sentence = "will you participate in the conference with new fellows on saturday evening after registration will you participate in the workshops on monday morning interested in sharing a room"
    word_list = test_sentence.split() # REMOVE self TEST CODE FOR TEXT FILE

    # pprint(word_list)
    markov = Markov(word_list)
    num_of_words = markov.select_word_length(15)
    # print(num_of_words)

    sentence_gen = markov.generate_sentence(num_of_words)
    print(sentence_gen)

if __name__ == "__main__":
    main()
