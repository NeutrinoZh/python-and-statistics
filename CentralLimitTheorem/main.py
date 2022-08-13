import math
from pytools import average

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

def limitTheorem(num):
    samples = [
        random_sample(num) for _ in range(100)
    ]

    sample_sum = [0] * len(samples[0])
    for sample in samples:
        sample_sum = sum_samples(sample_sum, sample)

    return distribution(sample_sum)

def testOne():
    from matplotlib import pyplot as plt

    fig, axs = plt.subplots(5, 5)
    plt.subplots_adjust(hspace=3)

    for i in range(5):
        for j in range(5):
            num = 100 * (i * 5 + j + 1)
            axs[i][j].set_title(num)
            axs[i][j].plot(limitTheorem(num))

    plt.show()

def testTwo():
    samples = [
        random_sample(100) for _ in range(1000)
    ]
    
    average_sample = [ average(sample) for sample in samples]  

    mean = average(average_sample)
    SE = math.sqrt(sum([(mean - n)**2 for n in average_sample]) / (len(average_sample) - 1))

    print("mean average sample:", mean)
    print("SE:" , SE)

testTwo()
testOne()