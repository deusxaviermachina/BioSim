from Allele import *
import matplotlib.pyplot as plt


trait1=Allele(0.5, 0, "x")
trait2=Allele(0.2, 0.5, "y", )
trait3=Allele(0.8, 1, "a")
trait2.gen_genotype_population(50)


n_generations=100
trait2=Allele(0.95, 1, "y", )
AA={f"Generation{i+1}":0 for i in range(n_generations)}
Aa={f"Generation{i+1}":0 for i in range(n_generations)}
aa={f"Generation{i+1}":0 for i in range(n_generations)}
for i in range(n_generations):
    pop=trait2.gen_genotype_population(50)
    for individual in pop:
        if individual==trait2.symbol.upper()+trait2.symbol.lower():
            Aa[f"Generation{i+1}"]+=1
        elif individual==trait2.symbol.upper()*2:
            AA[f"Generation{i+1}"]+=1
        elif individual==trait2.symbol.lower()*2:
            aa[f"Generation{i+1}"]+=1
        else:
            pass
    trait2.mate(50, 0.5)
pop_size=len(trait2.gen_genotype_population(50))

print("AA",AA,"\n" "Aa",Aa,"\n","aa", aa)
ax,fig=plt.subplots(figsize=(100,50))
plt.grid(True)
X = [i for i in range(1, n_generations + 1)]
Y = [AA[f"Generation{i+1}"]/(pop_size) for i in range(n_generations)]
plt.plot(X, Y, c='blue', label=trait2.symbol.upper() * 2)
X = [i for i in range(1, n_generations + 1)]
Y = [Aa[f"Generation{i+1}"]/ (pop_size) for i in range(n_generations)]
plt.plot(X, Y, c='purple', label=trait2.symbol.upper() + trait2.symbol.lower())
X = [i for i in range(1, n_generations + 1)]
Y = [aa[f"Generation{i+1}"]/(pop_size) for i in range(n_generations)]
plt.plot(X, Y, c='red', label=trait2.symbol.lower() * 2)

plt.legend()
plt.title(f"""
Selection: {trait2.s}
Dominance: {trait2.h}""")
plt.show()

