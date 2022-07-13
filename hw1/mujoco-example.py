import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# This is just a dummy function to generate some arbitrary data
def get_data():
    base_cond = [[18, 20, 19, 18, 13, 4, 1], [20, 17, 12, 9, 3, 0, 0],
                 [20, 20, 20, 12, 5, 3, 0]]
    cond1 = [[18, 19, 18, 19, 20, 15, 14], [19, 20, 18, 16, 20, 15, 9],
             [19, 20, 20, 20, 17, 10, 0],
             [20, 20, 20, 20, 7, 9, 1]]
    cond2 = [[20, 20, 20, 20, 19, 17, 4], [20, 20, 20, 20, 20, 19, 7], [19, 20, 20, 19, 19, 15, 2]]
    cond3 = [[20, 20, 20, 20, 19, 17, 12], [18, 20, 19, 18, 13, 4, 1], [20, 19, 18, 17, 13, 2, 0], [19, 18, 20, 20, 15, 6,
                                                                                               0]]
    return base_cond, cond1, cond2, cond3


# Load the data .
results = get_data()
fig = plt.figure()
# We will plot iterations 0 ... 6
xdata = np.array([0, 1, 2, 3, 4, 5, 6]) / 5.
# Plot each line
# (may want to automate this part e.g. with a loop).
sns.tsplot(time=xdata, data=results[0], color='r', linestyle='-')
sns.tsplot(time=xdata, data=results[1], color='g', linestyle='--')
sns.tsplot(time=xdata, data=results[2], color='b', linestyle=':')
sns.tsplot(time=xdata, data=results[3], color='k', linestyle='-.')
# Our y−axis is ”success rate” here.
plt.ylabel("Success Rate", fontsize=25)
# Our x−axis is iteration number.
plt.xlabel("Iteration Number", fontsize=25, labelpad=4)
# Our task is called ”Awesome Robot Performance”
plt.title("Awesome Robot Performance", fontsize=30)
# Legend.
plt.legend(loc='lower left')
# Show the plot on the screen .
plt.show()
