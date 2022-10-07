w = 15
profit = [7,2,4]
weight = [5,10,20]

n = len(weight)

def recursion(ind, w, val, wt):
    if ind == 0:
        return (w // wt[0])*val[0]
    
    not_take = 0 + recursion(ind-1, w, val, wt)

    take = 0
    if wt[ind] <= w:
        take = val[ind] + recursion(ind, w - wt[ind], val, wt)
    
    return max(take, not_take)

def unboundedKnapsack(n, w, val, wt):
    return recursion(n-1, w, val, wt)