import assignment
import sys

hours = int(sys.argv[1])
cpus = int(sys.argv[2])
price = float(sys.argv[3])
val = assignment.get_costs(hours,cpus,price)
print(val)