from Person import Person
import random
import string

class Population:
    def __init__(self, code, num_of_people):
        self.code = code
        self.people = []
        self.generations = 0
        self.num_of_people = num_of_people
    def generate_random_alphabet(self):
        alphabet = {'A': 't', 'B': 'g', 'C': 'o', 'D': 'n', 'E': 'b', 'F': 'h', 'G': 'i', 'H': 'v', 'I': 'j', 'J': 'z', 'K': 'k', 'L': 'y', 'M': 'w', 'N': 'm', 'O': 'x', 'P': 'd', 'Q': 'q', 'R': 'p', 'S': 'c', 'T': 'a', 'U': 'r',
        'V': 'e', 'W': 's', 'X': 'u', 'Y': 'f', 'Z': 'l'}
        random_alphabet = {}
        available_letters = list('abcdefghijklmnopqrstuvwxyz')
        for key in alphabet:
            random_index = random.randint(0, len(available_letters) - 1)
            random_letter = available_letters.pop(random_index)
            random_alphabet[key] = random_letter
        return random_alphabet

    def generate_random_population(self):
        population = []
        for p in range(self.num_of_people):
            person = Person(self.code, 0, self.generate_random_alphabet())
            person.update_code()
            self.people.append(person)
        return population

    def get_people(self):
        return self.people

    def fitness(self):
        word_dict = self.load_word_frequency("dict.txt")
        letter_freq = self.load_letter_frequency("Letter_Freq.txt")
        letter2_freq = self.load_letter_frequency("Letter2_Freq.txt")

        for person in self.people:
            code = person.get_new_code()
            person_fitness = 0

            # Calculate word frequency fitness
            words = code.split()
            for word in words:
                clean_word = self.clean_word(word)
                if clean_word in word_dict:
                    person_fitness += word_dict[clean_word]
                else:
                    # Calculate letter frequency fitness
                    letter_counter = []
                    for l in code:
                        letter_counter.append(l)
                    for lt in letter_counter:
                        if lt.isalpha():
                            if lt.upper() in letter_freq:
                                person_fitness += letter_freq[lt.upper()]

                    # Calculate letter combination frequency fitness
                    for i in range(len(code) - 1):
                        letter_combination = code[i:i + 2]
                        if letter_combination.isalpha():
                            if letter_combination.upper() in letter2_freq:
                                person_fitness += letter2_freq[letter_combination.upper()]

                        person.fitness = person_fitness

    def load_word_frequency(self, filename):
        word_dict = {}
        with open(filename, "r") as file:
            for line in file:
                word = self.clean_word(line.strip())
                word_dict[word] = 1  # Assign a fixed frequency of 1 for each word
        return word_dict

    def load_letter_frequency(self, filename):
        letter_freq = {}
        with open(filename, "r") as file:
            for line in file:
                if "#" not in line:
                    striped = line.strip("\n")
                    if len(striped) >= 2:
                        freq, letter = striped.split()
                        letter_freq[letter] = float(freq)
        return letter_freq

    def clean_word(self, word):
        return word.strip(",.;")

    def new_generation(self):
        new_people = []
        top_five = int(self.num_of_people*0.05)
        twenty_percent = int(self.num_of_people*0.2)
        temp_fitness = 0
        best_string = ''
        best_dict = {}
        for p in self.people:
            if p.get_fitness() > temp_fitness:
                temp_fitness = p.get_fitness()
                best_string = p.get_new_code()
                best_dict = p.get_alphabet()

        for i in range(top_five):
            new_people.append(Person(best_string, 0, best_dict))

        self.prepering_for_crossover()

        #indexes = list(range(len(self.people)))
        random_indexes = random.sample(range(len(self.people)), twenty_percent)

        for index in random_indexes:
            self.people[index].mutate()

        for y in range(self.num_of_people - top_five):
            new_people.append(self.people[y])

        self.people = new_people
        self.generations = self.generations + 1
        #for i in self.people:
        #    print(i.get_new_code())
        return best_string , best_dict

    def prepering_for_crossover(self):
        # Get the indexes of the people
        indexes = list(range(len(self.people)))

        # Create a list of tuples with two randomly selected people
        pairs = []
        while len(indexes) >= 2:
            random_pair_indexes = random.sample(indexes, 2)
            random_pair = (self.people[random_pair_indexes[0]], self.people[random_pair_indexes[1]])
            pairs.append(random_pair)
            indexes.remove(random_pair_indexes[0])
            indexes.remove(random_pair_indexes[1])

        for t in pairs:
            self.crossover(t)

    def crossover(self, couple_of_people):
        person1, person2 = couple_of_people
        alphabet1 = person1.get_alphabet()
        alphabet2 = person2.get_alphabet()

        # get the values of every dict
        keys = list(map(str, alphabet1.keys()))
        values1 = list(map(str, alphabet1.values()))
        values2 = list(map(str, alphabet2.values()))
        random_index = random.randint(0, 25)

        # generate the new values
        crossover_result1 = values1[:random_index] + values2[random_index:]
        crossover_result2 = values2[:random_index] + values1[random_index:]

        # replace all duplicated letters with none.
        crossover_result1_with_none = self.add_None_values(crossover_result1)
        crossover_result2_with_none = self.add_None_values(crossover_result2)

        # finding the values without duplication.
        crossover_result1_no_dups = self.replace_None_values(crossover_result1_with_none)
        crossover_result2_no_dups = self.replace_None_values(crossover_result2_with_none)

        new_alphabet1 = {k: v for k, v in zip(keys, crossover_result1_no_dups)}
        new_alphabet2 = {k: v for k, v in zip(keys, crossover_result2_no_dups)}

        #print("before: " + str(person1.get_alphabet()))
        person1.alphabet = new_alphabet1
        #print("after: " + str(person1.get_alphabet()))
        #print("before: " + str(person1.get_new_code()))
        person1.update_code()
        #print("after: " + str(person1.get_new_code()))
        person2.alphabet = new_alphabet2
        person2.update_code()



    # function that replaces duplicated letter with None
    def add_None_values(self, crossover_result):
        frequency = {}
        values_with_none = []

        for letter in crossover_result:
            frequency[letter] = frequency.get(letter, 0) + 1
            if frequency[letter] > 1:
                values_with_none = values_with_none + [None]
            else:
                values_with_none = values_with_none + list(letter)
        return values_with_none

    def replace_None_values(self, crossover_result_with_none):
        # Create a set from the letters in my_list (excluding None values)
        existing_letters = [letter for letter in crossover_result_with_none if letter is not None]

        # Create a new list of English letters not in my_list
        new_list = [letter for letter in string.ascii_lowercase if letter not in existing_letters]

        random.shuffle(new_list)  # Shuffle new_list randomly

        complite_vlues_crossover = []
        new_list_index = 0
        for value in crossover_result_with_none:
            if value is None:
                random_letter = new_list[new_list_index]
                complite_vlues_crossover.append(random_letter)
                new_list_index += 1
            else:
                complite_vlues_crossover.append(value)

        return complite_vlues_crossover