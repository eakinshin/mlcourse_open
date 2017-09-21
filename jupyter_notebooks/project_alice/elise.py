from __future__ import division, print_function
# отключим всякие предупреждения Anaconda
import warnings
from gc import enable

warnings.filterwarnings('ignore')
from glob import glob
import os
import pickle
#pip install tqdm
from tqdm import tqdm_notebook
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from pandas import DataFrame

from os import listdir
from pathlib import Path

def read_csv_from_dir(path_to_csv_files):
    all_files = listdir(path_to_csv_files)
    csv_files = filter(lambda x: x.endswith('.csv'), all_files)
    arr = []
    for x in csv_files:
        arr.append(x)
    return arr

def read_csv_from_dir_glob(path_to_csv_files):
    result = []
    for file_path in Path(path_to_csv_files).glob('**/*.csv'):
        result.append(file_path)  # do whatever you need with these files
    return result


def prepare_train_set(path_to_csv_files='d:/work/MachineLearning/OpenDataScience/2_курс/mlcourse_open/jupyter_notebooks/project_alice/capstone_user_identification/3users/', session_length=10):

    # read file names from current dir
    csv_file_names = read_csv_from_dir(path_to_csv_files)
    print(csv_file_names)

    #initial data
    site_id = 1
    site_freq = {}

    #prepare data frame
    cols = []
    for i in range(1, session_length + 1, 1):
        cols.append("site" + str(i))
    cols.append("user_id")
    df = DataFrame(columns = cols)
    print(df)
    row_id = 1

    #read files
    for file_name in csv_file_names:

        user_id = int(float((file_name.rsplit('user', 1)[1]).rsplit(".")[0]))
        print(user_id)

        session_idx = 0
        row = []
        myfile = open(path_to_csv_files + file_name, "rU")  # чтение из файла
        lines = myfile.readlines()
        myfile.close()
        for idx, line in enumerate(lines):  # построчно читаем файл и выводим на экран
            if (idx != 0):
                data = line.split(',')
                site_name = data[1].rstrip()
                #fill site_freq
                if (site_name in site_freq.keys()):
                    site_freq[site_name]['freq'] = site_freq[site_name]['freq'] + 1
                else:
                    site_freq[site_name] = {'id': site_id, 'freq': 1}
                    site_id = site_id + 1

                row.append(site_freq[site_name]['id'])
                if (idx == len(lines) - 1):
                    while (session_idx < 9):
                        row.append(0)
                        session_idx += 1
                    row.append(user_id)
                    session_idx = 0
                    print(row)
                    df.loc[row_id] = row
                    row_id = row_id + 1
                    row = []
                session_idx += 1

                if (session_idx >= 10) :
                    row.append(user_id)
                    print(row)
                    df.loc[row_id] = row
                    row_id = row_id + 1
                    row = []
                    session_idx = 0
    print(site_freq)
    print(df)


prepare_train_set()