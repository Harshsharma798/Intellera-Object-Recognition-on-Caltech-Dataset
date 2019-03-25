import os

path="/Users/preetam/Desktop/101-classification"
os.chdir(path)
os.system('python classify.py --model fashion.model --labelbin mlb.pickle --image examples/img.jpg')