
from sys import argv

if __name__ == '__main__':
   if len(argv) != 2:
      print('Usage: %s <huisman instance path>' % argv[0])
      exit(1)

   inst = read_huisman_instance(argv[1])
   write_glpk_instance(inst)