from math import sqrt

def mean(data):
	return sum(data) / len(data)
	
def median(data):
    sdata = sorted(data)
    return sdata[(len(data) - 1) / 2]

def mode(data):
    count = 0
    for i in range(len(data)):
        if data.count(data[i]) > count:
            number = data[i]
            count = data.count(data[i])
    return number

def variance(data):
    ndata = []
    for i in range(len(data)):
        ndata.append((data[i]-mean(data))**2)
    return 1.0 / len(data) * sum(ndata)

####
def variance1(data):
    mu = mean(data)
    return mean([(x-mu)**2 for x in data])

def stddev(data):
    return sqrt(variance(data))

