from Person import Person
from Population import Population
def main():
    given_code = "xaac, cbz"
    #test = Person(given_code, 0)
    #print(test.get_code())
    test = Population(given_code,20)
    test.generate_random_population()
    test.fitness()
    for p in test.people:
        print(p.get_fitnees())
    # taco = test.get_people()
    # for t in taco:
    #     print(t.get_code())


if __name__ == "__main__":
    main()