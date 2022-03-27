import pandas as pd
import numpy as np
import os
inpath = r"C:\Users\abhij\OneDrive\Desktop\Personal folder\Academics\Internships\Harvard internship\Files\Case data files\injector full\Combined files\Combined new"
outpath = "C:\\Users\\abhij\\OneDrive\\Desktop\\TKE.xlsx"
dirs = os.listdir(inpath)
d = 0
listdfs = []
while d in range(len(dirs)):
    if (dirs[d].find("Sensor") == -1):
        del(dirs[d])
    d += 1
for direc in dirs:
    excelpath = inpath + "\\" + direc
    dfs = pd.read_excel(excelpath, None)
    
    BLdf = pd.DataFrame({'Title' :[], 'Maximum turbulent KE': [], 'Average turbulent KE': []})
    
    for sheet in dfs:
        
        arr = dfs[sheet][[0,1]].dropna(0)
        arr = arr.iloc[1: , :]
        narr = pd.DataFrame.to_numpy(arr)
        narr = narr.astype(np.float)
        narr[:,1] = np.abs(narr[:,1])
        print("currently processing : ", direc, "\\", sheet)
        max_TKE = np.max(narr, 0)[1]
        av_TKE = np.average(narr, 0)[1]
        min_TKE = np.min(narr, 0)[1]
        
        subdf = pd.DataFrame({'Title' :[sheet], 'Maximum turbulent KE': [max_TKE], 'Minimum turbulent KE': [min_TKE], 'Average turbulent KE': [av_TKE]})
        BLdf = BLdf.append(subdf, ignore_index = True)
    listdfs.append([BLdf,direc])
writer = pd.ExcelWriter(outpath, engine='xlsxwriter')
for thing in listdfs:
    thing[0].to_excel(writer, sheet_name=thing[1])
writer.save()
writer.close()
writer.handles = None

    
        
         