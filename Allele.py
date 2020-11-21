import random

class Allele:
    def __init__(self,s,h,symbol):
        self.s=s
        self.h=h
        """
        DOMINANCE COEFFICIENT=H:
        IF H = 1, then allele 'a' is fully dominant (meaning that Genotype Aa--->phenotype a 100% of the time).
        If H=0, the opposite is true: "A" is fully dominant, so Genotype Aa--->phenotype A 100% of the time
        if H=0.5, then Aa;s fitness is intermediate with respect to AA and aa. EG suppose
        that S=0.75 and H=0.5. fitness(AA)=1, fitness(aa)=1-s=1-0.75=0.25,. 1-h(s)= 1-(0.5*0.75) = 1-0.375=0.625
        So, we have aa=0.25, Aa=0.625, AA=1
        
        'DOMINANCE COEFF.' IS ESSENTIALLY JUST MEASURES 'THE DEGREE OF PHENOTYPIC SIMILARITY OF THE
        'WEAK' HOMOZYGOTE (TYPICALLY REPRESENTED WITH LOWERCASE CHARACTERs) TO THE HETEROZYGOTE'--
        SO, A DOMINANCE SCORE OF "1" MEANS THE FOLLOWING:
        
        H=1 ---> [(AA--->A) & (Aa--->a) & (aa--->a)]   
        
        i.e. the phenotypic expression of the "aa" homozygote 
        will be identical to that of the heterozygote
        
        A DOMINANCE SCORE OF "0" WOULD MEAN THE OPPOSITE, SO:
        H=0 ---> [(AA--->A) & (Aa--->A) & (aa--->a)]
        
        i.e. the AA homozygote's phenotypic expression is no different from that of the "Aa" homozygote
        """
        self.symbol=symbol.lower()

    def gen_genotype_population(self,pop_size):
        pop=[]
        """
        create a 'strong'("A") and a 'weak'("a")
        allele variable.
        """
        allele1, allele2=self.symbol.upper(), self.symbol.lower()
        AA=self.symbol.upper()*2
        Aa=self.symbol.upper()+self.symbol.lower()
        aa=self.symbol.lower()*2
        AA_fitness=1
        Aa_fitness=1-self.h*self.s
        aa_fitness=1-self.s
        population=random.choices([AA,Aa,aa], weights=[AA_fitness,Aa_fitness,aa_fitness],k=pop_size)
        return population

    def mate(self,pop_size,survival_to_death_ratio):
        pop=self.gen_genotype_population(pop_size)
        """
        'culling of the weak' as it were--a fraction of the population survives into next generation,
        hence the 'survival to death ratio'
        """
        new_pop=random.choices(pop, k=int(pop_size*survival_to_death_ratio))
        [mate1, mate2] = [random.choice(pop), random.choice(pop)]
        zygote = []
        #this is similar to a Punnett square--a crossover/breeding event
        for mate in [mate1, mate2]:
            if mate == self.symbol.upper() * 2:
                zygote.append(self.symbol.upper())
            elif mate == self.symbol.lower() * 2:
                zygote.append(self.symbol.lower())
            else:
                zygote.append(random.choices([self.symbol.upper(), self.symbol.lower()],
                                             weights=(1 - self.s * self.h, 1 - self.s), k=1)[0])
            print(zygote)
        if [zygote[0], zygote[1]] == [self.symbol.lower(), self.symbol.upper()]:
            [zygote[0], zygote[1]] = [zygote[1], zygote[0]]
            print("updated: ", zygote, ('').join(zygote))

        for i in range(int(survival_to_death_ratio*pop_size)):
            new_pop.append(('').join(zygote))
        return "New Population: ",new_pop

if __name__ == "__main__":
    pop_size=100
    pop=Allele(0,0.3, "a").gen_genotype_population(pop_size)
    count_AA=0
    count_Aa=0
    count_aa=0
    for i in pop:
        if i =="AA":
            count_AA+=1
        elif i =="Aa":
            count_Aa+=1
        else:
            count_aa+=1
    print(" Count of AA Genotype:",count_AA,"\n","Count of Aa Genotype:",count_Aa,"\n","Count of aa genotype:",count_aa)
    print("INITIAL POPULATION: ","\n",pop)
    survival_to_death_ratio=0.5
    #proportion of population that survives to mating age
    new_pop=random.choices(pop,k=int(len(pop)*survival_to_death_ratio))
    print("\n","New Mating Pool After Selection Pressures Applied","\n",new_pop)
    AA=new_pop.count("AA")
    Aa=new_pop.count("Aa")
    aa=new_pop.count('aa')
    print("Freq of genotypes in new mating pool:","\n", "AA: ", AA,"\n","Aa: ",Aa, "\n","aa: ",aa)
