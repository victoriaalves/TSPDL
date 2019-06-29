from sys import argv
import parser
from Tabu import Tabu


if __name__ == "__main__":
    if len(argv) != 2:
        print(f'Usage: {argv[0]} <TSPDL instance path>')
        exit(1)
    instance = parser.read_tspdl_instance(argv[1])
    tabu_size = 10 if int(instance['number_of_ports']) < 50 else 1000
    tabu = Tabu(instance, 1000, tabu_size, 500)
    tabu.run(0)
