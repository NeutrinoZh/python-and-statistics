import random

def argmax(a):
    indexes = []
    _max = max(a)

    for i, n in enumerate(a):
        if n == _max:
            indexes.append(i)

    return indexes



numbers = [random.randint(0, 30) for i in range(100)]

freq = [0] * (abs(min(numbers)) + abs(max(numbers)) + 1)
for i in numbers:
    freq[i] += 1

modes = argmax(freq)

sort_numbers = sorted(numbers)

i = len(sort_numbers) / 2
if i == int(i):
    i = int(i)
    median = (sort_numbers[i - 1] + sort_numbers[i]) / 2
else:
    median = sort_numbers[int(i)]

average = sum(numbers) / len(numbers)

delta = [ n - average for n in numbers ]
delta_sum = round(sum(delta), 2)

print("numbers:", numbers)
print("   freq:", freq)
print("  modes:", modes)
print(" median:", median)
print("average:", round(average, 2))
print('delta:', [round(n, 2) for n in delta])
print(f'sum delta = 0({delta_sum})')

from matplotlib import pyplot as plt

plt.stairs(freq, fill=True)
plt.xlabel('value')
plt.ylabel('freq')
plt.show()