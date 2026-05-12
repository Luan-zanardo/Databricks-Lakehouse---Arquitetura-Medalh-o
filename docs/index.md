# Databricks Lakehouse - Arquitetura Medalhão

Bem-vindo à documentação do projeto de Lakehouse utilizando Databricks e a Arquitetura Medalhão.

O objetivo deste projeto é construir um pipeline de dados automatizado que extrai dados de fontes brutas e os transforma em insights através de camadas estruturadas.

## Estrutura das Camadas

*   **Landing**: Dados brutos extraídos da fonte.
*   **Bronze**: Dados convertidos para formato Delta, mantendo a fidelidade à fonte.
*   **Silver**: Dados limpos, validados e enriquecidos.
*   **Gold**: Modelagem dimensional para consumo analítico.
