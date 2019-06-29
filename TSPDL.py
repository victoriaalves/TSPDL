import random
import copy
import itertools

MOST_EXPENSIVE_ROUTE = 1000


class TSPDL:
    def __init__(self, instance):
        self.instance = instance

    def generate_initial_solution(self):
        all_ports = range(0, int(self.instance["number_of_ports"]))
        solution = []
        solution.append(0)
        # Starting from garage
        current_demand = self.get_total_demand()
        eligible_ports = self.find_eligible_ports(current_demand, [x for x in all_ports if x not in solution])
        next_port = self.find_cheapest_route(0, eligible_ports)
        solution.append(next_port)
        current_demand = current_demand - int(self.instance['demand'][next_port])
        # Finding intermiate route
        for i in range(1, int(self.instance['number_of_ports']) - 1):
            eligible_ports = self.find_eligible_ports(current_demand, [x for x in all_ports if x not in solution])
            next_port = self.find_cheapest_route(solution[-1], eligible_ports)
            solution.append(next_port)
            current_demand = current_demand - int(self.instance['demand'][next_port])
        # Going back to garage
        solution.append(0)

        return solution

    def get_total_demand(self):
        total = 0
        for value in self.instance['demand']:
            total = total + int(value)
        return total

    def find_eligible_ports(self, needed_draft, candidates):
        eligible_drafts = []
        for i in candidates:
            if int(self.instance['draft'][i]) >= needed_draft:
                eligible_drafts.append(i)
        return eligible_drafts

    def find_cheapest_route(self, origin, candidates):
        cheapest_route = MOST_EXPENSIVE_ROUTE
        cheapest_route_index = -1
        for i in candidates:
            if int(self.instance['cost'][origin][i]) < cheapest_route:
                cheapest_route = int(self.instance['cost'][origin][i])
                cheapest_route_index = i
        return cheapest_route_index

    def get_cost_from_solution(self, solution):
        total_cost = 0
        for i in range(0, len(solution) - 1):
            total_cost = total_cost + int(self.instance['cost'][solution[i]][solution[i+1]])
        return total_cost

    def get_all_valid_neighbors(self, solution):
        swap_candidates = list(itertools.combinations(range(1, len(solution) - 1), 2))
        neighbors = []
        for i in range(0, len(swap_candidates)):
            new_neighbor = copy.deepcopy(solution)
            aux = new_neighbor[swap_candidates[i][0]]
            new_neighbor[swap_candidates[i][0]] = new_neighbor[swap_candidates[i][1]]
            new_neighbor[swap_candidates[i][1]] = aux
            if self.is_valid(new_neighbor):
                neighbors.append(new_neighbor)
        return neighbors

    def is_valid(self, solution):
        current_demand = self.get_total_demand()
        for i in range(1, len(solution)):
            if int(self.instance['draft'][solution[i]]) < current_demand:
                return False
            current_demand = current_demand - int(self.instance['demand'][solution[i]])
        return True

