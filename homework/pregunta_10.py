import pandas as pd
def pregunta_10():
    df = pd.read_csv("tbl0.tsv", sep="\t")
    return (
        df.groupby("c1")["c2"]
        .apply(lambda x: ":".join(map(str, sorted(x))))
        .to_frame()
    )