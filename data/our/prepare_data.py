import shutil
import numpy as np
import os
import pandas as pd
import tqdm
import pickle

if __name__ == "__main__":
    excelfile = pd.read_excel("数据.xlsx")
    excel_data = excelfile.values
    txt_name = "images.txt"
    img_root_dir = "./images/"
    img_path = "./CUB_200_2011/images/"
    txt_root_dir = "./text/"
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    if not os.path.exists(txt_root_dir):
        os.makedirs(txt_root_dir)
    if not os.path.exists("./train"):
        os.makedirs("./train")
    
    id = 1
    txt_file = open("./CUB_200_2011/"+txt_name,"w")
    for line in excel_data:
        if(type(line[1])==str and type(line[2])==str):
            label_name = line[0].split('.')[0] + ".txt"
            label_file = open(txt_root_dir+label_name,"w")
            
            label_file.write(line[1]+"\n")
            label_file.write(line[2]+"\n")

            label_file.close()
            
            shutil.copy(img_root_dir+line[0],img_path+line[0])
            txt_file.write(str(id)+" "+line[0]+"\n")
            id += 1
            print(id)
        
    txt_file.close()

    for root,dir,files in os.walk("./text/"):
        data = files
        for i in range(len(data)):
            data[i] = data[i].split('.')[0]
        path = "./train/filenames.pickle"
        output = open(path, 'wb')
        pickle.dump(data, output)
        output.close()
