# Automação

O pipeline é automatizado utilizando Databricks Jobs.

## Configuração do Job
O Job encadeia a execução dos notebooks na seguinte ordem:
1. `001_Preparando_ambiente.py`
2. `002_Bronze.py`
3. `003_Silver.py`
4. `004_Gold.py`

Ao final do ciclo de vida, o notebook `005_Destruindo_ambiente.py` pode ser utilizado para limpeza, se necessário.
