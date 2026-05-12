# Databricks notebook source
# MAGIC %md
### (database/schema) catalogo.schema
### (volume) catalogo.schema.volume

Criando volumes e schemas/databases

# COMMAND ----------

# MAGIC %sql

-- Apagar todas as tabelas da camada bronze
DROP SCHEMA IF EXISTS workspace.bronze CASCADE;

-- Apagar todas as tabelas da camada silver
DROP SCHEMA IF EXISTS workspace.silver CASCADE;

-- Apagar todas as tabelas da camada gold
DROP SCHEMA IF EXISTS workspace.gold CASCADE;

-- Apagar todas as tabelas e volumes da camada landing
DROP SCHEMA IF EXISTS workspace.landing CASCADE;





# COMMAND ----------

# MAGIC %md
## (SQL) SHOW SCHEMAS IN catalogo;

Confirmar se tudo foi limpo

# COMMAND ----------

# MAGIC %sql
SHOW SCHEMAS IN workspace;

# COMMAND ----------

