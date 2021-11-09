import pandas as pd
from keras.models import Sequential, load_model
from keras.layers import *
from pandas.core.algorithms import unique
from pandas.core.indexes.base import Index
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf

# supervise or not
# size of data
# isboolean or not
# type of dataset
# goal


df_size = ""
df = pd.read_csv("input.csv")


def dataset_size():

    no_index = len(df.index)

    size_dataset = no_index

    if (size_dataset <= 10000):
        size_dataset_class = 'Small'
    else:
        size_dataset_class = 'Big'

    return size_dataset_class


def is_supervise():
    supervised = True

    for col in df.columns:
        for character in col:
            if character.isdigit():
                supervised = False

    return supervised


def is_binary():

    isBinary = 'FALSE'

    last_column = df.iloc[:, -1:]
    # print(last_column)

    array = last_column.to_numpy()

    for i in array:
        if i == 'yes' or i == 'no' or i == 'true' or i == 'false' or i == 1 or i == 0:
            isBinary = 'TRUE'

    # print(len(df.columns))
    # print(df.columns.values)

    # print(last_column.iloc[1]['binary_type'])

    return isBinary


def det_goal():
    if (is_boolean() == True):
        goal = 'classification'
    else:
        goal = 'regression'

    return goal
