import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats

# Use the following data for this assignment:
np.random.seed(12345)

n = 3650

df = pd.DataFrame([np.random.normal(32000, 200000, n),
                   np.random.normal(43000, 100000, n),
                   np.random.normal(43500, 140000, n),
                   np.random.normal(48000, 70000, n)],
                  index=[1992, 1993, 1994, 1995])

df

# Create a dataset with the mean, std, and confidence intervals
df_new = pd.concat([df.mean(axis=1), df.std(axis=1) / np.sqrt(n)], axis=1)
df_new.columns = ['mean', 'std']
df_new['lcb'] = df_new['mean'] - 1.96 * df_new['std']
df_new['ucb'] = df_new['mean'] + 1.96 * df_new['std']
df_new.head()

# Set up some inputs for later
N = 4
ind = np.arange(4)  # the x locations for the groups
width = 0.9  # the width of the bars

# Let's start by creating a figure:
fig, ax = plt.subplots()
fig.set_size_inches(8, 6, forward=True)

# Temporarily create a scatter plot so we can use the color bar
cmap = matplotlib.cm.get_cmap('RdBu')
y = np.array([0, .5, 1])
plot = plt.scatter(y, y, c=y, cmap='RdBu')
ax.cla()
cbar = fig.colorbar(plot, ticks=[0, 0.025, .5, .975, 1])
cbar.ax.set_yticklabels(['1', '0.95', '0', '-0.95', '-1'])

# Create our base bar chart
bars = ax.bar(ind, df_new['mean'], width, color=[cmap(.5), cmap(.5), cmap(.5), cmap(.5)], yerr=df_new['std'])

# Add proper titles and axes
ax.set_ylabel('Estimate of the Mean', fontsize=12)
ax.set_title('Has the Mean Changed over the Years?', fontsize=12, weight='bold')
ax.set_xticks(np.arange(len(bars)))
ax.set_xticklabels(('1992', '1993', '1994', '1995'), fontsize=12)
ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))


def recolor_bars(x):
    # Create a standard t-statistic by normalizing the x value (subtracting the mean and dividing by the std dev)
    t = (df_new['mean'] - x) / df_new['std']
    # Calculate the likelihood that the mean is equal to the input (1 - p-value)
    probabilities = 1 - stats.t.pdf(x=t, df=n - 1)
    # Add a sign to these probabilities (probability above or below)
    probabilities = -1 * np.sign(df_new['mean'] - x) * probabilities
    # Normalize around 0.5 for the color map
    probabilities = 0.5 + (probabilities / 2)
    # Get colors for the color map
    cmap = matplotlib.cm.get_cmap('RdBu')
    colors = cmap(probabilities)
    bars = ax.bar(ind, df_new['mean'], width, color=colors, yerr=df_new['std'])


recolor_bars(40000)


def onclick(event):
    print(event.y)
    recolor_bars(event.ydata)


# tell mpl_connect we want to pass a 'button_press_event' into onclick when the event is detected
plt.gcf().canvas.mpl_connect('button_press_event', onclick)
