#Write a function sim_probability(num_heads, num_flips) that uses Monte Carlo simulation to compute the probability 
# of getting a given number of heads in a given number of flips of a fair coin.

#First, simulate a large number of trials (say, 1000). In each trial, flip a coin num_flips times and count how many 
# heads appear. You may import a random number generator for this.
#Then, count the number of trials in which exactly num_heads heads appeared and divide it by the total number of trials (1000).
#To test your implementation, work out the result by hand for several combinations of num_heads and num_flips, and verify 
# that your function consistently returns results that are close to these true values.
import random

def coin_flip(head_prob=0.5):
    score = random.random()
    if score < head_prob:
        return('heads')
    else:
        return('tails')

def sim_flips(num_flips=1000):
    heads_count = 0
    tails_count = 0
    for flip in range(num_flips):
        result = coin_flip()
        if result == 'heads':
            heads_count += 1
        else:
            tails_count += 1
    
    return(heads_count, tails_count)


#probabilidad de que salga justo ese numero de caras:

def sim_probability(num_heads=500, num_trials = 1000, **kwargs):
    num_heads_count = 0
    for trial in range(num_trials):
        heads_count, tails_count = sim_flips(**kwargs)
        if heads_count == num_heads:
            num_heads_count += 1

    prob_num_heads = num_heads_count / num_trials
    print(prob_num_heads)


#probabilidad de un intervalo, potencialmente un solo valor si tomamos un intervalo de comienzo y fin iguales
def bin_simulated_probablity(num_heads_range=[400,500], num_trials = 10000, **kwargs):
    num_heads_in_range_count = 0
    for trial in range(num_trials):
        heads_count, tails_count = sim_flips(**kwargs)
        lower_limit = num_heads_range[0]
        upper_limit = num_heads_range[1]
        if ((heads_count >= lower_limit) and (heads_count <= upper_limit)):
            #print(num_heads_range)
            num_heads_in_range_count += 1

    prob_num_heads_in_range = num_heads_in_range_count / num_trials
    return(prob_num_heads_in_range)    


#bin_simulated_probablity()
#bin_simulated_probablity(num_heads_range=[4000,5000], num_flips = 10000)


bin_distribution = []
bin_labels = []
num_of_bins = 10
for i in range(num_of_bins):
    factor = 10
    lower_lim = i*factor
    upper_lim = (i+1)*factor
    bin_prob = bin_simulated_probablity(num_heads_range=[lower_lim,upper_lim], num_flips = 10*factor)
    bin_labels.append(f"[{lower_lim},{upper_lim}]")
    bin_distribution.append(bin_prob)
print(bin_distribution)
#bin_simulated_probablity(num_flips=1000)

import seaborn as sns
import matplotlib.pyplot as plt

# Create the histogram
sns.barplot(x = bin_labels , y = bin_distribution)

# Show the plot
plt.show()

    

