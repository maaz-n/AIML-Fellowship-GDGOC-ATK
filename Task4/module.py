from modules.file_handling import utils
from modules.calc import calc

utils.write_to_file("./test.txt", "FAAAHHH")

print('Reading file "test.txt": ', end=" ")
utils.read_file("./test.txt")

print("\nPerforming basic calc functions on two numbers: 7, 2")
print("Addition")
calc.add(7, 2)
print("\nSubtraction")
calc.subtract(7, 2)
print("\nMultiplication")
calc.multiply(7, 2)
print("\nDivision")
calc.divide(7, 2)