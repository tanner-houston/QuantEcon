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