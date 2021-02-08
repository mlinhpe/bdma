import math
# s = []
# e = ?
s = ['A', 'B', 'C', 'C', 'A', 'C', 'B', 'A', 'C', 'C', 'A', 'C']
epsilon = 0.25
w = 1/epsilon
n = 0
freq = {}
delta = {}
lookup = {}

for item in s:
    freq[item] = 0
    delta[item] = 0


for item in s:
    n += 1
    bcurr = math.ceil(n/w)
    freq[item] += 1
    lookup[item] = [freq[item], delta[item]]
    if n % w == 0:
        temp_lookup = lookup
        lookup = {}
        for entry in temp_lookup:
            if temp_lookup[entry][0] + temp_lookup[entry][1] > bcurr:
                lookup[entry] = temp_lookup[entry]
            else:
                delta[entry] += 1
                freq[entry] = 0

print(lookup)


