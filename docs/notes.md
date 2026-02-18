# Les différentes possibilités d'outils

---

## Big data

Dask plutôt que Spark si petit jeu de données (< 50 Gigas)

## Organistateur/plannificateur de tâches

Airflow pour les gros jeux de données sinon SnakeMake
Airflow plutôt pour industriel et opérationnel / SnakeMake pour la reproductibilité scientifique

SnakeMake fonctionne avec R aussi plus facilement

## Machine Learning

 Joblib pour sauvegrder via python les modeles ML (voir scikit Learn)

## Autres

**YAML** pour les fichiers de **configs** de Snake Make.

# Versionnage

Via GitHub

###################################################################################################

# Le schéma du workflow

Raw Data (CSV / NetCDF / API)
          │
          ▼
   Snakemake Pipeline
   ┌───────────────────┐
   │ Python + Dask     │ <-- Cleaning, aggregation, ETL
   │ R scripts         │ <-- Stats, spatial analyses
   └───────────────────┘
          │
          ▼
   Processed Data / Features
          │
          ▼
   Machine Learning Models
   ┌───────────────────┐
   │ Python ML         │
   │ R Mixed Models    │
   └───────────────────┘
          │
          ▼
   Results (plots, tables, reports)

# La préparation de l'environnement de travail

project/  
├─ data/  
│   ├─ raw/          # données brutes  
│   └─ processed/    # données nettoyées et features  
├─ scripts/  
│   ├─ etl.py        # ETL Python avec Dask  
│   ├─ analysis.R    # analyses R / mixed models  
│   └─ ml.py         # ML Python  
├─ results/  
│   ├─ plots/  
│   ├─ tables/  
│   └─ models/  
├─ config.yaml       # paramètres globaux  
└─ Snakefile         # workflow Snakemake  

---------

# Pour aller plus loin

## Comparaison du workflow avec databrick?

Databricks a l'air d'être beaucoup plus orienté opérationnel et BI. En fait il concentre ce que l'on appelle la **Data Intelligence**.
