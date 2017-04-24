# BAYES RULE

# p0 --> vjerojatnost bolesti
# p1 --> sensitivity
# p2 --> specificity

### Positive Test
def PosTest(p0,p1,p2):
    return p0*p1 / (p0*p1 + (1-p0) * (1-p2))


### Negative Test
def NegTest(p0,p1,p2):
    return p0 * (1-p1) / (p0 * (1-p1) + (1-p0) * p2)