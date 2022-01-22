import pandas as pd
import numpy as np
import os
inpath = "C:\\Users\\abhij\\OneDrive\\Desktop\\Personal folder\\Academics\\Internships\\Harvard internship\\Files\\Case data files\\inlet as obstruction\\Combined files\\Excel Files"
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
    
    BLdf = pd.DataFrame({'Title' :[], 'Maximum boundary layer': [], 'Average Boundary Layer': []})
    
    for sheet in dfs:
        
        arr = dfs[sheet][[0,1]].dropna()
        arr = arr.iloc[1: , :]
        narr = pd.DataFrame.to_numpy(arr)
        narr = narr.astype(np.float)
        narr[:,0] = np.abs(narr[:,0])
        print("currently processing : ", direc, "\\", sheet)
        max_vel = np.max(narr, 0)[0]
        lower_cutoff_vel = 0.985*max_vel
        upper_cutoff_vel = max_vel
        
        i = 0
        top_index = None
        flag = 0
        while i in range(len(narr[:,0])):
            if narr[i , 0] > lower_cutoff_vel and narr[i , 0] < upper_cutoff_vel:
                top_index = i
                flag = 1
            i += 1
            if(flag):
                break
        
        i = len(narr[:,0]) - 1
        bottom_index = None
        flag = 0
        while i >= 0:
            if narr[i , 0] > lower_cutoff_vel and narr[i , 0] < upper_cutoff_vel:
                bottom_index = i
                flag = 1
            i -= 1
            if(flag):
                break
            
        topbl = abs(narr[0,1] - narr[top_index,1])
        bottombl = abs(narr[(len(narr)-1),1] - narr[bottom_index,1])
        len_pipe = abs(narr[0,1] - narr[(len(narr)-1),1])
        topBLT = 100*topbl/len_pipe
        botBLT = 100*bottombl/len_pipe
        average_BLT = (topBLT + botBLT)/2
        max_BLT = max([topBLT, botBLT])
        subdf = pd.DataFrame({'Title' :[sheet], 'Maximum boundary layer': [max_BLT], 'Average Boundary Layer': [average_BLT]})
        BLdf = BLdf.append(subdf, ignore_index = True)
    listdfs.append([BLdf,direc])
writer = pd.ExcelWriter(outpath, engine='xlsxwriter')
for thing in listdfs:
    thing[0].to_excel(writer, sheet_name=thing[1])
writer.save()
writer.close()
writer.handles = None

    
        
         