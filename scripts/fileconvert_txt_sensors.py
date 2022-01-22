import pandas as pd

import os
inpath = "C:\\Users\\abhij\\OneDrive\\Desktop\\Personal folder\\Academics\\Internships\\Harvard internship\\Files\\Case data files\\inlet as obstruction\\turbulent kinetic energy"
outpath= "C:\\Users\\abhij\\OneDrive\\Desktop\\"
dirs = os.listdir(inpath)
string = "xy/key/label"
d = 0
while d in range(len(dirs)):
    if (dirs[d].find("sensor") == -1):
        del(dirs[d])
    d += 1
for i in dirs:
    current = inpath + "\\" + i 
    listdfs = []
    indirs = os.listdir(current)
    for j in indirs:
        f = open(current +"\\" + j , "r")
        k = f.readlines()
        print(k)
        title = j.replace("ms.dat","")
        
        data = k[5:-2]
        for d in range(len(data)):
            data[d] = data[d].replace("\n","")
            data[d] = data[d].replace("\t",",")
            data[d] = data[d].split(',')
        title = title.replace('"',"")
        data.insert(0,["title", title])
        df = pd.DataFrame(data)
        listdfs.append(df)
        print(listdfs)
        print("listdfs printed")
    filename = i + '.xlsx'
    with pd.ExcelWriter(outpath + filename) as writer:
        for dataframe in listdfs:
            print(dataframe[1][0])
            dataframe.to_excel(writer,dataframe[1][0])
        writer.save()
       
       
        

            
    
    
