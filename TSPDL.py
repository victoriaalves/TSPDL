

class TSPDL:
    def __init__(self, instance):
        self.instance = instance

    def generate_initial_solution(self):
        total_demand = self.get_total_demand()
        print(self.find_eligible_ports(total_demand))

    def get_total_demand(self):
        total = 0
        for value in self.instance['demand']:
            total = total + int(value)
        return total

    def find_eligible_ports(self, needed_draft):
        eligible_drafts = []
        for i,port_draft in enumerate(self.instance['draft']):
            if int(port_draft) >= needed_draft:
                eligible_drafts.append(i)
        return eligible_drafts