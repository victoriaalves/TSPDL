from sys import argv
import parser
from Tabu import Tabu


if __name__ == "__main__":
    if len(argv) != 2:
        print(f'Usage: {argv[0]} <TSPDL instance path>')
        exit(1)
    instance = parser.read_tspdl_instance(argv[1])
    tabu = Tabu(instance, 10, 100)
    tabu.run(0)
