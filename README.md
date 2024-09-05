# Projet de Suivi de Consommation d'Eau et de Détection des Fuites

## Description du Projet

Ce projet consiste à analyser les données de consommation d'eau d'un camping, où chaque mobile home et chaque embranchement du réseau d'eau est équipé d'un compteur. L'objectif est de calculer la consommation totale d'eau pour chaque compteur et de détecter la quantité d'eau perdue à cause des fuites.

Les résultats attendus incluent :
- `totals.csv` : le total d'eau consommée par chaque compteur.
- `leaks.csv` : le total d'eau perdue par les fuites après chaque compteur.
- `daily_leaks.csv` : les fuites d'eau par jour pour identifier les jours avec des fuites importantes.

## Technologies Utilisées

- **Python** : Le choix du langage Python est dû à sa simplicité et à sa richesse en bibliothèques pour l'analyse de données.
- **Pandas** : Utilisé pour la manipulation des données. Il permet de lire des fichiers CSV, de traiter les données, et de les analyser facilement.
- **Matplotlib** : Utilisé pour visualiser les résultats. Les graphiques générés permettent de mieux comprendre la répartition de la consommation d'eau et des fuites dans le réseau.
- **Docker** et **Docker Compose** : Pour faciliter l'exécution du projet et garantir un environnement cohérent entre les différentes machines.

## Installation et Exécution du Projet

### Prérequis

- Docker
- Docker Compose

### Étapes d'Exécution

1. Clonez le dépôt du projet :

    ```bash
    git clone https://github.com/sofian-30/camping-water-management.git
    cd votre-projet
    ```

2. Construisez et démarrez les services Docker :

    ```bash
    docker-compose up --build
    ```

   Cette commande construira l'image Docker et démarrera le conteneur.

3. Les scripts Python seront exécutés automatiquement dans le conteneur, générant les fichiers `totals.csv`, `leaks.csv` et `daily_leaks.csv` ainsi que les graphiques pour visualiser les résultats.

4. Les résultats et les graphiques sont sauvegardés dans le répertoire `output` du projet.

## Points d'Évaluation

### Respect des Consignes

Toutes les consignes ont été respectées, notamment le calcul de la consommation totale d'eau et la détection des fuites, avec la génération des fichiers CSV requis.

### Explication du Travail Réalisé

Le projet charge les données des capteurs et des relevés d'eau, vérifie la qualité des données (données manquantes, doublons), et calcule les totaux d'eau consommée ainsi que les pertes d'eau dues aux fuites. Les résultats sont visualisés à l'aide de graphiques pour une meilleure interprétation.

### Clarté et Structure du Code

Le code est structuré de manière claire et organisé en étapes logiques :
1. Chargement des données
2. Vérification des données manquantes et des doublons
3. Calcul des totaux d'eau consommée
4. Détection et calcul des fuites d'eau
5. Fuites d'eau quotidienne
6. Visualisation des résultats


## Commentaires

Les données sont analysées et visualisées pour assurer une compréhension complète des comportements de consommation d'eau et des fuites potentielles. Les outils utilisés sont bien adaptés pour ce type d'analyse et permettent une extensibilité future si des analyses supplémentaires sont nécessaires.