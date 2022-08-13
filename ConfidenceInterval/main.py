import math
from pytools import average

def random_sample(n, a=0, b=9):
    from random import randint
    return [ randint(a, b) for _ in range(n) ]

def distribution(sample):
    begin = min(sample)

    freq = [0] * (max(sample) - begin + 1)
    for i in sample:
        freq[i - begin] += 1
    return freq

def math_sd(sample, mean):
    return math.sqrt(sum([(mean - n)**2 for n in sample]) / (len(sample) - 1))

sample = random_sample(100)
mean = average(sample)
sd = math_sd(sample, mean)
se = sd / math.sqrt(len(sample))
interval = ( mean - 1.96 * se, mean + 1.96 * se )

print("95% ConfidenceInterval:", interval)