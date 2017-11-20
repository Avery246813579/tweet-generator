# stochastic_example.py (In-class example)


from functools import reduce
import sys, random, time
t_init = time.time()

class Stochastic(object):
    sentence = []

    def word_frequency(self, word_list, cycles):
        freq = dict()
        probabilities, res_arr = [], []
        word_counter = 0
        word_list = word_list.split(" ")
        print(word_list)

        # LIST COMPREHENSION for creating list of order-preserved user-inputted string values
        word_uniques = [[value, 1] for (item, value) in enumerate(word_list) if value not in word_list[0:item]]
        print(word_uniques)
        print(poop)

        # LOOPS through original word list and sets word frequency to frequency DICTIONARY
        for word in word_list:
            # word_counter += 1
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        print(freq)

        sum_vals = sum(freq.values())

        # Creates probability ARRAY from occurrences in frequency ARRAY
        for key, value in freq.items():
            probabilities.append(freq[key]/sum_vals)

        for _ in range(int(cycles)):
            Stochastic.frequency_distribute(self, word_uniques, freq, probabilities, res_arr)

        # Reducer that creates dictionary instances of actual word frequencies
        actual_frequency = reduce(lambda index, count: index.update([(count, index.get(count, 0) + 1)]) or index, self.sentence, {})
        
        # Print resultant sentence if number of cycles is less than 50; then print word frequencies
        if int(cycles) <= 50:
            res_sentence = "\nRESULTING SENTENCE: \n\"{}\"".format(" ".join(self.sentence))
        else:
            res_sentence = "\nRESULTING SENTENCE IS TOO LONG AND HAS BEEN OMITTED.\n"
        res_freq = "\nACTUAL WORD FREQUENCIES: \n{}".format(actual_frequency)
        
        return(res_sentence, res_freq)



    """
    Create counter variable that sums each item of probability list, then freezes at index
    where random roll value is less than the summed counter, checks the corresponding dict
    value at the matching index and prints that word out
    """
    def frequency_distribute(self, words_arr, frequency_arr, probability_arr, result_arr):
        roll_counter, range_counter = 0, 0
        prob_range= []
        roll_val = random.random()

        # Create probability RANGES mapped for every UNIQUE word in the input string
        for prob in probability_arr:
            range_counter += prob
            prob_range.append(range_counter)

        # Create mapped LIST that assigns every range map to every unique word in sequence
        assigned_ranges = [[prob_range[i], words_arr[i]] for i in range(len(prob_range))]
            
        # LOOPS through probability_arr and sets roll_counter value for word output
        for prob in probability_arr:
            roll_counter += prob
            if roll_val < roll_counter:
                break

        # LOOPS through assigned_ranges array and PRINTS word at matching frequency index
        for item in assigned_ranges:
            if roll_counter == item[0]:
                self.sentence.append(item[1])


if __name__ == "__main__":
    input_string = "it is a fair bet that if it is fair tomorrow then my fair haired wife and I will head to the spring fair which is held in a fair sized park in this fair city of ours and we may win a prize in a competition if everyone else plays fair"
    user_cycles = 30

    print("\nINPUT STRING: \"{}\"".format(input_string))
    print("INPUT CYCLES: {}\n".format(user_cycles))

    s = Stochastic()
    s.word_frequency(input_string, user_cycles)
    print("\n\nProgram runtime is as follows: {} milliseconds.\n".format(1000 * (time.time() - t_init)))
