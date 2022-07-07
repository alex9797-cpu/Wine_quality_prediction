

import pandas as pd
import numpy as np


def print_summary_stats(data: pd.DataFrame,index:int)-> None:
    print(f'Variable {data.columns[index]}')
    print(f'Mean: {np.mean(data.iloc[:,index])}')
    print(f'Maximum: {np.max(data.iloc[:, index])}')
    print(f'Minimum: {np.min(data.iloc[:, index])}')
    print(f'Median: {np.median(data.iloc[:, index])}')
    print(f'Variance: {np.std(data.iloc[:, index])**2}')
    print(f'SD: {np.std(data.iloc[:, index])}')
    print('\n')