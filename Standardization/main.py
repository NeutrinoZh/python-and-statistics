import math

numbers = [ 5, 5, 4, 6, 7, 8, 1, 7, 9, 6, 7 ]
average = sum(numbers) / len(numbers)
sD = math.sqrt(sum([(average - n)**2 for n in numbers]) / (len(numbers) - 1))

zNumbers = [ (n - average) / sD for n in numbers ]
zAverage = round(sum(zNumbers) / len(zNumbers), 2)

print("average  :", average)
print("variance:", round(sD, 2))
print("average-z:", zAverage)

print("numbers  :", numbers)
print("z-numbers:", [ round(n, 2) for n in zNumbers ])