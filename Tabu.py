from TSPDL import TSPDL

class Tabu:
    def __init__(self, instance, tabu_size, max_iterations):
        self.tspdl = TSPDL(instance)
        self.tabu_size = tabu_size
        self.max_iterations = max_iterations

    def run(self, seed):
        print(self.tspdl.generate_initial_solution())


