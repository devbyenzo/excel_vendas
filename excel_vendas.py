# Autor: Enzo
# Projeto - Verificar quantos determinados produtos foram vendidos seguindo uma planilha .xlsx

import pandas as pd


def Excel():
    # 1 - Lendo a planilha
    data = pd.read_excel("vendas.xlsx")

    # 2 - Agrupando os dados (Incluindo o ID do Produto para não dar erro no print)
    df_agrupa = (
        data.groupby(["Nome_Produto", "ID_Produto"], as_index=False)[
            "Quantidade_Vendida"
        ]
        .sum()
    )

    # 3 - Criando a coluna unificada
    df_agrupa["Resultado"] = (
        df_agrupa["Nome_Produto"]+ ", " + df_agrupa["Quantidade_Vendida"].astype(str))

    # 4 - Loop para pegar tudo e printar
    for linha in df_agrupa.itertuples():
        print(
            f"Produto: {linha.Nome_Produto}, Quantidade: {linha.Quantidade_Vendida}, ID: {linha.ID_Produto}"
        )


Excel()
