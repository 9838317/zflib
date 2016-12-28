def minMeanMax (argArray):
    meanArray = 1.0 * sum(argArray)/len(argArray);
    maxArray  = max(argArray)
    minArray  = min(argArray)
    return (minArray, meanArray, maxArray)

def var(argArray):
    meanArray = minMeanMax(argArray)[1]
    sumArray  = 0.0
    for i in argArray:
        sumArray += (i - meanArray)**2
    sumArray *= 1.0
    return (sumArray/len(argArray), sumArray)
    
def std(argArray):
    return (var(argArray)[0])**0.5

