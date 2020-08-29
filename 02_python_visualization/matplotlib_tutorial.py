import matplotlib.pyplot as plt
import numpy as np

# Plot a line Graph

x = np.random.rand(10)
y = x * 2
# 
plt.plot(x,y,x,y,"g>")
plt.title("Title")
plt.xlabel("Xlabel")
plt.ylabel("ylable")
plt.show()
