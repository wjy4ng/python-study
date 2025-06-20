from tkinter import *
import csv
import pandas as pd

class App():
    def __init__(self):
        pass

    def run(self, file="./weather.csv"):
        wdf = pd.read_csv(file, encoding='UTF-8').set_index('일시')
        wdf['month'] = pd.DatetimeIndex(wdf.index).month

        month_wdf = wdf.groupby('month').max()
        print(month_wdf.loc[[6]])
    
if __name__=="__main__":
    app = App()
    app.run()
