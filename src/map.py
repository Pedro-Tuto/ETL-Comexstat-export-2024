import pandas as pd

def detectar_valores_vazios(df: pd.DataFrame) -> pd.DataFrame:
    if df.isna().any().any():
        df = df.fillna(0)
        return df
    else:
        print("Nenhum valor vazio encontrado.")
        return df
    

def expandir_estados(df: pd.DataFrame, sg_uf_dict_path: str) -> pd.DataFrame:
    print("Expandindo estados.")
    sg_uf_dict = pd.read_csv(sg_uf_dict_path, sep=";")
    df_merged = pd.merge(df, sg_uf_dict, on="SG_UF_NCM", how="left")
    return df_merged



def expandir_dados(df: pd.DataFrame) -> pd.DataFrame:
    expandir_estados(df, r"dicionarios/sg_uf.csv")
    return df
