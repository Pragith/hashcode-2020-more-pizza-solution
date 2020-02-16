#%%
import os
import itertools
from collections import defaultdict

## Functions
def extract_data(file):
    f = open(file, 'r').readlines()
    slices = [int(i) for i in f[1].split(' ')]
    return {
        'max':int(f[0].split(' ')[0]),
        'types':int(f[0].split(' ')[1]),
        'slices':slices,
    }

def find_pos(arr, vals):
    result = []
    for val in vals:
        result.append(arr.index(val))
    return result

def generate_combinations(slices, maxSlices):
    result = []
    for l in range(2,len(slices)+1):
        totalSlices = list(itertools.combinations(slices, l))
        totalTypes = list(map(sum, totalSlices))
        combos = { totalTypes[i]:totalSlices[i] for i in range(len(totalTypes)) }
        
        for types in combos.keys():
            if types <= maxSlices:                
                result.append({
                    'types':types,
                    'combo':combos[types],
                    'slices':slices,
                    'result':find_pos(slices, combos[types])
                })

    return result[-1]

## Execution
for file in os.listdir('input'):
    inputFile = f'input/{file}'
    data = extract_data(inputFile)
    slices = 0

    output = generate_combinations(data['slices'], data['max'])

    print(f'Input: {data}')
    print(f"Output: {output}")

    outputFile = open(f'output/{file.split(".")[0]}.out', 'w')
    outputFile.write(f"{len(output['result'])}\n{f' '.join([str(x) for x in output['result']])}")
    outputFile.close()
    


# %%