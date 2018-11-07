#!/opt/local/bin/python
from __future__ import absolute_import
import numpy as np
import help_functions as hlp
import matplotlib.pyplot as plt
import re
from sys import argv

fig, ax = plt.subplots()
list_of_logs = [vals for vals in argv[1:]]

#c = ['r','g','b','c','m','y','k','w']
#legend = ["Flex Anneal","Flex Quench","Rigid Anneal","Rigid Quench"]
legend = ["Anneal","Quench"]
#legend = ["Rigid Quench"]

#legend = ["Flex Quench", "Rigid Quench"]
#legend = ["Flex Anneal", "Rigid Anneal"]

#legend =["Last Frame", "2nd Last Frame"]
for i, log in enumerate(list_of_logs):
    log_data = hlp.get_data_with_headers(log)  # Need to change it so I just load in the first line
    #log_data_headers = log_data.dtype.names

    log_data = hlp.get_data(log)
    #if i == 0 or i == 1:
    #    y = log_data[:, 1]*4184*(0.25)+0.5e8
    #    y_err = log_data[:, 2]*4184*(0.25)+0.5e8
    #else:
    #    y = log_data[:, 1]*4184*(0.25)
    #    y_err = log_data[:, 2]*4184*(0.25)
    y = log_data[:, 1]*4184*(0.25)
    y_err = log_data[:, 2]*4184*(0.25)#/np.sqrt(log_data[:,3])

    x = log_data[:, 0]*125.867#*0.87#*125.867#/0.87#/(2*np.pi)#*125.867

    ax.errorbar(x,y,yerr=y_err,label=legend[i], marker = 'o', markeredgewidth=0, markersize=8)
    #plt.plot(x,y, marker='o', label=legend[i])
    #print(legend[i])
    #for _ in y:
    #    print(_)
#ax.set_ylim(0,1)
#ax.set_ylim(-2.00,-1.60)
#ax.set_xlim(200, 1000)
plt.rcParams.update({'mathtext.default':  'regular' })
plt.xlabel(r"Temperature (K)")
#plt.ylabel("% Of Chains In Cluster")
#plt.ylabel(r"First Peak Height Intensity")
#plt.ylabel("TPS")
#plt.ylabel(r"E$_{LJ}$ (J/mol)")
plt.ylabel(r"E$_{LJ}$ $\Delta$ (J/mol)")
#plt.ylabel("My SD")
#plt.axhline(y=1e5, xmin=0, xmax=9.5*125.867, hold=None)
#plt.axhline(y=1e6, xmin=0, xmax=9.5*125.867, hold=None)
#plt.yscale('log', nonposy='clip')
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0), useMathText=True)
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)
#ax.xaxis.major.formatter._useMathText = True
ax.yaxis.major.formatter._useMathText = True
legend = ax.legend(loc='best', shadow=False, prop={'size':20})
plt.savefig("deltaE_error.pdf")
#plt.show()
