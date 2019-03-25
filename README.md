# Intellera-Object-Recognition-on-Caltech-Dataset
Intellera is an object recognition software based on python and Machine Learning techniques and can be used for any multi-class classification

Put your dataset to be trained into dataset folder

Run the command given below:
python train.py --dataset dataset --model 101.model --labelbin mlb.pickle
  
It would take a lot much of time so make sure that your system is connected to power source and does not go for sleep.

Once the model is trained, put the image to be tested in examples folder

Run following command for testing the model:
python classify.py --model 101.model --labelbin mlb.pickle --image examples/xyz.jpg

Replace xyz.jpg with your image name
