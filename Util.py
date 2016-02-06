import numpy as np

def softmax(x):
  """ Compute softmax values for each sets of scores in x """
  if (len(x) < 1):
    return x

  exp = np.exp(x);
  sum_exp = np.sum(exp, axis=1);
  prob = [[exp_i / sum_exp for exp_i in exp_j] for exp_j in exp]

  return prob  
     
