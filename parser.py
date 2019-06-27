
from sys import argv


def skip(lines, fp):
    for _ in range(lines):
        fp.readline()

def read_tspdl_instance(filepath):
    inst = {}
    inst["filename"] = filepath.split("/")[-1]
    print(f'Reading file {inst["filename"]}')
    with open(filepath, 'r') as fp:
        skip(4, fp)
        inst["number_of_ports"] = int(fp.readline().split()[1])

        skip(10, fp)
        inst["cost"] = []
        for _ in range(inst["number_of_ports"]):
            inst["cost"].append(fp.readline().split())

        skip(8, fp)
        inst["demand"] = fp.readline().split()

        skip(2, fp)
        inst["draft"] = fp.readline().split()
    return inst

def write_glpk_instance(inst):
    with open("instances/glpk/" + inst["filename"], 'w') as fp:
        fp.write('#\n')
        fp.write('# GLPK data file generated by %s.\n#\n\n' % argv[0])

        fp.write('set V :=')
        for i in range(inst["number_of_ports"]):
            fp.write(f' {i+1}')
        fp.write(';\n\n')

        fp.write('param d :=\n')
        for i in range(inst["number_of_ports"]):
            fp.write(f'   {i+1} {inst["demand"][i]}\n')
        fp.write(';\n\n')

        fp.write('param l :=\n')
        for i in range(inst["number_of_ports"]):
            fp.write(f'   {i+1} {inst["draft"][i]}\n')
        fp.write(';\n\n')

        fp.write('param custo :=\n')
        for i in range(inst["number_of_ports"]):
            for j in range(inst["number_of_ports"]):
                fp.write(f'   {i+1} {j+1} {inst["cost"][i][j]}\n')
        fp.write(';\n\n')

        fp.write('end;\n')

if __name__ == '__main__':
   if len(argv) != 2:
      print(f'Usage: {argv[0]} <TSPDL instance path>')
      exit(1)

   inst = read_tspdl_instance(argv[1])
   write_glpk_instance(inst)
