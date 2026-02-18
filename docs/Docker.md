# Docker

## Installation

[Windows Installation | Docker Docs](https://docs.docker.com/desktop/setup/install/windows-install)

## A savoir

Si la version Windows est non professionnelle, on ne peut avoir que des **conteneurs Linux**.

> Containers and images created with Docker Desktop are shared between all user accounts on machines where it is installed. This is because all Windows accounts use the same VM to build and run containers. Note that it is not possible to share containers and images between user accounts when using the Docker Desktop WSL 2 backend.

### Hyper-V ou WSL?

[Hyper-V vs WSL: How To Pick The Right Tool?](https://pmbanugo.me/blog/hyperv-wsl-on-windows)

...

# Différences entre Images et Conteneurs

[Docker : image vs container - IONOS](https://www.ionos.fr/digitalguide/serveur/configuration/docker-image-vs-container/)

-------

# Lexique

## Containers

Le conteneur est toute l'application en elle même et son environnement, modifiables en temps réel. Les conteneurs sont des "**unités d’exécution isolées pour les applications et leurs dépendances**"

### [Container images](https://docs.docker.com/get-started/introduction/build-and-push-first-image/#container-images)

If you’re new to container images, think of them as a standardized package that contains everything needed to run an application, including its files, configuration, and dependencies. These packages can then be distributed and shared with others.

> Docker hub a un catalogue d'Images Officielle (exemple: base MySQL ou [PostGRESQL](https://www.datacamp.com/tutorial/postgresql-docker))
> 
> - [Explore Docker&#x27;s Container Image Repository | Docker Hub](https://hub.docker.com/search?badges=official&_gl=1*1asfnmm*_gcl_au*ODA0NDkyOTc1LjE3NzA2NTUxNjQ.*_ga*NzA2NDcxNDgwLjE3NzA2NTUxNjQ.*_ga_XJWPQMJYHQ*czE3NzA3NDc0NzckbzMkZzEkdDE3NzA3NDc2MzMkajYwJGwwJGgw)
> 
> - https://hub.docker.com/hardened-images/catalog?_gl=1*1c2mix7*_gcl_au*ODA0NDkyOTc1LjE3NzA2NTUxNjQ.*_ga*NzA2NDcxNDgwLjE3NzA2NTUxNjQ.*_ga_XJWPQMJYHQ*czE3NzA3NDc0NzckbzMkZzEkdDE3NzA3NDc2MzMkajYwJGwwJGgw

Attention les images ne sont pas visible depuis le Windows explorer file! Puisqu'elle sont dans un conteneur, environnement isolé, on ne peut les voir qu'avec les commandes docker. Donc c'est important de se souvenir de vérifier les contenus Docker si on doit gérer la mémoire du PC.

## Volumes

Les données disparaissent quand un conteneur s'arrête de tourner, on ne veut pas cela dans le cas des databases. Les volumes permets de conserver ces données importantes à l'arrêt du conteneur.

... 

------------

# Commandes utiles

## Création image

```
# Création de l'image
docker build -t <DOCKER_USERNAME>/getting-started-todo-app .

# Vérif 
docker image ls
```

<u>Attention</u> : Au moment de créer l'image le `DOCKER_USERNAME` doit être exactement le notre (celui du compte), sinon on ne pourra pas push sur le serveur ! 

```
# lister les images
  docker images
```

## Push de l'image sur le serveur

```
docker push <DOCKER_USERNAME>/getting-started-todo-app
```

## Suppression des image: [docker image rm | Docker Docs](https://docs.docker.com/reference/cli/docker/image/rm/#:~:text=You%20can%20remove%20an%20image,image%20is%20removed%20by%20tag.)

## Liste des conteneur actifs

```
docker ps
```

## Relancer et arrêter un conteneur déjà créé

```
docker restart <DOCKER_ID> 
```

```
docker stop <DOCKER_ID> 
```

# Docker compose

Dès que l'on a plusieurs applications qui doivent communiquer entre elles et donc **plusieurs conteneurs**, cela devient très vite compliqué de tout manier via les CLI, une solution et de retranscrire toute les spécifications sur un seul fichier `yml`.

Docker compose se dépatouille ensuite avec.

<u>Exemple</u>: 

```
ervices:
  postgres:
    image: postgres:16
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: pass
    volumes:
      - pgdata:/var/lib/postgresql/data


```

Important:

Pour  le **volume**: 

```
  - pgdata:/var/lib/postgre
```

Ce qui est avant les `:` est le chemin monté sur Windows, ce qui est apres et le repère des dossiers pour Docker en lui même. 

On aura seulement à réactiver ou activer avec:

```
docker compose down -v
docker compose up -d
```

# Connexion via autres applications

On pourra ensuite se connecter via <u>Dbeaver </u>(pas forcément lui même dans un container) en précisant Host:Localhost et le port (exemple au dessus:5432). 

Préciser aussi les mêmes "Users credentials".

De même pour <u>Python</u> grâce au package `psycopg2` spécialement conçu pour PostgreSQL

```
import psycopg2

# ⚠️ Modifie ces paramètres si nécessaire
host = "localhost"
port = 5432
dbname = "test_db"
user = "admin"
password = "louvre"

# 1️⃣ Connexion
conn = psycopg2.connect(
    host=host,
    port=port,
    dbname=dbname,
    user=user,
    password=password
)

cur = conn.cursor()

# 2️⃣ Création d'une table simple
cur.execute("""
CREATE TABLE IF NOT EXISTS test_table (
    id SERIAL PRIMARY KEY,
    name TEXT,
    value INTEGER
);
""")
conn.commit()

# 3️⃣ Insertion d'une ligne
cur.execute("""
INSERT INTO test_table (name, value) VALUES (%s, %s)
""", ("exemple", 42))
conn.commit()

# 4️⃣ Lecture pour vérifier
cur.execute("SELECT * FROM test_table;")
rows = cur.fetchall()
for row in rows:
    print(row)

# 5️⃣ Fermeture
cur.close()
conn.close()

```






