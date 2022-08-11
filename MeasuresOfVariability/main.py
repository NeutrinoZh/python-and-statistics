import math

numbers = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]

R = max(numbers) - min(numbers)

average = sum(numbers) / len(numbers)
D = math.sqrt(sum([(average - n)**2 for n in numbers]) / (len(numbers) - 1))

print("Range:", R)
print("Variance:", round(D, 2))


print("Confirmation of dispersion properties:")

c = 3

test_one = [ n + c for n in numbers ]
average_one = sum(test_one) / len(test_one)
one_D = math.sqrt(sum([(average_one - n)**2 for n in test_one]) / (len(test_one) - 1))

test_two = [ n * c for n in numbers ]
average_two = sum(test_two) / len(test_two)
two_D = math.sqrt(sum([(average_two - n)**2 for n in test_two]) / (len(test_two) - 1))

print("first property:", one_D == D)
print("second property:", two_D == D * c)