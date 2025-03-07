# Description générale
Ce projet utilise les données contenues dans un fichier Excel pour construire un modèle de prédiction de la valeur financière d'un bien. J'ai choisi de construire un simple modèle de prédiction car j'estime que l'objet du test est la construction de l'API.

# Objectifs des fichiers dans `app` :
* **app.py** : Contient l'endpoint de l'API du modèle de prédiction.
* **config.py** : Définit le chemin vers le dataset dans la variable `DATA_PATH`.
* **interface.py** : Construit l'interface avec Streamlit et effectue un appel à l'API pour obtenir la prédiction.
* **model_trainings.py** : Le script utilisé pour la construction du modèle de régression.
* **model_predictions.py** : Charge le modèle entraîné et définit une fonction qui prend les données en entrée et retourne la prédiction du modèle.
* **model.joblib** : Le modèle de prédiction entraîné.
* **tools.pkl** : Outils de prétraitement et de normalisation des données.

# Explication du lancement de Docker

Le projet comporte un backend (l'API) et un frontend (l'interface). Les deux sont lancés simultanément. L'API est exposée, puis l'application frontend utilise cette API pour obtenir les résultats.

## Tester l'API localement

Pour tester l'API localement, exécutez les commandes suivantes :

Dans le répertoire du projet de Melissa, lancez :

```
cd melissa_technicaltest
docker-compose up --build
```

Une fois l'application lancée, vous pouvez y accéder via l'adresse suivante : `http://localhost:8501`.

## Utilisation de GitHub Actions pour l'automatisation

J'ai ensuite créé un fichier YAML (voir `./.github/workflows/docker-image.yml`) pour GitHub Actions. Ce fichier automatise la construction de l'image et son importation sur mon Docker Hub à chaque push dans la branche `master`.

## Récupérer la version du conteneur depuis Docker Hub

Pour récupérer la version du conteneur depuis mon Docker Hub (elle est publique) et lancer le conteneur, exécutez les commandes suivantes :

```
docker pull mokhtarimelissa/technicaltest
docker run -d -p 8501:8501 --name melissa_container mokhtarimelissa/technicaltest:latest
```

Ensuite, ouvrez votre navigateur et accédez à l'adresse suivante : `http://localhost:8501/`.

Vous accéderez à une page Streamlit où vous pourrez choisir les paramètres d'entrée et obtenir la prédiction du modèle.
