from src.extract import baixar_csv, baixar_totais_validacao, ler_csv_para_validacao, ler_dados_csv
from src.map import detectar_valores_vazios, expandir_dados
from src.validate import test_validate_data
from src.regressao import aplicar_regressao

URL_BASE = "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2024.csv"
URL_VALIDACAO = "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_TOTAIS_CONFERENCIA.csv"

# Baixando dados
baixar_csv(URL_BASE, "EXP_2024.csv")
baixar_totais_validacao(URL_VALIDACAO, "2024_validation.csv")

# Lendo dados
df = ler_dados_csv(r"input\EXP_2024.csv")
validation = ler_csv_para_validacao(r"input\2024_validation.csv")

# Conferindo totais
test_validate_data(df, validation)

# Detectando valores vazios
df = detectar_valores_vazios(df)
# Expandindo os dados
df = expandir_dados(df)

# Aplicando modelo de regressão para o produto de carnes (outros filtros podem ser inseridos)
aplicar_regressao(df, "CARNES")

print("Consolidando arquivo final.")
print(df)
df.to_csv(r"output\dados_finais.csv", index=False)
