import matplotlib.ticker as ticker
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

% matplotlib notebook

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])


mean_val = df.mean(axis=1).values
# confidence interval, 1.96 comes from the fact we want 95% 
# confidence interval (z* value)
# http://www.dummies.com/education/math/statistics/how-to-
# calculate-a-confidence-interval-for-a-population-mean-when-
# you-know-its-standard-deviation/
confd_val = 1.96 * (std_val / math.sqrt(len(df.columns)))
confd_val

# Easiest option:
# Implement the bar coloring as described above - a color scale with 
# only three colors, (e.g. blue, white, and red). Assume the user 
# provides the y axis value of interest as a parameter or variable.

cutoff = 42500

def colorForBar(mean, cutoff, confidence):
    if (mean - confidence) <= cutoff and (mean + confidence) >= cutoff:
        return "white"
    
    if mean < cutoff:
        return "blue"
    
    if mean > cutoff:
        return "red"

colors=[colorForBar(mean_val[0], cutoff, confd_val[0]),
        colorForBar(mean_val[1], cutoff, confd_val[1]), 
        colorForBar(mean_val[2], cutoff, confd_val[2]), 
        colorForBar(mean_val[3], cutoff, confd_val[3])]

x_ndx=np.arange(len(mean_val))

fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.set_xlim(0,4)
ax1.set_ylim(0,55000)
x_sticks=['1992','1993','1994','1995']

ax1.bar(x_ndx, mean_val,color=colors, tick_label=x_sticks, yerr=confd_val,
       error_kw=dict(ecolor='black', lw=1, capsize=2.5, capthick=2))

majors = [0.5,1.5,2.5, 3.5]
ax1.xaxis.set_major_locator(ticker.FixedLocator(majors))

ax1.axhline(y=cutoff, color='grey', linestyle='--')

#Harder option:
# Implement the bar coloring as described in the paper, where 
# the color of the bar is actually based on the amount of data 
# covered (e.g. a gradient ranging from dark blue for the distribution 
# being certainly below this y-axis, to white if the value is certainly  
# contained, to dark red if the value is certainly not contained as the 
# distribution is above the axis).
 
from matplotlib import cm
from matplotlib.cm import ScalarMappable

# prepare data
mean_val = df.mean(axis=1).values
std_val  = df.std(axis=1).values
confd_val = 1.96 * (std_val / math.sqrt(len(df.columns)))

# fraction of data that is above the cutoff line
def Norm(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


up_bound = mean_val + confd_val
lower_bound = mean_val - confd_val
confd_length = confd_val*2
cutoff = 42500
fraction = (up_bound - cutoff)/confd_length
x_sticks=['1992','1993','1994','1995']


colors = cm.RdBu(fraction)
my_cmap = plt.cm.get_cmap('RdBu')

fig = plt.figure()
ax1 = fig.add_subplot(111)

xxx = ax1.bar(x_ndx,mean_val,color=colors,tick_label=x_sticks, yerr=confd_val,
       error_kw=dict(ecolor='black', lw=1, capsize=2.5, capthick=2))

ax1.axhline(y=cutoff, color='grey', linestyle='--')

ax1.set_xlim(0,4)
ax1.set_ylim(0,55000)

majors = [0.5,1.5,2.5, 3.5]
ax1.xaxis.set_major_locator(ticker.FixedLocator(majors))

sm = ScalarMappable(cmap=my_cmap, norm=plt.Normalize(0,max(fraction)))
sm.set_array([])
plt.colorbar(sm)

