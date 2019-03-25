import os

path="/Users/preetam/Desktop/101-classification"
os.chdir(path)
os.system('python classify.py --model 101.model --labelbin mlb.pickle --image examples/img.jpg')