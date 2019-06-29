from TSPDL import TSPDL
import copy

class Tabu:
    def __init__(self, instance, tabu_size, max_iterations):
        self.tspdl = TSPDL(instance)
        self.tabu_size = tabu_size
        self.max_iterations = max_iterations

    def run(self, seed):
        current_solution = self.tspdl.generate_initial_solution()
        best_solution = copy.deepcopy(current_solution)
        print(current_solution)
        current_cost = self.tspdl.get_cost_from_solution(current_solution)
        best_solution_cost = current_cost

        while(True):
            print("New iteration.")
            best_neighbor, best_neighbor_cost = self.get_best_solution(self.tspdl.get_all_valid_neighbors(current_solution))
            if best_neighbor_cost < best_solution_cost:
                best_solution = best_neighbor
                best_solution_cost = best_neighbor_cost
                print(f'Updated best solution. New best cost is {best_solution_cost}')
            else:
                break

    def get_best_solution(self, solutions):
        best_solution = []
        best_cost = 10000000
        for solution in solutions:
            cost = self.tspdl.get_cost_from_solution(solution)
            if cost < best_cost:
                best_cost = cost
                best_solution = solution
        return best_solution, best_cost

