import pandas as pd
import numpy as np
import pickle

model_df = pd.read_csv('testresample_df.csv')


def get_rec(userChoice,df):
    #pred = []
    df = df.reset_index()
    if userChoice in df['name'].values:
        return list(df.iloc[df[userChoice].sort_values(ascending =False)[1:6].index]['name'].values)
        # return list(df.loc[userChoice].sort_values(ascending =False)[1:5].index)
    # else:
    #     return "Song not included"
    #final_pred = pred[0:5]
    #return final_pred
