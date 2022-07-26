import os
os.environ['R_HOME'] = 'D:\\R\\R-4.2.1'
os.environ['R_USER'] = 'D:\\Applications\\Anaconda\\envs\\igem\\Lib\\site-packages\\rpy2' 

import rpy2.robjects as robjects
import  rpy2.robjects.packages as rpackages
from rpy2.robjects.packages import importr

rxnsim = importr('RxnSim')

t = robjects.r['ms.compute']('CCO', 'CO')
print(t[0])