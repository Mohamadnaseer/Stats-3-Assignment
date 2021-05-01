#!/usr/bin/env python
# coding: utf-8

# # Stats 3 Assignment

# # Problem Statement 1:
# Blood glucose levels for obese patients have a mean of 100 with a standard deviation of
# 15. A researcher thinks that a diet high in raw cornstarch will have a positive effect on
# blood glucose levels. A sample of 36 patients who have tried the raw cornstarch diet
# have a mean glucose level of 108. Test the hypothesis that the raw cornstarch had an
# effect or not.

# In[3]:


import scipy.stats as sts
from scipy.stats import norm
import math
import numpy as np
p_mean = 100
p_std = 15
n = 36
sample_mean = 108
alpha = 0.05
SE = p_std/n**0.5
print(f"SE: {SE}")
Z = (sample_mean-p_mean)/SE
print(f"Z_score: {Z}")


# # Problem Statement 2:
# In one state, 52% of the voters are Republicans, and 48% are Democrats. In a second
# state, 47% of the voters are Republicans, and 53% are Democrats. Suppose a simple
# random sample of 100 voters are surveyed from each state.
# What is the probability that the survey will show a greater percentage of Republican
# voters in the second state than in the first state?

# In[7]:


n1 = 100
n2 = 100
R1 = 0.52            
D1 = 0.48          
R2 = 0.47            
D2 = 0.53 
x = 0
mu = R1 - R2
print(f"mu: {mu}")
std = math.sqrt(((R1 * D1 ) / n1) + ((R2 * D2) /n2))
print(f"std: {std}")
Z_R1_R2 = ( x - mu)/std
print(f"Z_p1_p2 : {Z_R1_R2}")


# # Problem Statement 3:
# You take the SAT and score 1100. The mean score for the SAT is 1026 and the standard
# deviation is 209. How well did you score on the test compared to the average test taker?

# In[8]:


x = 1100 
mu = 1026 
sd = 209
z = ( x - mu)/sd
print("Z Score : ",z)
print("My Score is in the range {} - {}  with a  zscore {:.2f}".format(mu - sd,mu + sd,z))

