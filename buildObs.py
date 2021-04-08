import pandas as pd
import re

def buildObs(inFName: str, floorID: str):

    waypoint_x = 0.0
    waypoint_y = 0.0
    floor = "0"

    inFile = open (inFName, "r")
    inFileLines = inFile.readlines()

    names=["ts",
           "floor",
           "waypoint_x",
           "waypoint_y",
           "accel_1",
           "accel_2",
           "accel_3",
           "accel_4",
           "magnet_1",
           "magnet_2",
           "magnet_3",
           "magnet_4",
           "gyro_1",
           "gyro_2",
           "gyro_3",
           "gyro_4",
           "magnet_un_1",
           "magnet_un_2",
           "magnet_un_3",
           "magnet_un_4",
           "magnet_un_5",
           "magnet_un_6",
           "magnet_un_7",
           "gyro_un_1",
           "gyro_un_2",
           "gyro_un_3",
           "gyro_un_4",
           "gyro_un_5",
           "gyro_un_6",
           "gyro_un_7",
           "accel_un_1",
           "accel_un_2",
           "accel_un_3",
           "accel_un_4",
           "accel_un_5",
           "accel_un_6",
           "accel_un_7",
           "wifi_1",
           "wifi_2",
           "wifi_3",
           "wifi_4",
           "wifi_5",
           "beacon_1",
           "beacon_2",
           "beacon_3",
           "beacon_4",
           "beacon_5",
           "beacon_6",
           "beacon_7",
           "beacon_8"
           ]
    dFrame = pd.DataFrame(columns=names)

    #Set the floor where 1F or F1 = 0, F2 = 1, and 1B = 01
    if "B" in (floorID):
        floor = str((int(re.findall("\d+", floorID)[0]) ) * -1)

    if "F" in (floorID):
        floor = str(int(re.findall("\d+", floorID)[0]) - 1)

    #Create rows of data for each observation by timestamp
    for line in inFileLines:

        splitLine = line.split()

        if "TYPE" in line:

            if splitLine[1] == "TYPE_WAYPOINT":

                waypoint_x = float(splitLine[2])
                waypoint_y = float(splitLine[3])

            elif splitLine[1] == "TYPE_ACCELEROMETER":

                accel_1 = float(splitLine[2])
                accel_2 = float(splitLine[3])
                accel_3 = float(splitLine[4])
                accel_4 = float(splitLine[5])

            elif splitLine[1] == "TYPE_MAGNETIC_FIELD":

                magnet_1 = float(splitLine[2])
                magnet_2 = float(splitLine[3])
                magnet_3 = float(splitLine[4])
                magnet_4 = float(splitLine[5])

            elif splitLine[1] == "TYPE_GYROSCOPE":

                gyro_1 = float(splitLine[2])
                gyro_2 = float(splitLine[3])
                gyro_3 = float(splitLine[4])
                gyro_4 = float(splitLine[5])

            elif splitLine[1] == "TYPE_ROTATION_VECTOR":

                rot_1 = float(splitLine[2])
                rot_2 = float(splitLine[3])
                rot_3 = float(splitLine[4])
                rot_4 = float(splitLine[5])

            elif splitLine[1] == "TYPE_MAGNETIC_FIELD_UNCALIBRATED":

                magnet_un_1 = float(splitLine[2])
                magnet_un_2 = float(splitLine[3])
                magnet_un_3 = float(splitLine[4])
                magnet_un_4 = float(splitLine[5])
                magnet_un_5 = float(splitLine[6])
                magnet_un_6 = float(splitLine[7])
                magnet_un_7 = float(splitLine[8])

            elif splitLine[1] == "TYPE_GYROSCOPE_UNCALIBRATED":

                gyro_un_1 = float(splitLine[2])
                gyro_un_2 = float(splitLine[3])
                gyro_un_3 = float(splitLine[4])
                gyro_un_4 = float(splitLine[5])
                gyro_un_5 = float(splitLine[6])
                gyro_un_6 = float(splitLine[7])
                gyro_un_7 = float(splitLine[8])

            elif splitLine[1] == "TYPE_ACCELEROMETER_UNCALIBRATED":

                accel_un_1 = float(splitLine[2])
                accel_un_2 = float(splitLine[3])
                accel_un_3 = float(splitLine[4])
                accel_un_4 = float(splitLine[5])
                accel_un_5 = float(splitLine[6])
                accel_un_6 = float(splitLine[7])
                accel_un_7 = float(splitLine[8])

                dFrame = dFrame.append({
                    "ts": float(splitLine[0]),
                    "floor" : floor,
                    "waypoint_x": waypoint_x,
                    "waypoint_y": waypoint_y,
                    "accel_1": accel_1,
                    "accel_2": accel_2,
                    "accel_3": accel_3,
                    "accel_4": accel_4,
                    "magnet_1": magnet_1,
                    "magnet_2": magnet_2,
                    "magnet_3": magnet_3,
                    "magnet_4": magnet_4,
                    "gyro_1": gyro_1,
                    "gyro_2": gyro_2,
                    "gyro_3": gyro_3,
                    "gyro_4": gyro_4,
                    "rot_1": rot_1,
                    "rot_2": rot_2,
                    "rot_3": rot_3,
                    "rot_4": rot_4,
                    "magnet_un_1" : magnet_un_1,
                    "magnet_un_2" : magnet_un_2,
                    "magnet_un_3": magnet_un_3,
                    "magnet_un_4": magnet_un_4,
                    "magnet_un_5": magnet_un_5,
                    "magnet_un_6": magnet_un_6,
                    "magnet_un_7": magnet_un_7,
                    "gyro_un_1": gyro_un_1,
                    "gyro_un_2": gyro_un_2,
                    "gyro_un_3": gyro_un_3,
                    "gyro_un_4": gyro_un_4,
                    "gyro_un_5": gyro_un_5,
                    "gyro_un_6": gyro_un_6,
                    "gyro_un_7": gyro_un_7,
                    "accel_un_1": accel_un_1,
                    "accel_un_2": accel_un_2,
                    "accel_un_3": accel_un_3,
                    "accel_un_4": accel_un_4,
                    "accel_un_5": accel_un_5,
                    "accel_un_6": accel_un_6,
                    "accel_un_7": accel_un_7},
                    ignore_index=True)

            elif splitLine[1] == "TYPE_WIFI":

                dFrame = dFrame.append({
                    "ts": float(splitLine[0]),
                    "floor": floor,
                    "waypoint_x": waypoint_x,
                    "waypoint_y": waypoint_y,
                    "wifi_1": str(splitLine[2]),
                    "wifi_2": str(splitLine[3]),
                    "wifi_3": float(splitLine[4]),
                    "wifi_4": float(splitLine[5]),
                    "wifi_5": float(splitLine[6])},
                    ignore_index=True)

            elif splitLine[1] == "TYPE_BEACON":

                dFrame = dFrame.append({
                    "ts": float(splitLine[0]),
                    "floor": floor,
                    "waypoint_x": waypoint_x,
                    "waypoint_y": waypoint_y,
                    "beacon_1": str(splitLine[2]),
                    "beacon_2": str(splitLine[3]),
                    "beacon_3": str(splitLine[4]),
                    "beacon_4": float(splitLine[5]),
                    "beacon_5": float(splitLine[6]),
                    "beacon_6": float(splitLine[7]),
                    "beacon_7": str(splitLine[8]),
                    "beacon_8": float(splitLine[9])},
                    ignore_index=True)

    return dFrame.copy()