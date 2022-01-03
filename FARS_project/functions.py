import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO, StringIO
import xlrd


class HelperFunctions:

    def __init__(self, filepath):
        self.filepath = filepath
    
    def load_csv(self):
        with open(self.filepath, 'rb') as f:
            fileData = f.read().decode('ISO-8859-1')
            data = StringIO(fileData)
            df = pd.read_csv(data)
            return df