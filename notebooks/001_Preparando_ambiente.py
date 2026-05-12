# Databricks notebook source
# MAGIC %sql

CREATE SCHEMA IF NOT EXISTS workspace.landing
COMMENT 'Schema/Database para dados bronze (delta)';

CREATE VOLUME IF NOT EXISTS workspace.landing.dados
COMMENT 'Volume para dados brutos criados no schema/database landing';

CREATE SCHEMA IF NOT EXISTS workspace.bronze
COMMENT 'Schema/Database para dados bronze (delta)';

CREATE SCHEMA IF NOT EXISTS workspace.silver
COMMENT 'Schema/Database para dados silver (delta)';

CREATE SCHEMA IF NOT EXISTS workspace.gold
COMMENT 'Schema/Database para dados gold (delta) - modelagem dimensional';

# COMMAND ----------

# MAGIC %md
### (database/schema) catalogo.schema
### (volume) catalogo.schema.volume

Criando volumes e schemas/databases

# COMMAND ----------

