import random
import matplotlib.pyplot as plt

class Trait:
    def __init__(self, h: float, s: float, name: str, pop_size: int):
        self.h = h
        self.s = s
        self.name = name
        self.pop_size = pop_size

    """
    1.) Generate population of 'trait' with simulation parameters s (i.e. the selection coefficient),
    h (i.e. the dominance coefficient), population size, and name
    2.) Have population mate to produce next generation
    3.) Plot genotype frequencies
    4.) Repeat 2.) and 3.) for new generation n times
    5.) Observe data
    
    """

    def gen_population(self):
        AA = self.name[0].upper() * 2
        aa = self.name[0].upper() + self.name[0].lower()
        Aa = self.name[0].lower() * 2
        AA_fitness = 1
        Aa_fitness = 1 - self.h * self.s
        aa_fitness = 1 - self.s
        population = random.choices([AA, Aa, aa], weights=[AA_fitness, Aa_fitness, aa_fitness], k=self.pop_size)
        return population

    def get_average_frequencies(self, n_trials):

        """
        debugging mechanism to make sure that the ratio of the average frequency
        of the three genotypes is approximately equal to
        1 : 1-s(h) : 1-h
        """

        data = {"AA": 0, "aa": 0, "Aa": 0}
        for i in range(n_trials):
            pop = self.gen_population()
            data["AA"] += pop.count("AA")
            data["aa"] += pop.count("aa")
            data["Aa"] += pop.count("Aa")
        data["AA"] /= n_trials * 100
        data["aa"] /= n_trials * 100
        data["Aa"] /= n_trials * 100
        return data

    def mate(self):
        pop = self.gen_population()
        next_gen = random.choices(pop, k=int(self.pop_size))
        while len(next_gen) < self.pop_size:
            zygote = []
            [mate1, mate2] = [random.choice(pop), random.choice(pop)]
            for mate in [mate1, mate2]:
                if mate == self.name[0].upper() * 2:
                    zygote.append(self.name[0].upper())
                elif mate == self.name[0].lower() * 2:
                    zygote.append(self.name.lower())
                else:
                    zygote.append \
                        (random.choices([self.name.upper(), self.name.lower()],
                                        weights=(1 - self.s * self.h, 1 - self.s), k=1)[0])
            if [zygote[0], zygote[1]] == [self.name[0].lower(), self.name[0].upper()]:
                [zygote[0], zygote[1]] = [zygote[1], zygote[0]]

            next_gen.append(('').join(zygote))
        return next_gen

    def evolve(self, n_generations):
        data = {f"generation{i + 1}":
                    {"AA": 0,
                     "Aa": 0,
                     "aa": 0}
                for i in range(n_generations)}

        for i in range(n_generations):
            pop = self.mate()
            data[f"generation{i + 1}"]["AA"] = pop.count("AA")
            data[f"generation{i + 1}"]["Aa"] = pop.count("Aa")
            data[f"generation{i + 1}"]["aa"] = pop.count("aa")
        return data


    def freq_plot(self, n_generations):
        dataset=self.evolve(n_generations)
        ax, fig = plt.subplots(figsize=(100, 50))
        plt.grid(True)
        X1 = [i for i in range(1, n_generations + 1)]
        Y1 = [dataset[f"generation{i + 1}"]["AA"] / (self.pop_size) for i in range(n_generations)]
        X2 = [i for i in range(1, n_generations + 1)]
        Y2 = [dataset[f"generation{i + 1}"]["Aa"] / (self.pop_size) for i in range(n_generations)]
        X3 = [i for i in range(1, n_generations + 1)]
        Y3 = [dataset[f"generation{i + 1}"]["aa"] / (self.pop_size) for i in range(n_generations)]
        plt.plot(X1, Y1, c=(0.5, 0, 1), label=self.name.upper() * 2)
        plt.plot(X2, Y2, c=(0.5, 1, 0), label=self.name.upper() + self.name.lower())
        plt.plot(X3, Y3, c=(0, 0.5, 1), label=self.name.lower() * 2)
        plt.xlabel("Generation", fontsize=15)
        plt.ylabel("Frequency"
                   " (as % of total population)",fontsize=15)
        plt.legend()
        plt.title(f"""
        Selection: {self.s}
        Dominance: {self.h}""")
        plt.show()

