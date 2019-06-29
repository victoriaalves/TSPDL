from TSPDL import TSPDL
import copy

class Tabu:
    def __init__(self, instance, tabu_size, max_iterations, max_iterations_without_improvement):
        self.tspdl = TSPDL(instance)
        self.tabu_size = tabu_size
        self.tabu_list = [None] * tabu_size
        self.max_iterations = max_iterations
        self.max_iterations_without_improvement = max_iterations_without_improvement

    def run(self, seed):
        current_solution = self.tspdl.generate_initial_solution()
        best_solution = copy.deepcopy(current_solution)
        current_cost = self.tspdl.get_cost_from_solution(current_solution)
        best_solution_cost = current_cost
        print(current_solution, current_cost)

        iteration = 0
        iterations_without_improvement = 0
        while(iteration < self.max_iterations and iterations_without_improvement < self.max_iterations_without_improvement):
            best_neighbor, best_neighbor_cost = self.get_best_neighbor(self.tspdl.get_all_valid_neighbors(current_solution, self.tabu_list))
            current_solution = best_neighbor.solution
            current_cost = best_neighbor_cost
            self.add_to_tabu(best_neighbor.swap, iteration)

            if best_neighbor_cost < best_solution_cost:
                best_solution = best_neighbor.solution
                best_solution_cost = best_neighbor_cost
                print(f'[Iteration {iteration}] Updated best solution. New best cost is {best_solution_cost}')
                print(f'[Iteration {iteration}] Updated best solution. New best solution is {best_solution}')
                iterations_without_improvement = 0

            print(f'Iteration {iteration}')
            iterations_without_improvement = iterations_without_improvement + 1
            iteration = iteration + 1
        print(f'[Iteration {iteration}] Best solution found was {best_solution} with cost {best_solution_cost}')
                
    def get_best_neighbor(self, neighbors):
        best_neighbor = None
        best_cost = 10000000
        for neighbor in neighbors:
            cost = self.tspdl.get_cost_from_solution(neighbor.solution)
            if cost < best_cost:
                best_cost = cost
                best_neighbor = neighbor
        return best_neighbor, best_cost

    def add_to_tabu(self, swap_tuple, iteration):
        self.tabu_list[iteration % self.tabu_size] = swap_tuple
