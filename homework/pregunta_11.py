import pandas as pd
def pregunta_11():
    df = pd.read_csv("tbl1.tsv", sep="\t")
    return (
        df.groupby("c0")["c4"]
        .apply(lambda x: ",".join(sorted(x)))
        .reset_index()
    )