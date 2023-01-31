import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter

values = """143 227 152 147 212 148 143 188 153 142
158 125 236 109 157 131 227 66 274 96
114 173 217 205 182 137 195 138 135 158
138 119 133 144 230 123 171 133 41 132
140 194 164 116 388 425 333 493 196 176"""

values = values.split()
values = list(map(lambda val: int(val), values))

def freq(arr):
    freqs = {"0 - 49": 0, "50 - 99": 0, "100 - 149": 0, "150 - 199": 0, "200 - 249": 0, "250 - 299": 0, "300 - 349": 0, "350 - 399": 0,
     "400 - 449": 0, "450 - 499": 0}

    for val in arr: 
        if val >= 0 and val <= 49:
            freqs["0 - 49"] += 1
        else: 
            if val >= 50 and val <= 99:
                freqs["50 - 99"] += 1
            else: 
                if val >= 100 and val <= 149:
                    freqs["100 - 149"] += 1
                else: 
                    if val >= 150 and val <= 199:
                        freqs["150 - 199"] += 1
                    else: 
                        if val >= 200 and val <= 249:
                            freqs["200 - 249"] += 1
                        else: 
                            if val >= 250 and val <= 299:
                                freqs["250 - 299"] += 1
                            else: 
                                if val >= 300 and val <= 349:
                                    freqs["300 - 349"] += 1
                                else: 
                                    if val >= 350 and val <= 399:
                                        freqs["350 - 399"] += 1
                                    else: 
                                        if val >= 400 and val <= 449:
                                            freqs["400 - 449"] += 1
                                        else:
                                            freqs["450 - 499"] += 1
    
    relFreqs = []
    for val in freqs.values():
        relFreqs.append(val/len(values))

    return [freqs, relFreqs]


values = np.array(values)
print(freq(values))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(values, edgecolor="black")
plt.show()



"""plt.hist(values, density=True, bins=30)  # density=False would make counts
plt.ylabel('Probability')
plt.xlabel('Data')
plt.show()"""