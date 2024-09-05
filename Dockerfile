# Utiliser une image Python 3.10 officielle comme base
FROM python:3.10-slim

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source dans le conteneur
COPY . .

# Spécifier la commande à exécuter
CMD ["python", "src/main.py"]
