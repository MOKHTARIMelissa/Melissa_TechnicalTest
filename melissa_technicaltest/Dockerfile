# Utiliser l'image Python 3.12
FROM python:3.12

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code source
COPY . .

# Exposer les ports de FastAPI et Streamlit
EXPOSE 8000 8501

# Commande par défaut (sera écrasée par docker-compose)
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
