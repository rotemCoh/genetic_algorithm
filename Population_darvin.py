from Person import Person
import random
import string
import math
from Levenshtein import distance
from copy import deepcopy

class Population_darvin:
    def __init__(self, code, num_of_people, num_mutations):
        self.code = code
        self.people = []
        self.generations = 0
        self.num_mutations = num_mutations
        self.num_of_people = num_of_people
        self.letter2_freq = self.load_letter_frequency("Letter2_Freq.txt")
        self.word_list_from_file = self.words_from_dict("dict.txt")
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

    def clean_code(self, code):
        words_list = code.split()
        clean_list = []
        for word in words_list:
            clean_word = word.strip(",.;")
            clean_list.append(clean_word)
        return clean_list

    def words_from_dict(self,filename):
        words_from_dict = {}
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                line_length = len(line)
                words_from_dict.setdefault(line_length, []).append(line)
        return words_from_dict

    def find_word(self, words_dict, word):
        #max_grade = 0  # Track the maximum grade encountered
        haming_dist = 0
        word_length = len(word)
        if word_length in words_dict:
            if word in words_dict[word_length]:
                return 100
            else:
                haming_dist = min([distance(w, word) for w in words_dict[word_length]])
                if haming_dist <=math.floor(word_length/2):
                    return (1-haming_dist/len(word))*100
            if haming_dist > 0:
                return haming_dist
            else:
                return None

    def grade_2letter(self, letter2_freq, word):
        one_letter_check = len(word) -1
        if one_letter_check == 0:
            return 0
        grade = 0
        count = len(word)
        for i in range(len(word) - 1):
            letter_combination = word[i:i + 2]
            if letter_combination.isalpha():
                if letter_combination.upper() in letter2_freq:
                    grade += letter2_freq[letter_combination.upper()]
        final_grade = grade*1000
        return final_grade/(count-1)
    
    def fitness(self):
        for person in self.people:
            code = person.get_new_code()
            person_fitness = 0
            cleaned_code = self.clean_code(code)
            for word in cleaned_code:
                grade =  self.find_word(self.word_list_from_file, word)
                if grade != None:
                    person_fitness += grade
                else:
                    person_fitness += self.grade_2letter(self.letter2_freq, word)
            final_fit = person_fitness/len(cleaned_code)
            person.fitness = final_fit

    def fitness_for_one(self, person):
        code = person.get_new_code()
        person_fitness = 0
        cleaned_code = self.clean_code(code)
        for word in cleaned_code:
            grade =  self.find_word(self.word_list_from_file, word)
            if grade != None:
                person_fitness += grade
            else:
                person_fitness += self.grade_2letter(self.letter2_freq, word)
        final_fit = person_fitness/len(cleaned_code)
        person.fitness = final_fit

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
    
    def darvin(self):
        for person in self.people:
            temp_person = Person(person.get_code(), person.get_fitness(), deepcopy(person.get_alphabet()))
            for m in range(self.num_mutations):
                temp_person.mutate()
            self.fitness_for_one(temp_person)
            if temp_person.get_fitness() > person.get_fitness():
                person.fitness = temp_person.fitness

    def new_generation(self):
        self.darvin()
        new_people = []
        sixty_percent = int(self.num_of_people*0.6)
        temp_fitness = 0
        best_string = ''
        best_dict = {}
        for p in self.people:
            if p.get_fitness() > temp_fitness:
                temp_fitness = p.get_fitness()
                best_string = p.get_new_code()
                best_dict = p.get_alphabet()
        #print(temp_fitness)
        amount = temp_fitness/10
        amount = math.ceil((self.num_of_people/100)*amount)

        for i in range(amount):
            new_people.append(Person(p.get_code(), 0, deepcopy(best_dict)))
        for p in new_people:
            p.update_code()
        self.prepering_for_crossover()

        random_indexes = random.sample(range(len(self.people)), sixty_percent)

        for index in random_indexes:
           self.people[index].mutate()

        for y in range(self.num_of_people - amount):
            new_people.append(deepcopy(self.people[y]))
        for p in new_people:
            p.update_code()
        self.people = new_people
        #print("population leangth: " +str(len(self.people)))
        self.generations = self.generations + 1
        print("Genaration number: " + str(self.generations))
        print("fitness grade: " + str(temp_fitness))
        print("Number of calls to fitness function per generation: " + str(int(self.generations)*2))
        print("Number of calls to fitness in total " + str(int(self.generations)*int(self.num_of_people)*2))
        return best_string , best_dict, temp_fitness

    def prepering_for_crossover(self):
        # Get the indexes of the people
        savion = []
        for p in self.people:
            for _ in range(int(p.get_fitness())):
                savion.append(deepcopy(p))

        indexes = list(range(len(savion)))

        # Create a list of tuples with two randomly selected people
        pairs = []
        while len(pairs) <= self.num_of_people/2:
            random_pair_indexes = random.sample(indexes, 2)
            random_pair = (savion[random_pair_indexes[0]], savion[random_pair_indexes[1]])
            pairs.append(random_pair)

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

        person1.alphabet = new_alphabet1
        person1.update_code()
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