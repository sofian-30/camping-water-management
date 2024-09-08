
# Projet de Suivi de Consommation d'Eau et de Détection des Fuites

## Description du Projet

Ce projet vise à analyser les données de consommation d'eau d'un camping. Chaque mobile home et embranchement du réseau d'eau est équipé d'un compteur. Le but est de calculer la consommation totale d'eau pour chaque compteur et de détecter les fuites d'eau. 

Les résultats générés incluent :
- **totals.csv** : Le total d'eau consommée par chaque compteur.
- **leaks.csv** : La quantité d'eau perdue par les fuites après chaque compteur.
- **daily_leaks.csv** : Les fuites d'eau par jour, permettant d'identifier les journées avec des fuites importantes.

## Technologies Utilisées

- **Python** : Langage utilisé pour l'analyse des données, sa simplicité et ses nombreuses bibliothèques en font un excellent choix pour ce projet.
- **Pandas** : Utilisé pour manipuler et analyser les données en format CSV.
- **Matplotlib** : Bibliothèque utilisée pour générer des graphiques et visualiser les données.
- **PostgreSQL** : Une base de données relationnelle utilisée pour stocker les données des capteurs.
- **Docker & Docker Compose** : Utilisés pour encapsuler l'application dans des conteneurs et assurer la portabilité et la reproductibilité sur n'importe quel environnement de machine.

## Prérequis

- **Docker** : Assurez-vous que Docker est installé sur votre machine. Vous pouvez le télécharger [ici](https://docs.docker.com/get-docker/).
- **Docker Compose** : Outil pour définir et gérer plusieurs conteneurs Docker à la fois. Il est souvent inclus avec Docker.
- **Git** : Pour cloner le projet sur votre machine. Téléchargez-le [ici](https://git-scm.com/).

### Installation des Dépendances Python

Les dépendances Python utilisées dans ce projet sont listées dans le fichier `requirements.txt`. Vous pouvez générer ce fichier à partir des bibliothèques Python installées dans votre environnement en exécutant :

```bash
pip freeze > requirements.txt
```

Cela capture toutes les versions de bibliothèques actuellement installées, comme :

```
contourpy==1.3.0
cycler==0.12.1
fonttools==4.53.1
kiwisolver==1.4.7
matplotlib==3.9.2
numpy==2.1.1
packaging==24.1
pandas==2.2.2
pillow==10.4.0
pyparsing==3.1.4
python-dateutil==2.9.0.post0
pytz==2024.1
six==1.16.0
tzdata==2024.1
```

Les bibliothèques principales ici sont :
- **Pandas** : Pour le traitement des données.
- **Matplotlib** : Pour la création des graphiques de consommation et des fuites.

## Configuration du Projet avec Docker et Docker Compose

### Étapes d'Installation et de Lancement du Projet

1. **Cloner le dépôt** :

    ```bash
    git clone https://github.com/sofian-30/camping-water-management.git
    cd camping-water-management
    ```

2. **Construire et démarrer les services** :

    Cette étape utilise Docker Compose pour construire deux conteneurs :
    - Un pour l'application Python.
    - Un autre pour la base de données PostgreSQL.

    ```bash
    docker-compose up --build
    ```

3. **PostgreSQL et Base de Données** :

   Le fichier `docker-compose.yml` crée automatiquement une instance PostgreSQL avec les informations suivantes :
   - **Utilisateur** : `postgres`
   - **Mot de passe** : `password`
   - **Nom de la base de données** : `mydatabase`

   Ces informations sont définies dans la section `db` du fichier `docker-compose.yml`. Une fois le conteneur démarré, PostgreSQL est accessible à partir du conteneur de l'application.

4. **Exécution du code** :

   Le script Python principal `main.py` est exécuté automatiquement lorsque le conteneur de l'application est démarré. Il traite les données, détecte les fuites et génère les fichiers de résultats suivants dans le dossier `output` :
   - **totals.csv**
   - **leaks.csv**
   - **daily_leaks.csv**
   - Divers graphiques pour visualiser les résultats.

5. **Vérifiez les sorties** :

   Les fichiers générés et les graphiques sont sauvegardés dans le dossier `output`.

### Structure du Projet

Voici la structure du projet une fois cloné :

```
camping-water-management/
├── app/
├── data/
├── output/
├── src/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── ...
```

- **app/** : Répertoire de travail du conteneur Docker.
- **data/** : Contient les fichiers CSV d'entrée (comme `sensors.csv` et `records.csv`).
- **output/** : Contient les fichiers générés comme les totaux et les graphiques.
- **src/** : Contient le script principal `main.py`.
- **Dockerfile** : Fichier de configuration pour construire l'image Docker de l'application.
- **docker-compose.yml** : Fichier pour orchestrer plusieurs conteneurs Docker.

---

## Notes Importantes

- **Manipulation de la Base de Données** : PostgreSQL est automatiquement configuré via Docker Compose. Aucune action manuelle n'est requise pour la base de données.
- **Volumes Docker** : Le répertoire local `output` est monté dans le conteneur, permettant aux fichiers générés d'être accessibles sur votre machine hôte.
