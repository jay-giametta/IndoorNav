import pandas as pd
import numpy as np

def cleanObs(dFrame: pd.DataFrame):

    #perform bidirectional linear interpolation to fill in missing values
    dFrame = dFrame.interpolate(limit_direction="both")

    for column in dFrame.columns:

        if dFrame[column].dtype == "float64":

            #if there are any leftover missing float values replace them with the mean
            dFrame[column] = dFrame[column].replace(np.nan,dFrame[column].mean())

        else:

            #if there are any missing string values replace them with NULL
            dFrame[column] = dFrame[column].replace(np.nan, "NULL")

    return dFrame