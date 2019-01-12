import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(20).reshape((4,5)), columns = list("abcde"))

sub_df = df.agg({"a":["min", "mean"]})

print(df)
print(sub_df)
