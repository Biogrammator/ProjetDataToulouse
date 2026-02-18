# Quelles base de données choisir selon ses objectifs ?

- [Faire le bon choix entre MySQL et PostgreSQL](https://www.data-bird.co/blog/postgresql-vs-mysql)

- https://www.astera.com/fr/knowledge-center/postgresql-vs-oracle/

# PostGreSQL

Respecte les principes [ACID](https://en.wikipedia.org/wiki/ACID)

### Troubleshoot

Parfois les logiciels complexes comme PostgreSQl ont besoin de repères précis, comme des noms de **groupes systèmes**. Dans mon cas, le groupe **Administrator** est demandé par PostgreSQL mais je n'ai que **Administrateurs**.

Le meilleur moyen d'éviter dans des complications sur les modifications machine est de créer des environnement isolés tels que les **conteneurs**. Ceci est réalisable avec **Docker** par exemple.On peut même envoyer ces conteneur sur d'autres machine sans avoir à réinstaller PostgreSQL !

[Introduction | Docker Docs](https://docs.docker.com/get-started/introduction/)

Plus de détail sur **Docker** dans [./Docker.md](./Docker.md)

# Oracle

Oracle est <mark>payant</mark>! 

# Serveur pour héberger sa base de données :

- https://neon.com/

- [Miget - Modern Platform as a Service](https://miget.com/#sign-up-now)

- ## https://aiven.io/postgresql

## PostGres: quelques TIPS
