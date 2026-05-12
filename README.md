# Databricks Lakehouse - Arquitetura Medalhão

Este projeto implementa um pipeline de dados utilizando o Databricks Free Edition e a arquitetura Medalhão (Landing → Bronze → Silver → Gold).

## Estrutura do Projeto

- `notebooks/`: Contém os notebooks do Databricks.
- `docs/`: Documentação do projeto (MKDOCS).
- `data/`: (Opcional/Referência) Informações sobre a origem dos dados.

## Pipeline

1. **Landing**: Extração de dados (CSV/JSON).
2. **Bronze**: Conversão para Delta Lake.
3. **Silver**: Limpeza e Data Quality.
4. **Gold**: Modelagem Dimensional (Ralph Kimball).
5. **Automação**: Jobs & Pipelines.

## Como Executar

(Instruções serão adicionadas conforme o desenvolvimento)
