import pickle
path = "./train/filenames.pickle"   
with open(path , "rb") as fh:
    data = pickle.load(fh)
    print(data)