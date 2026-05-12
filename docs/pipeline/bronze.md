# Camada Bronze

A camada Bronze contém os dados crus em formato Delta Lake.

## Processo
1. Leitura dos arquivos da camada Landing.
2. Adição de metadados (data de processamento, nome do arquivo).
3. Salvamento das tabelas no schema `bronze`.

## Notebooks
- `002_Bronze.py`: Realiza a ingestão dos dados para a camada Bronze.
