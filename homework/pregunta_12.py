import pandas as pd
def pregunta_12():
    df = pd.read_csv("tbl2.tsv", sep="\t")
    df["pair"] = df["c5a"] + ":" + df["c5b"].astype(str)
    return (
        df.groupby("c0")["pair"]
        .apply(lambda x: ",".join(sorted(x)))
        .reset_index(name="c5")
    )