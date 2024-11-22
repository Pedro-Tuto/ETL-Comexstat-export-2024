# Projeto de Análise de Dados de Exportação

Este projeto realiza a análise de dados de exportação para 2024, fazendo downloads de arquivos CSV, limpando e transformando os dados, e expandindo as informações com base em um dicionário de estados. O código foi refatorado para melhorar a organização e eficiência da análise.

## Estrutura de Pastas

- **dicionarios/**: Contém os arquivos que são usados para expandir os dados. Exemplo: dicionários de estados.
- **input/**: Armazena os arquivos CSV baixados durante o processo. Estes são os arquivos brutos que serão processados.
- **output/**: Contém os arquivos CSV resultantes após o processamento, com os dados limpos e transformados.
- **src/**: Contém o código fonte do projeto, incluindo funções e a lógica de processamento de dados.
- **requirements.txt**: Lista todas as dependências necessárias para rodar o projeto. Basta instalar as dependências com `pip install -r requirements.txt`.

## Como Rodar o Projeto

1. Clone o repositório em sua máquina local.
2. Crie um ambiente virtual para isolar as dependências do projeto, evitando conflitos com outras versões de bibliotecas que você possa ter instaladas globalmente. Para criar e ativar o ambiente virtual, siga os seguintes passos:

   - **No Windows**:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **No Linux/Mac**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Instale as dependências necessárias executando o seguinte comando:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o arquivo `main.py` para rodar o processo de análise:
   ```bash
   python main.py
   ```

## Descrição do Processo

1. O script `main.py` faz o download de arquivos CSV (dados de exportação) e os armazena na pasta **input**.
2. Ele então carrega e processa esses arquivos, tratando valores vazios e expandindo os dados com informações de estados.
3. O arquivo final, contendo os dados transformados, é salvo na pasta **output**.

## Dependências

As dependências necessárias para rodar o projeto estão listadas no arquivo `requirements.txt`. Algumas das principais bibliotecas são:

- `pandas`: Para manipulação de dados.
- `requests`: Para realizar downloads dos arquivos CSV.

---
