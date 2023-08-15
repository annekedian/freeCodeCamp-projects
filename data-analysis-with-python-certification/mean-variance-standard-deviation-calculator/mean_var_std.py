import numpy as np

def calculate(list):
  if len(list) != 9 :
    raise ValueError("List must contain nine numbers.")
  else :
    array = np.array(list).reshape(3,3)
    
    #mean
    ma0 = array.mean(axis=0).tolist()
    ma1 = array.mean(axis=1).tolist()
    mf = array.mean()
    
    #variance
    va0 = array.var(axis=0).tolist()
    va1 = array.var(axis=1).tolist()
    vf = array.var()
        
    #std
    stda0 = array.std(axis=0).tolist()
    stda1 = array.std(axis=1).tolist()
    stdf = array.std()
        
    #max
    mxa0 = array.max(axis=0).tolist()
    mxa1 = array.max(axis=1).tolist()
    mxf = array.max()
        
    #min
    mna0 = array.min(axis=0).tolist()
    mna1 = array.min(axis=1).tolist()
    mnf = array.min()
        
    #sum
    sa0 = array.sum(axis=0).tolist()
    sa1 = array.sum(axis=1).tolist()
    sf = array.sum()
        
    calculations = {'mean': [ma0, ma1, mf],
            'variance': [va0, va1, vf],
            'standard deviation': [stda0, stda1, stdf],
            'max': [mxa0, mxa1, mxf],
            'min': [mna0, mna1, mnf],
            'sum': [sa0, sa1, sf]}



    return calculations