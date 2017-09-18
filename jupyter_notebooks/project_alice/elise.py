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

from os import listdir
import glob
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
    csv_file_names = read_csv_from_dir(path_to_csv_files)
    print(csv_file_names)

    site_id = 1
    site_freq = {}

    #for idx, file_name in enumerate(csv_file_names):
    for file_name in csv_file_names:
        myfile = open(path_to_csv_files + file_name, "rU")  # чтение из файла
        for idx, line in enumerate(myfile.readlines()):  # построчно читаем файл и выводим на экран
            if (idx != 0):
                data = line.split(',')
                site_name = data[1].rstrip()

                if (site_name in site_freq.keys()):
                    site_freq[site_name]['freq'] = site_freq[site_name]['freq'] + 1
                else:
                    site_freq[site_name] = {'id': site_id, 'freq': 1}
                    site_id = site_id + 1
    print(site_freq)


prepare_train_set()