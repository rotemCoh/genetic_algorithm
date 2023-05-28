import random
class Person:

    # constructor.
    def __init__(self, code, fitness, alphabet):
        self.code = code
        self.fitness = fitness
        self.alphabet = alphabet
        self.new_code = ""        

    # funtion that update the code after a change.
    def update_code(self):
        updated_code = ""
        for char in self.code:
            if char.isalpha():
                updated_code += self.alphabet[char.upper()]
            else:
                updated_code += char
        self.new_code = updated_code

    # function that mutate the code of a person.
    def mutate(self):
        # Filter out non-letter characters
        letters = [char for char in self.code if char.isalpha()]

        # Randomly choose a letter to replace
        if letters:
            letter_to_replace = (random.choice(letters)).upper()

        # Randomly choose a replacement letter
        replacement_letter = random.choice(list(self.alphabet.keys()))

        # update the dictionary
        self.alphabet[letter_to_replace], self.alphabet[replacement_letter] = self.alphabet[replacement_letter], self.alphabet[letter_to_replace]
        self.update_code()

    # a getter for the code.
    def get_code(self):
        return self.code

    # a getter for the new code.
    def get_new_code(self):
        return self.new_code

    # a getter for the fitness.
    def get_fitness(self):
        return self.fitness

    # a getter for the alphabet.
    def get_alphabet(self):
        return self.alphabet
