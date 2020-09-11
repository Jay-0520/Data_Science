import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax = fig.add_subplot(111)

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

bars = ax.bar(pos, popularity, align='center',linewidth=0, color='lightslategrey')
bars[0].set_color('#1F77B4')

ax.set_title("Top 5 Languages for Math")
ax.set_ylabel("% Popularity")

ax.set_xticks(np.arange(0,5))
ax.set_xticklabels(languages)

ax.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')

for spine in ax.spines.values():
    spine.set_visible(False)
    
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, 
                   bar.get_height() - 5, 
                   str(int(bar.get_height())) + '%', 
                 ha='center', color='w', fontsize=11)

