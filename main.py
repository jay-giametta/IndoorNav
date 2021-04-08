import buildObs as bo
import cleanObs as co
import pandas as pd
import random as rnd

from os import listdir
from os import remove
from os.path import isfile

path = "data/train"

for file in listdir(path):

    for floor in listdir(path + "/" + file):

        folder = listdir(path + "/" + file + "/" + floor)

        #take a random sampling of five files from each folder
        for i in rnd.sample(range(0, len(folder)), 5):

            fileName = folder[i]

            if "txt" in fileName:

                fullName = path + "/" + file + "/" + floor + "/" + fileName
                newName = (path + "/_processed/" + fileName).replace("txt","csv")

                print("Processing " + fullName + ":")
                print("Building observations...")
                dFrame = pd.DataFrame(bo.buildObs(fullName, floor))

                print("Cleaning observations...")
                dFrame = pd.DataFrame(co.cleanObs(dFrame))

                print("Writing " + newName + "...")
                dFrame.to_csv(newName, index=False)

                print("Deleting .txt...")
                remove(fullName)

                print("Complete.\n")
