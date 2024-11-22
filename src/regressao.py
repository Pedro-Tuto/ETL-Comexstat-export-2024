import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd
from sklearn.metrics import mean_squared_error

def aplicar_regressao(df, produto):
    df_produto = df[df['id_product'] == produto]
    
    if df_produto.empty:
        print(f"O produto '{produto}' não foi encontrado no dataframe.")
        return
    
    # Selecionando variáveis preditoras (features) e variável alvo (target)
    X = df_produto[['CO_ANO', 'CO_MES', 'CO_NCM', 'CO_UNID', 'CO_PAIS', 'SG_UF_NCM', 'CO_VIA', 'CO_URF', 'QT_ESTAT', 'KG_LIQUIDO']]
    y = df_produto['VL_FOB']
    
    # Dividindo os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Definindo um pipeline com pré-processamento e modelo
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['CO_PAIS', 'SG_UF_NCM'])  # Exemplo de variáveis categóricas
        ], 
        remainder='passthrough'  # As variáveis numéricas são passadas sem alteração
    )
    
    modelo = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())  # Modelo de regressão linear
    ])
    
    # Treinando o modelo
    modelo.fit(X_train, y_train)
    
    # Fazendo previsões
    y_pred = modelo.predict(X_test)
    
    # Exibindo as previsões e os valores reais
    print("Previsões:", y_pred[:5])  # Mostra as primeiras 5 previsões
    print("Valores reais:", y_test[:5].values)  # Mostra os primeiros valores reais
    
    # Calculando o erro quadrático médio (MSE)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Erro quadrático médio (MSE): {mse}")
    
    # Podemos também calcular o erro médio absoluto (MAE) para entender melhor a precisão
    mae = abs(y_test - y_pred).mean()
    print(f"Erro médio absoluto (MAE): {mae}")

    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, color='blue', label='Previsões vs Reais')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2, label='Linha de Perfeição')
    plt.xlabel('Valores Reais')
    plt.ylabel('Previsões')
    plt.title(f'Previsões vs Valores Reais para o produto {produto}')
    plt.legend()
    plt.grid(True)
    
    plt.savefig(f'output/grafico_previsao_{produto}.png')
    plt.show()
