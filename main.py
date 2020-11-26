from Trait import *
a1 = Trait(0.9, 0.75, "A",100)
n_generations=1000
dataset = a1.evolve(n_generations)
print(a1.get_average_frequencies(1000))
a1.freq_plot(n_generations)
