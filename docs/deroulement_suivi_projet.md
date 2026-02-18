# Objectif :

Remarque, un mini projet formateur pour la data science est déjà présent sur Toulouse métropole : https://github.com/brooks-code/toulouse-biblio-chronicle/blob/main/README.md

Il se base sur les emprunts de la bibliothèque.

![](assets_deroulement_suivi_projet/2026-01-25-21-32-21-image.png)

---

# Répertoire de travail

On se place dans *~/Documents/Python/projet/AnalyseDataToulouse*

# Choix des données

Données issues de Toulouse Metropole dispo sur https://data.toulouse-metropole.fr/explore/dataset

Possibilité d'utiliser une[ API](https://data.toulouse-metropole.fr/page/outils/) : détail sur le protocole [ici](https://help.opendatasoft.com/apis/ods-explore-v2/)

Les datasets potentiels sont pour le moments : 

- [Inventaire de la Flore sauvage en milieu urbain – ville de Toulouse](https://data.toulouse-metropole.fr/explore/dataset/inventaire-de-la-flore-sauvage-en-milieu-urbain-ville-de-toulouse/information/))
- [Jardins partagés - Toulouse &mdash; Open Data Toulouse Metropole](https://data.toulouse-metropole.fr/explore/dataset/jardins-partages/information/)
- [Part de végétation haute &mdash; Open Data Toulouse Metropole](https://data.toulouse-metropole.fr/explore/dataset/vegetation-iris/information/)
- [Carte des îlots de chaleur urbains (ICU) &mdash; Open Data Toulouse Metropole](https://data.toulouse-metropole.fr/explore/dataset/carte-icu/information/)
- [Part du territoire couvert par la végétation haute de plus de 2 mètres &mdash; Open Data Toulouse Metropole](https://data.toulouse-metropole.fr/explore/dataset/lidar-2m/)
- [Nombre d&#x27;arrêtés de catastrophes naturelles - pour visulisation &mdash; Open Data Toulouse Metropole](https://data.toulouse-metropole.fr/explore/dataset/nombre-darretes-de-catastrophes-naturelles-copie/) (voir juste inondation pour faire le lien avec les arbres)
- [37 Station météo Toulouse université Paul Sabatier &mdash; Open Data Toulouse Metropole](https://data.toulouse-metropole.fr/explore/dataset/37-station-meteo-toulouse-universite-paul-sabatier/) <mark>Beaucoup de données</mark>
- [Arbres urbains &mdash; Open Data Toulouse Metropole](https://data.toulouse-metropole.fr/explore/dataset/arbres-urbains) A l'air intéressant, grand jdd, avec du **géospatial** aussi mais attention aux erreurs de dataset [voir les commentaires](https://data.toulouse-metropole.fr/explore/dataset/arbres-urbains/comments/)

## Chargement des données

Points à prendre en compte avant de charger les données :

- Comment le site nous distribue les données?

- Comment avec Python on récupère celle-ci?

- Quelles manières d'extraction est retenue? On charge toutes les données brutes puis ensuite on filtre via **Python** ou est ce que l'on filtre un premier temps avec la **requete API**?

- Si le jeu de donnée est petit, il est possible de charger directement un csv ou parquet. (<u>mais moins formateur</u>)

### 1) Sur le site de Toulouse Métropole

The Opendatasoft Explore API v2 is organized around REST. It provides access to all the data available through the platform in a coherent, hierarchical way.

- Only the HTTP `GET` method is supported.  <u>IMPORTANT</u>
- All API endpoints return JSON.
- Endpoints are organized in a hierarchical way describing the relative relationship between objects.
- All responses contain a list of links allowing easy and relevant navigation through the API endpoints.
- All endpoints use the [Opendatasoft Query Language (ODSQL)](https://help.huwise.com/apis/ods-explore-v2/#section/Opendatasoft-Query-Language-(ODSQL)). This means that, most of the time, parameters work the same way for all endpoints.
- While the `records` endpoint is subject to a [limited number of returned records](https://help.huwise.com/apis/ods-explore-v2/#tag/Dataset/operation/getRecords), the `exports` endpoint has no limitations. 

### 2) REST API avec Python

La méthode est donnée ici : ([Python and REST APIs: Interacting With Web Services – Real Python](https://realpython.com/api-integration-in-python/#api-endpoints))

Pour résumer, on utilise :

1. la librairie [requests](https://realpython.com/python-requests/)

2. la méthode `GET`

3. la liste de endpoints pour formuler notre demande : [API &mdash; Open Data Toulouse Metropole](https://data.toulouse-metropole.fr/api/explore/v2.1/console)

4. on ressort un fichier **JSON**.

Au final on a un Exemple avec l'api du type :

```
import requests
server = "https://data.toulouse-metropole.fr/api/explore/v2.1"
endpoint = "/catalog/datasets/inventaire-de-la-flore-sauvage-en-milieu-urbain-ville-de-toulouse/records?limit=20"

api_url = server + endpoint
print(api_url)

response = requests.get(api_url)

# Affichage
print(response.json())


print(response.status_code)
print(response.headers["Content-Type"])
```

D'autres infos sont disponibles comme le statut code ou les HTTP headers : [HTTP headers - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

```
>>> response.status_code
200

>>> response.headers["Content-Type"]
'application/json; charset=utf-8'
```

### Problèmes et solutions

Plus d'infos sur les problèmes rencontrés avec l'API et les solutions dans  [/Procédure_API.md](./Procédure_API.md)

## Nettoyage des données

Plusieurs options : 

- Utilisation de OpenRefine ? Sur GithUb, inspiré de Google refine. (Suppression de doublon, correction syntaxe, **facet**)

- Utilisation de Python seuleument ?

- Aurtres ?

## Infos : License des données

Info ici :  [outils data &mdash; Open Data Toulouse Metropole](https://data.toulouse-metropole.fr/page/outils/).

# Mise en place de la chaîne ETL

Pour pouvoir mettre en place une **pipeline** ETL , les données doivent s'y prêter.

1) Récupération depuis différentes sources de types variés

2) Transformation des données 

3) Chargement (load)

4) Envoi vers système cible
   
   Tout cela sous une orchestration et plannification.
   
   <u>Exemple</u>:  

### Package python indispensable

requests /sqlalchemy/ psycopg2-binary / pandas /sqlite3/ => exemple: pip install requests polars sqlalchemy psycopg2-binary

> A Savoir: sqlite3 est pratique pour du local, sinon préférer du MySql/Oracle/PostgreSQL. Plus de détails [ici](./databases_MoreInfos.md)

Pour les gros jeux de données: PySpark / [Polars](https://docs.pola.rs)

[Appropriate Uses For SQLite](https://sqlite.org/whentouse.html)



Polars a un mode read "eager" et un mode scan "lazy" des fichiers. Le premier oblige a lire tout le dataset tandis que le second le "survole". C'est donc plus rapide si on sait déjà ce que l'on cherche. 

> # Versionnage et préparation de l'environnement de travail

On se base sur ce que l'on va utiliser pou compartimenter au mieux les différents éléments, on pourra toujours refusionner si on fait de trop nombreux répertoires.

## Préparation avec git

Via ~~git ~~Bash.

Pour tenir à jour les notebooks, docs, la data.

[Git Push Local Branch to Remote – How to Publish a New Branch in Git](https://www.freecodecamp.org/news/git-push-local-branch-to-remote-how-to-publish-a-new-branch-in-git/)

# Analyses exploratoires

## Multivariées

## Séries temporelles

# Data viz (bonus)

Qlik sense, QlikView, Skywise, 
