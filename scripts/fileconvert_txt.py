import pandas as pd

import os
inpath = "C:\\Users\\abhij\\OneDrive\\Desktop\\Personal folder\\Academics\\Internships\\Harvard internship\\Files\\Case data files\\injector full\\XY plots\\turbulent kinetic energy"
outpath= "C:\\Users\\abhij\\OneDrive\\Desktop\\"
dirs = os.listdir(inpath)
string = "xy/key/label"
for i in dirs:
    current = inpath 
    listdfs = []
    indirs = os.listdir(current)
    for j in indirs:
        f = open(current +"\\" + j , "r")
        k = f.readlines()
        print(k)
        title = k[1].replace("Series 1 at /LINE:","")
        
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
       
       
        

            
    
    
