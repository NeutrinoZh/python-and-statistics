def random_sample(n, a=0, b=9):
    from random import randint
    return [ randint(a, b) for _ in range(n) ]

def sum_samples(a, b):
    if len(a) != len(b):
        raise "len(a) != len(b)"
    return [ a[i] + b[i] for i in range(len(a)) ]

def distribution(sample):
    begin = min(sample)

    freq = [0] * (max(sample) - begin + 1)
    for i in sample:
        freq[i - begin] += 1
    return freq

samples = [
    random_sample(10000) for _ in range(10)
]

sample_sum = [0] * len(samples[0])
for sample in samples:
    sample_sum = sum_samples(sample_sum, sample)

#print("Samples:")
#for sample in samples:
#    print(sample)
#print("="*30)
#print("Sample Sum:")
#print(sample_sum)

from matplotlib import pyplot as plt

#plt.hist(sample_sum)
#plt.stairs(distribution(sample_sum), fill=True)
plt.plot(distribution(sample_sum))
plt.show()