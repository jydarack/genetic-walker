from mesa import Agent, Model
from mesa.time import SimultaneousActivation
from mesa.space import ContinuousSpace

GeneSet = ["u", "d", "l", "r"]

GENERATIONS = 50


class Walker(Agent):
    def __init__(self, unique_id, model, genes=[]):
        super().__init__(unique_id, model)
        self.fitness = 0
        self.genes = (
            genes
            if genes != []
            else [self.random.choice(GeneSet) for _ in range(GENERATIONS)]
        )
        self.pos = (0, 0)

    def get_fitness(self, target):
        # geometric distance & prise en compte du nombre d'étapes
        return 10000

    def step(self):
        ## preparation du mouvement
        pass

    def advance(self):
        ## Mouvement
        pass


class Parkur(Model):
    def __init__(self):
        super().__init__()
        self.schedule = SimultaneousActivation(self)
        self.grid = ContinuousSpace(75, 40, False)

        ## Creation des agents de base
        for _ in range(1):
            a = Walker(self.next_id(), self)
            self.schedule.add(a)
            self.grid.place_agent(a, (0, 0))

    def step(self):
        self.schedule.step()
