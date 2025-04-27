#Weekly Task 08
#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2 
#a plot of the function  h(x)=x**3 in the range 0 to 10


import numpy as np
import matplotlib.pyplot as plt

#x and y points for the plot
x = np.linspace(0, 10, 1000)
h = x**3

#Data for the histogram
data = np.random.normal(loc=5, scale=2, size=1000)

#larger figure size
plt.figure(figsize=(10,6))

#plotting h(x)=x**3
plt.plot(x, h, color="maroon", label = "h(x)=x^3")

#plotting the histogram
plt.hist(data, bins=15, alpha=0.6, color="royalblue", label = "Normal Distribution (mean=5, std=2)")

#Labels, titles, and legend
plt.title("Weekly Task 08")
plt.xlabel("x")
plt.ylabel("h(x)")
plt.legend()

#displaying the plot
plt.show()