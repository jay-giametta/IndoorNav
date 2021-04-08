import buildObs as bo
import cleanObs as co
import pandas as pd

from os import listdir
from os import remove
from os.path import isfile

path = "data/train"

for file in listdir(path):

    for floor in listdir(path + "/" + file):

        for fileName in listdir(path + "/" + file + "/" + floor):

            if "txt" in fileName:

                fullName = path + "/" + file + "/" + floor + "/" + fileName

                print(fullName.replace("txt","csv"))
                print("Building observations...")
                dFrame = pd.DataFrame(bo.buildObs(fullName, floor))

                print("Cleaning observations...")
                dFrame = pd.DataFrame(co.cleanObs(dFrame))

                print("Writing .csv...")
                dFrame.to_csv(fullName.replace("txt","csv"),index=False)

                print("Deleting .txt...")
                remove(fullName)

                print("Complete.\n")
