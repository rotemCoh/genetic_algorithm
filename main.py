from Person import Person
from Population import Population
def main():
    given_code = "xaac, cbz"
    test = Population(given_code, 2)
    test.generate_random_population()
    # for i in test.people:
        # print(i.get_code())
    test.fitness()
    for p in test.people:
        # print(p.get_fitnees())
        p.mutate()
    test.new_generation()


    # taco = test.get_people()
    # for t in taco:
    #     print(t.get_code())


if __name__ == "__main__":
    main()