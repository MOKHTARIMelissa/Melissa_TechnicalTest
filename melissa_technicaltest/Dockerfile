# Utiliser une image officielle Python comme image parent
FROM python:3.12

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application dans le conteneur
COPY ./app /app

# Installer uvicorn pour FastAPI et streamlit pour l'interface
RUN pip install uvicorn streamlit

# Exposer les ports nécessaires
EXPOSE 8000 8501

# Lancer les deux applications simultanément
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000 & streamlit run interface.py"]
