# Plotting White Noise
# load libraries
import numpy as np
import matplotlib.pyplot as plt

# Version 1
e_values = np.random.randn(100)
plt.plot(e_values)
plt.show()

# Version 2: Using For Loop
ts_length = 100 #set length of time series
e_values = [] #generate empty list
for i in range(ts_length):
    e_values.append(np.random.rand())

plt.plot(e_values)
plt.show()

# Version 3: Using While Loop
ts_length = 100
e_values = []
i = 0
while i < ts_length:
    e_values.append(np.random.rand())
    i += 1

plt.plot(e_values)
plt.show()

# Balance of Bank Account
r = 0.025 #interest rate
T = 50 #end date/period
b = np.empty(T+1) #an empty Numpy array, to store all b_t
b[0] = 10 # initial balance

# Loop for compounding
for t in range(T):
    b[t+1] = (1+r)*b[t]

plt.plot(b, label='Bank Balance')
plt.legend()
plt.show()

# Exercises

# Exercise 3.1
# Plot correlated time series
T = 200
a = 0.9

x = np.empty(T+1)
x[0] = 0
for t in range(T):
    x[t+1] = a*x[t] + np.random.randn()

# plot time series
plt.plot(x)
plt.show()

# Exercise 3.2
# plot three simulated time series to the same figure
x = np.empty(T+1)
alpha = [0, 0.8, 0.98]
for a in alpha:
    for t in range(T):
        x[t+1] = a*x[t] + np.random.randn()
    plt.plot(x, label='alpha = ' + str(a))

# show plot with legend
plt.legend()
plt.show()

# Exercise 3.3
# plot time series
a = 0.9 # set alpha
x = np.empty(T+1)

for t in range(T):
    x[t+1] = a*abs(x[t]) + np.random.randn()

plt.plot(x, label='alpha = ' + str(a))
plt.legend()
plt.show()

# Exercise 3.4 Branching and Conditioning
# re-write 3.3 with conditioning for absolute value
x = np.empty(T+1)
x[0] = 0
for t in range(T):
    if x[t] < 0:
        x[t] = x[t]*-1
    else:
        x[t] = x[t]
    x[t+1] = a*x[t] + np.random.randn()

plt.plot(x, label='alpha = ' + str(a))
plt.legend()
plt.show()

# Monte Carlo simulation to estimate $\\pi$
n = 100000 # sample size for Monte Carlo

count = 0
for i in range(n):

    # drawing random position on the unit square
    u,v = np.random.uniform(), np.random.uniform()

    # check whether the point falls within the boundary of circle
    d = np.sqrt((u - 0.5)**2 + (v - 0.5)**2)

    # if it falls within the inscribed circle add to count
    if d < 0.5:
        count += 1

area_estimate = count / n
print(area_estimate * 4)