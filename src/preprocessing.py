import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:

    df = pd.read_csv(filepath)
    return df

def preprocess_data(df: pd.DataFrame) -> tuple:

    df["Mega_Evolution"] = df["Name"].apply(lambda x: 1 if "Mega" in x else 0)

    df = df.drop(columns=["Name", "Type 1", "Type 2", "Generation", "Legendary"], errors="ignore")

    X = df.drop(columns=["Mega_Evolution"])
    y = df["Mega_Evolution"]
    return X, y
