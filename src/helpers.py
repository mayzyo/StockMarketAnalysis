import numpy as np
import re
import pandas as pd
from datetime import datetime, timedelta

def scope_dataframe(df, time_range):
    now = datetime.now()
    start = now - timedelta(days=time_range)
    return df.loc[(df.index >= start) & (df.index <= now)]

def annotate_arrows(ax, yPos, label=[], indexes=[]):
    for i in range(len(yPos)):
        x = i if len(indexes) == 0 else indexes[i]
        y = yPos[i]
        ax.annotate(label[i] if len(label) > 0 else np.round(y, decimals=2),
            xy=(x, y),
            xycoords='data',
            color='b',
            xytext=(-20, 40), textcoords='offset points',
            bbox=dict(boxstyle='round,pad=0.2', fc='black', alpha=0.3),
            arrowprops=dict(facecolor='b', shrink=0.02),
            horizontalalignment='right', verticalalignment='top')

def annotate_texts(ax, yPos, label=[], indexes=[]):
    for i in range(len(yPos)):
        x = i if len(indexes) == 0 else indexes[i]
        y = yPos[i]
        ax.annotate(label[i] if len(label) > 0 else np.round(y, decimals=2),
            xy=(x, y),
            xycoords='data',
            color='b',
            xytext=(-20, 40),
            bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.3),
            textcoords='offset points')

def correct_ticker(input):
    exDict = {
        'SH': 'SS',
        'SZ': 'SZ'
    }
    if type(input) == str:
        try:
            digits = re.findall('[0-9]+', input)
            if digits:
                exchange = input.replace(digits[0], '')
                ticker = f'{digits[0]}.{exDict[exchange]}'
                return ticker
        except:
            print(input)
    return None

def load_txt(path):
    df = pd.read_csv(path, sep='\t+', engine='python')
    df['代码'] = df['代码'].apply(lambda row : correct_ticker(row))
    return df