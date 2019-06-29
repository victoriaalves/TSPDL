from TSPDL import TSPDL

class Tabu:
    def __init__(self, instance, tabu_size, max_iterations):
        self.tspdl = TSPDL(instance)
        self.tabu_size = tabu_size
        self.max_iterations = max_iterations

    def run(self, seed):
        initial_solution = self.tspdl.generate_initial_solution()
        print(initial_solution)
        initial_cost = self.tspdl.get_cost_from_solution(initial_solution)
        all_valid_neighbors = self.tspdl.get_all_valid_neighbors(initial_solution)
        print(all_valid_neighbors)
