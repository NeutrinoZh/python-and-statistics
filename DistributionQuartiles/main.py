numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sort_numbers = sorted(numbers)

def get_i(i):
    if i == int(i):
        i = int(i)
        return (sort_numbers[i - 1] + sort_numbers[i]) / 2
    else:
        return sort_numbers[int(i)]



median = get_i(len(sort_numbers) / 2)
kv1 = get_i(len(sort_numbers) / 4)
kv2 = get_i(len(sort_numbers) / 2 + len(sort_numbers) / 4)

print("median:", median)
print("kv1:", kv1)
print("kv2:", kv2)