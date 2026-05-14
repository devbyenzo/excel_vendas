# 📦 Análise de Vendas com Python e Excel

Projeto desenvolvido em Python para analisar uma planilha `.xlsx` de vendas, agrupando produtos automaticamente e exibindo a quantidade total vendida de cada item no terminal.

---

# 🚀 Funcionalidades

- Leitura de arquivos Excel `.xlsx`
- Agrupamento automático de produtos
- Soma da quantidade vendida
- Exibição organizada no terminal
- Tratamento utilizando ID do produto
- Código simples e didático para estudos de análise de dados

---

# 🛠️ Tecnologias utilizadas

- Python
- Pandas
- OpenPyXL

---

# 📁 Estrutura do projeto

```bash
analise-vendas/
│
├── main.py
├── vendas.xlsx
├── requirements.txt
└── README.md
```

---

# 📄 Estrutura da planilha

O arquivo `vendas.xlsx` deve conter as seguintes colunas:

| Nome_Produto | ID_Produto | Quantidade_Vendida |
|--------------|------------|--------------------|
| Mouse Gamer | 101 | 2 |
| Mouse Gamer | 101 | 5 |
| Teclado RGB | 102 | 3 |

---

# ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Entre na pasta:

```bash
cd seu-repositorio
```

Instale as dependências:

```bash
pip install pandas openpyxl
```

---

# ▶️ Como executar

Certifique-se de que o arquivo `vendas.xlsx` esteja na mesma pasta do código Python.

Depois execute:

```bash
python main.py
```

---

# 💻 Código principal

```python
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
```

---

# 📌 Como o sistema funciona

## 1️⃣ Leitura da planilha

O sistema utiliza o `pandas` para abrir o arquivo:

```python
pd.read_excel("vendas.xlsx")
```

---

## 2️⃣ Agrupamento dos produtos

Os dados são agrupados por:
- Nome do produto
- ID do produto

Depois disso, o sistema soma automaticamente todas as quantidades vendidas.

---

## 3️⃣ Organização dos resultados

O programa cria uma coluna personalizada chamada `Resultado`, unificando:
- Nome do produto
- Quantidade vendida

---

## 4️⃣ Exibição no terminal

O sistema percorre todos os produtos agrupados e exibe:

```bash
Produto: Mouse Gamer, Quantidade: 7, ID: 101
```

---

# ✅ Exemplo de saída

```bash
Produto: Mouse Gamer, Quantidade: 7, ID: 101
Produto: Teclado RGB, Quantidade: 3, ID: 102
```

---

# 📸 Preview

Você pode adicionar prints do:
- Código utilizando CodeSnap
- Planilha Excel
- Resultado no terminal

Exemplo:

```markdown
<p align="center">
  <img src="images/codesnap.png" width="900"/>
</p>
```

---

# 📦 Requirements

Arquivo `requirements.txt`:

```txt
pandas
openpyxl
```

---

# 👨‍💻 Autor

Desenvolvido por **Enzo**.

---

# 📜 Licença

Este projeto está sob a licença MIT.
