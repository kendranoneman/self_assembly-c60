from sys import argv
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
 
data = loadtxt(argv[1])

#To skip a row: elimnates the name row.
data = loadtxt(argv[1], skiprows = 1)

#Splitting up the data:
timesteps = data[:,0]
potential = data[:,1]

#Doing the Graph
plt.plot(timesteps,potential)
plt.ylabel('Average Potential Energy')
plt.xlabel('Timestep')
plt.title('Potential Energy over Time')
#set up plot option
print "Would you to save the figure?"
print "Yes or No? (y or n)"
option = raw_input("> ")
if option == 'y': 
    plt.savefig('potential.png')
if option == 'n':
    plt.show()
