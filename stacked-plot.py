#!/usr/bin/env python3

import numpy as np
import matplotlib
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

FIGSIZE = (8, 5)


x = [datetime.date(2012,1,1), datetime.date(2013,1,1), datetime.date(2014,1,1), datetime.date(2015,1,1),datetime.date(2016,1,1)]

y1 = [1, 1, 2, 3, 5]
y2 = [0, 4, 2, 6, 8]
y3 = [1, 3, 5, 7, 9]

y = np.vstack([y1, y2, y3])

labels = ["Fibonacci ", "Evens", "Odds"]

fig, ax = plt.subplots(figsize=FIGSIZE, dpi=300)
fig.tight_layout()

ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax.tick_params(top=False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
#ax.tick_params(bottom="off", left="off", top='off')
ax.tick_params(left="off")

ax.get_yaxis().set_visible(False)

date_fmt = DateFormatter("%Y")
ax.xaxis.set_major_formatter(date_fmt)
fig.autofmt_xdate()

CB91_Blue = '#2CBDFE'
CB91_Green = '#47DBCD'
CB91_Pink = '#F3A0F2'
CB91_Purple = '#9D2EC5'
CB91_Violet = '#661D98'
CB91_Amber = '#F5B14C'

color_list = [CB91_Blue, CB91_Pink, CB91_Green, CB91_Amber,
              CB91_Purple, CB91_Violet]

vibrant = ('#ee7733',  '#cc3311', '#0077bb', '#009988', '#33bbee',  '#ee3377', '#bbbbbb')
light = ('#77AADD', '#EE8866', '#EEDD88', '#FFAABB', '#99DDFF', '#44BB99', '#BBCC33', '#AAAA00', '#DDDDDD', '#000000')
baseline = 'wiggle'
ax.stackplot(x, y1, y2, y3, baseline=baseline, labels=labels, colors=light)
ax.legend(loc='upper left')

filename = "stack-plot.png"
plt.savefig(filename, transparent=False)
