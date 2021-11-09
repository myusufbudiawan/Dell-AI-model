import pandas as pd
from keras.models import Sequential, load_model
from keras.layers import *
from pandas.core.algorithms import unique
from pandas.core.indexes.base import Index
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf


class attribute_retrieval:
    # size of data
    # isboolean or not
    # type of dataset

    size_dataset_class = 'small'

    def dataset_size():
        df = pd.read_csv("input.csv")

        no_index = len(df.index)
        no_columns = len(df.columns)

        size_dataset = no_index/no_columns

        if (size_dataset <= 10000):
            size_dataset_class = 'small'
        else:
            size_dataset_class = 'big'
    
        return size_dataset_class
