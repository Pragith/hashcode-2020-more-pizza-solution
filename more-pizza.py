#%%
import os

## Functions
def extract_data(file):
    f = open(file, 'r').readlines()
    slices = [int(i) for i in f[1].split(' ')]
    return {
        'max':int(f[0].split(' ')[0]),
        'types':int(f[0].split(' ')[1]),
        'slices':slices,
    }

def generate_combinations(slices, maxSlices):
    result = []
    i = len(slices) - 1
    j = len(slices) - 1
    flag1 = True
    flag2 = True
    score = 0

    while (i >= 0 & flag1):
        tempI = []
        j = i
        Sum = 0
        while (j >= 0 & flag2):
            tempJ = slices[j]
            if (Sum + tempJ) < maxSlices:
                Sum += tempJ
                tempI.append(j)
            elif (Sum + tempJ) == maxSlices:
                Sum += tempJ
                tempI.append(j)
                flag1 = False
                flag2 = False
            j -= 1
        if score < Sum:
            score = Sum
            result = tempI
        if len(result) == len(slices):
            flag1 = False
        i -= 1

    result.reverse()
    return {
        'totalSlices':len(result),
        'result':result
    }

## Execution
for file in os.listdir('input'):
    inputFile = f'input/{file}'
    data = extract_data(inputFile)

    print(f'Processing {inputFile}...')
    output = generate_combinations(data['slices'], data['max'])    
    print(f'Complete!')

    outputFile = open(f'output/{file.split(".")[0]}.out', 'w')
    outputFile.write(f"{len(output['result'])}\n{f' '.join([str(x) for x in output['result']])}")
    outputFile.close()
    
