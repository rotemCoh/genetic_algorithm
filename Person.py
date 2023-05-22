import random
class Person:
    # def __init__(self, code, fitness):
    #     self.code = code
    #     self.alphabet = {}
    #     self.alphabet = self.generate_random_alphabet()
    #     self.update_code()
    #     self.fitness = fitness

    def __init__(self, code, fitness, alphabet):
        self.code = code
        self.fitness = fitness
        self.alphabet = alphabet
        self.update_code()

    def update_code(self):
        updated_code = ""
        for char in self.code:
            if char.isalpha():
                updated_code += self.alphabet[char.upper()]
            else:
                updated_code += char
        self.code = updated_code

    def mutate(self):
        # Select a random position in the code
        print(self.code)
        print(self.alphabet)
        # Filter out non-letter characters
        letters = [char for char in self.code if char.isalpha()]

        # Randomly choose a letter to replace
        if letters:
            letter_to_replace = random.choice(letters)

        # Randomly choose a replacement letter
        replacement_letter = random.choice(list(self.alphabet.keys()))

        # Replace the chosen letter with the replacement letter
        updated_text = self.code.replace(letter_to_replace, replacement_letter.lower())
        # wanted_key = {i for i in self.alphabet if self.alphabet[i] == replacement_letter.lower()}
        # # print(wanted_key)
        # self.alphabet.update({list(wanted_key)[0]: letter_to_replace})

        self.alphabet.update({replacement_letter.upper(): letter_to_replace})
        # self.alphabet.update({letter_to_replace: replacement_letter.upper()})



        print(updated_text)
        print(self.alphabet)


    def get_code(self):
        return self.code
    def get_fitnees(self):
        return self.fitness
    def get_alphabet(self):
        return self.alphabet




