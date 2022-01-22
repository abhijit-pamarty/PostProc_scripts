import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
inpath = "C:\\Users\\abhij\\OneDrive\\Desktop\\Personal folder\\Academics\\Internships\\Harvard internship\\Files\\Case data files\\\inlet as obstruction\\Combined files\\Excel Files"
outpath = "C:\\Users\\abhij\\OneDrive\\Desktop\\boundary_layers.xlsx"
dirs = os.listdir(inpath)
d = 0
listdfs = []
while d in range(len(dirs)):
    if (dirs[d].find("ms") == -1):
        del(dirs[d])
    d += 1
for direc in dirs:
    excelpath = inpath + "\\" + direc
    dfs = pd.read_excel(excelpath, None)
    
    for sheet in dfs:
        
        arr = dfs[sheet][[0,1]].dropna()
        arr = arr.iloc[1: , :]
        narr = pd.DataFrame.to_numpy(arr)
        narr = narr.astype(float)
        narr[:,0] = np.abs(narr[:,0])
        max_vel = max(narr[:,0])
        top_limit = max(narr[:,1])
        bot_limit = min(narr[:,1])
        top_line = np.array([[top_limit,0]])
        bot_line = np.array([[bot_limit,0]])
        i = 0
        while i < max_vel:
            top_line = np.append(top_line, np.array([[top_limit, i*1.5]]), axis = 0)
            bot_line = np.append(bot_line, np.array([[bot_limit, i*1.5]]), axis = 0)
            i += 1
        print(top_line)
        plt.title(direc.replace(".xlsx",":")  +  sheet.replace("-"," "))
        plt.plot(top_line[:,1],top_line[:,0], color = 'black')
        plt.plot(bot_line[:,1],bot_line[:,0], color = 'black')
        plt.plot(narr[:,0],narr[:,1], color = 'blue')
        plt.xlim(0,(int(direc.replace("ms.xlsx",""))*5))
        plt.show()
        
