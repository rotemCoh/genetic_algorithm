from Person import Person

class Population:
    def __init__(self, code, num_of_people):
        self.code = code
        self.people = []
        self.generations = 0
        self.num_of_people = num_of_people

    def generate_random_population(self):
        population = []
        for _ in range(self.num_of_people):
            person = Person(self.code, 0)
            self.people.append(person)
        return population

    def get_people(self):
        return self.people
    def cross_over(self):
        pass
    def fitness(self):
        word_freq = self.load_word_frequency("dict.txt")
        letter_freq = self.load_letter_frequency("Letter_Freq.txt")
        print(letter_freq)
        letter2_freq = self.load_letter_frequency("Letter2_Freq.txt")

        for person in self.people:
            code = person.get_code()
            person_fitness = 0

            # Calculate word frequency fitness
            words = code.split()
            for word in words:
                clean_word = self.clean_word(word)
                if clean_word in word_freq:
                    person_fitness += word_freq[clean_word]
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
        word_freq = {}
        with open(filename, "r") as file:
            for line in file:
                word = self.clean_word(line.strip())
                word_freq[word] = 1  # Assign a fixed frequency of 1 for each word
        return word_freq

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
    