# Camada Landing

A camada Landing é o ponto de entrada dos dados no Lakehouse.

## Processo
1. Extração de dados de bancos de dados relacionais ou não relacionais.
2. Salvamento dos dados em formato bruto (CSV ou JSON) no volume `landing.dados`.

## Notebooks
- `001_Preparando_ambiente.py`: Configura os schemas e volumes necessários.
