import numpy as np
import itertools
#print(np.linspace(0,1,10))
#print(np.arange(0,1,0.1))
#probabilities = list(np.round(np.arange(0.1,1.1,0.1),2))
probabilities = [.4,.5,.1]
#accumulated_probabilities = [0.4,0.9,1]
accumulated_probabilities = list(itertools.accumulate(probabilities))
import random

def sampling(probs):
    r = random.random()
    for prob in probs:
        if r <= prob:
            return(prob)

def count_samples(probs, acc_probs, trials = 10000):        
    dic_sampled =  {label: 0 for label in probs}
    keys = list(dic_sampled.keys())
    for trial in range(trials):
        sample = sampling(acc_probs)
        sample_index = acc_probs.index(sample)
        sample_label = keys[sample_index]
        #print(sample, sample_index, sample_label, keys[sample_index])
        dic_sampled[sample_label] += 1
    dic_sampled_probs = {key: value / trials for key, value in dic_sampled.items()}
    return(dic_sampled_probs)

print(count_samples(probs=probabilities, acc_probs=accumulated_probabilities))