import tkinter as tk
import pyedflib
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
import glob
import pickle
# import pandas as pd
from scipy import signal
import os

def GetFilesListFromFolder(FolderName=None, FileExtention=None, IsToSort=True):

    """
    Function for getting the files list from folder root specified in the parameter FolderName.


    :param FolderName: string variable

        The root to the needed folder with necessary files
        Usually it is the root taken from the os function glob

    :param FileExtention: string variable

        The extension of the files you want to get

        Example:
        FileExtension = 'edf'

    :param IsToSort:

    :example

        dataFolder = '/home/admin/PycharmProjects/data/'

        foldersList = glob.glob(dataFolder)

        for i in foldersList:
            FileListInCurrentFolder = GetFilesListFromFolder(FolderName=foldersList[i],
                                                             FileExtension='edf',
                                                             isToSort=True)

    :return: FilesList if the :param isToSort set to False
             SortedList if the :param isToSort set to True
    """


    if FolderName is None:
        raise ValueError("parameter FolderName cannot be NONE!")

    if FileExtention is None:
        raise ValueError("parameter FileExtention cannot be NONE!")


    FilesList = glob.glob(FolderName+'/*.'+FileExtention)

    if IsToSort == False:
        return FilesList

    else:
        SortedList = [0 for i in range(len(FilesList))]

        for i in range(len(FilesList)):
            lhs = FilesList[i].split("/")
            lunderscored = lhs[len(lhs) - 1].split("_")
            ldotted = lunderscored[len(lunderscored) - 1].split(".")
            SortedList[int(ldotted[0]) - 1] = FilesList[i]

        return SortedList


def GetSignalsListFromEDF(FileName):

    f = pyedflib.EdfReader(FileName)
    NumberOfSignals = f.signals_in_file
    BirthDate = f.birthdate
    Gender = f.gender
    Name = f.patientname
    SignalLabels = f.getSignalLabels()
    NumberOfSamp = f.getNSamples()[0]
    SignalList = np.zeros((NumberOfSignals, f.getNSamples()[0]))
    Fs = round(len(SignalList[3, :]) / f.file_duration)

    for i in np.arange(NumberOfSignals):
        SignalList[i, :] = f.readSignal(i)

    return SignalList, Fs, SignalLabels, NumberOfSignals, BirthDate, Gender, Name

def GetSignalsListFromEDFPRO(FileName):

    f = pyedflib.EdfReader(FileName)
    NumberOfSignals = f.signals_in_file
    BirthDate = f.birthdate
    Gender = f.gender
    Name = f.patientname
    SignalLabels = f.getSignalLabels()
    NumberOfSamp = f.getNSamples()[0]
    SignalList = np.zeros((NumberOfSignals, f.getNSamples()[0]))
    Fs = round(len(SignalList[3, :]) / f.file_duration)

    for i in np.arange(NumberOfSignals):
        SignalList[i, :] = f.readSignal(i)

    return SignalList

def FindTheShortestEDFFileInFolder(FolderName):

    FilesList = glob.glob("%s*.edf" % FolderName)

    ShortestDurationFileName = ''
    CurrentFileDuration = 0
    ShortestFileDuration = 0

    for i in range(len(FilesList)):
        f = pyedflib.EdfReader(FilesList[i])

        if i == 0:
            ShortestFileDuration = f.getNSamples()[0]
            ShortestDurationFileName = FilesList[i]

        else:
            CurrentFileDuration = f.getNSamples()[0]
            if CurrentFileDuration < ShortestFileDuration:
                ShortestFileDuration = CurrentFileDuration
                ShortestDurationFileName = FilesList[i]
        f._close()

    return ShortestFileDuration, ShortestDurationFileName

def is_the_directory_exists(directory=None):

    if directory is None:
        raise ValueError("Please define the path to the folder to check if the directory is present!")

    #check if the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory

def is_the_file_exists(path_to_file):

    if not os.path.isfile(path_to_file):
        raise ValueError("File does not exist!")


def save_dict_to_obj_file(input_dict=None, filename="default", output_folder=None, mode="wb"):

    if input_dict is None:
        raise ValueError("Please define the dictionary you want to save!")

    if output_folder is None:
        raise ValueError("Please specify the output folder!")

    output_folder = is_the_directory_exists(output_folder)

    file = open(output_folder + filename + '.obj', mode)

    pickle.dump(input_dict, file)

    print('Generating Data for DFA Completed!')

    return


def get_data_from_obj_file(path_to_file=None):

    if path_to_file is None:
        raise ValueError("Please define name of the input file!")

    is_the_file_exists(path_to_file)

    filehandler = open(path_to_file, 'rb')
    data = pickle.load(filehandler)

    return data

