import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

usa_df = pd.read_csv("../data/raw/usa_00005-002/usa_00005-002.csv")

usa_df_cleaning = usa_df.copy()

usa_df_cleaning.isnull.sum()