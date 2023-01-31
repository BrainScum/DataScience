import numpy as np

values = """32.92
29.25
33.76
30.29
27.93
29.03
41.41
38.03
31.50
29.22
42.47
31.34
26.09
27.13
43.28
42.89
32.11
37.37
44.10
29.31
36.57
38.74
35.78
37.02
28.40"""

values = values.split()
values = list(map(lambda val: float(val), values))
#print(values)

thing = np.histogram(values, bins = 6, density=False)
#print(thing)

def freq(arr):
    freqs = {"25 - 28": 0, "28 - 31": 0, "31 - 34": 0, "34 - 37": 0, "37 - 41": 0, "41 - 43": 0, "43 - 46": 0,}

    for val in arr: 
        if val >= 25 and val < 28:
            freqs["25 - 28"] += 1
        else: 
            if val >= 28 and val < 31:
                freqs["28 - 31"] += 1
            else: 
                if val >= 31 and val < 34:
                    freqs["31 - 34"] += 1
                else: 
                    if val >= 34 and val < 37:
                        freqs["34 - 37"] += 1
                    else: 
                        if val >= 37 and val < 41:
                            freqs["37 - 41"] += 1
                        else: 
                            if val >= 41 and val < 43:
                                freqs["41 - 43"] += 1
                            else: 
                                freqs["43 - 46"] += 1
    
    relFreqs = []
    for val in freqs.values():
        relFreqs.append(val/len(values))

    return [freqs, relFreqs]

print(freq(values))