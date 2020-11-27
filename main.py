from Trait import *
a1 = Trait(0.9, 0.75, "A",100)
a2=Trait(0.5, 0.5, "A",100)
a3=Trait(0.1, 0.3, "A",100)
a4=Trait(0.2, 0.8, "A",100)
n_generations=1000
dataset = a1.evolve(n_generations)
#print(a1.get_average_frequencies(1000))
a1.freq_plot(n_generations)
a2.freq_plot(n_generations)
a3.freq_plot(n_generations)
a4.freq_plot(n_generations)
