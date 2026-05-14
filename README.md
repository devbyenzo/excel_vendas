# 📊 Analisador de Planilhas com Python

Projeto desenvolvido em **Python** para analisar uma planilha detalhada de forma automatizada, processando os dados e exibindo os resultados de maneira clara, organizada e prática.

---

# 🚀 Sobre o Projeto

Este script foi criado com o objetivo de facilitar a análise de dados presentes em planilhas, evitando processos manuais e economizando tempo.

Com ele, é possível carregar uma planilha, ler suas informações, processar os dados e apresentar os resultados finais diretamente no terminal.

---

# 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- OpenPyXL

---

# 📁 Estrutura do Projeto

```bash
projeto/
│
├── main.py
├── planilha.xlsx
├── requirements.txt
└── README.md
```

---

# 📦 Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

## 2. Acesse a pasta do projeto

```bash
cd seu-repositorio
```

## 3. Crie um ambiente virtual

```bash
python -m venv venv
```

## 4. Ative o ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

## 5. Instale as dependências

```bash
pip install -r requirements.txt
```

---

# ▶️ Como Usar

## 1. Coloque sua planilha na pasta do projeto

Adicione o arquivo `.xlsx` dentro da pasta principal do projeto.

Exemplo:

```bash
planilha.xlsx
```

## 2. Verifique o nome da planilha no código

No arquivo `main.py`, confira se o nome do arquivo está correto:

```python
arquivo = "planilha.xlsx"
```

## 3. Execute o script

```bash
python main.py
```

## 4. Veja o resultado

Após a execução, o script irá analisar os dados da planilha e mostrar o resultado no terminal.

---

# 📌 Exemplo de Saída

```bash
Análise concluída com sucesso!

Total de registros analisados: 150
Maior valor encontrado: R$ 2.500,00
Menor valor encontrado: R$ 50,00
Média dos valores: R$ 730,00
```

---

# 📄 Exemplo de Código Base

```python
import pandas as pd

arquivo = "planilha.xlsx"

df = pd.read_excel(arquivo)

print("Planilha carregada com sucesso!")
print(df.head())

print("Total de registros:", len(df))
```

---

# ✅ Funcionalidades

- Leitura de planilhas `.xlsx`
- Análise automática dos dados
- Exibição dos resultados no terminal
- Código simples e fácil de adaptar
- Organização dos dados com Pandas

---

# 📋 Requirements

Crie um arquivo chamado `requirements.txt` com:

```txt
pandas
openpyxl
```

---

# 🎯 Objetivo

O objetivo deste projeto é praticar automação com Python, leitura de planilhas e análise de dados, criando uma ferramenta simples, funcional e útil para diferentes tipos de relatórios.

---

# 📌 Possíveis Melhorias Futuras

- Exportar o resultado para uma nova planilha
- Criar gráficos automáticos
- Gerar relatórios em PDF
- Criar uma interface gráfica
- Permitir seleção automática do arquivo

---

# 👨‍💻 Autor

Desenvolvido por **Enzo Pietrantonio**.

---

# 📜 Licença

Este projeto está sob a licença MIT.
