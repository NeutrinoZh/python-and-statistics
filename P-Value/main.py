import math
from pytools import average
from scipy.stats import norm

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

sample = random_sample(32)
mod_sample = [ n - 1 for n in sample ]

mean = average(sample)
mod_mean = average(mod_sample)

sd = math_sd(mod_sample, mod_mean)
se = sd / math.sqrt(len(sample))

z_dev = (mod_mean - mean) / se

p = 1 - norm.cdf(abs(z_dev))

print("Sample:", sample)
print("Mod Sample (-1):", mod_sample)
print("SE:", round(se, 4))
print("Deviation in Z-scale:", round(z_dev, 4))
print("P-Value:", round(p, 4))

if p < 0.05:
    print("Нулевую гипотезу можно отбросить, так как p-value < 0.05")
else:
    print("Недостаточно оснований отбросить нулевую гипотезу, так как p-value > 0.05")