from typing import List

import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame


class HeatMap:
    df: DataFrame
    xlabels: List

    def __init__(self, df: DataFrame, xlabels: List):
        if df.shape[1] != len(xlabels):
            raise Exception("Length of the xlabels list should match the number of dataframe columns")
        self.df = df
        self.xlabels = xlabels

    def plot(self, output_file_path, title):
        df = self.df.loc[:, (self.df != 0).any(axis=0)]
        if df.empty:
            df = self.df
        plt.figure(figsize=(10, 7))
        hm = sns.heatmap(
            df, cmap="gray_r", square=True,
            linewidths=0.1)
        for _, spine in hm.spines.items():
            spine.set_visible(True)
        hm.set_yticklabels(hm.get_yticklabels(), rotation=0)
        hm.set_xticklabels(hm.get_xticklabels(), rotation=90)
        hm.set_title(title)
        plt.savefig(output_file_path)
        # plt.show()
