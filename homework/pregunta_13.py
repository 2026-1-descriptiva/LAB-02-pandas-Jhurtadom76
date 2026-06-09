import pandas as pd
def pregunta_13():

    t0 = pd.read_csv("tbl0.tsv", sep="\t")
    t2 = pd.read_csv("tbl2.tsv", sep="\t")
    m = pd.merge(t0, t2, on="c0")
    return m.groupby("c1")["c5b"].sum()