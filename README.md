# 🚀 Databricks Lakehouse - Arquitetura Medalhão

![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta_Lake-00ADD8?style=for-the-badge&logo=delta-lake&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Este repositório contém a implementação completa de um pipeline de dados utilizando a **Arquitetura Medalhão** no **Databricks Free Edition**. O objetivo é transformar dados brutos em insights estruturados através de camadas de qualidade e modelagem dimensional.

---

## 🏗️ Arquitetura do Projeto

O pipeline segue o fluxo da Arquitetura Medalhão, garantindo governança, qualidade e performance:

1.  **Landing (Dados Brutos):** Ponto de entrada onde os arquivos originais (CSV/JSON) são armazenados sem modificações.
2.  **Bronze (Dados Crus):** Ingestão dos dados da Landing para tabelas Delta, adicionando metadados de auditoria (data de carga e origem).
3.  **Silver (Dados Tratados):** Limpeza, padronização de nomes (Case, prefixos), tratamento de nulos e aplicação de regras de negócio.
4.  **Gold (Dados Analíticos):** Modelagem dimensional (Star Schema) baseada na metodologia de **Ralph Kimball**, com tabelas Fato e Dimensão prontas para consumo em BI.

---

## 🛠️ Tecnologias Utilizadas

*   **Databricks Community Edition:** Ambiente de computação em nuvem.
*   **PySpark & Spark SQL:** Motores de processamento de dados.
*   **Delta Lake:** Formato de armazenamento ACID para confiabilidade.
*   **Unity Catalog (Volumes):** Gestão de arquivos na camada Landing.
*   **MkDocs:** Documentação técnica estática.

---

## 📂 Estrutura do Repositório

```bash
├── notebooks/              # Scripts de execução no Databricks
│   ├── 001_Preparando...   # Configuração de schemas e volumes
│   ├── 002_Bronze.py       # Ingestão Landing -> Bronze
│   ├── 003_Silver.py       # Transformação Bronze -> Silver
│   ├── 004_Gold.py         # Modelagem Silver -> Gold (Fato/Dim)
│   └── 005_Destruindo...   # Cleanup do ambiente
├── docs/                   # Documentação detalhada (MKDOCS)
├── mkdocs.yml              # Configuração do site de documentação
└── README.md               # Guia principal do projeto
```

---

## 🚀 Como Executar

### 1. Preparação do Ambiente
No Databricks, crie um cluster (Runtime 13.3 LTS ou superior) e execute o notebook `001_Preparando_ambiente.py` para criar os schemas:
*   `workspace.landing`
*   `workspace.bronze`
*   `workspace.silver`
*   `workspace.gold`

### 2. Carga de Dados (Landing)
Suba os arquivos `.csv` (referentes a apólices, clientes, sinistros, etc.) para o volume criado em:
`/Volumes/workspace/landing/dados/` clicando na barra lateral esquerda escrita "Catalog"

### 3. Execução do Pipeline
Siga a sequência dos notebooks:
1.  **Bronze:** Converte CSV para Delta.
2.  **Silver:** Aplica Data Quality e renomeia colunas para o padrão corporativo.
3.  **Gold:** Alimenta as dimensões (SCD Tipo 1) e a tabela fato de sinistros.

### 4. Automação
Para automação completa, crie um **Databricks Job** encadeando os notebooks 001 a 004.

---

## 📊 Modelagem Dimensional (Gold)

A camada Gold foi projetada para responder perguntas de negócio como:
*   *Qual a quantidade de sinistros por região e período?*
*   *Quais modelos de carros possuem maior incidência de sinistros?*

**Tabelas Criadas:**
*   `dim_carro`
*   `dim_cliente`
*   `dim_localidade`
*   `dim_tempo`
*   `fato_sinistro`

---

## 📄 Documentação Completa
Este projeto utiliza **MKDOCS**. Para visualizar localmente:
1. `pip install -r requirements.txt`
2. `mkdocs serve`
3. Acesse `http://127.0.0.1:8000`

---
⭐ *Trabalho desenvolvido como parte do curso de Engenharia de Dados.*
