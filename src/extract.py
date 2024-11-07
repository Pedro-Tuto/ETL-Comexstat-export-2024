import requests
import pandas as pd

def ler_dados_csv(file_path, delimiter=";"):
    df = pd.read_csv(file_path, sep=delimiter)
    return df

def ler_csv_para_validacao(file_path, delimiter=";"):
    df = pd.read_csv(file_path, sep=delimiter)
    return df

def baixar_csv(url, filename):
    print("Baixando dados de Exportação 2024.")
    response = requests.get(url)
    if response.status_code == 200:
        file_path = f"input/{filename}"
        with open(file_path, "wb") as file:
            file.write(response.content)

def baixar_totais_validacao(url, filename):
    print("Baixando totais para validação.")
    response = requests.get(url)
    if response.status_code == 200:
        file_path = f"input/{filename}"
        with open(file_path, "wb") as file:
            file.write(response.content)
