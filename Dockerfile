# Utiliser une image Python légère
FROM python:3.10.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY Pipfile Pipfile.lock /app/
RUN pip install --no-cache-dir pipenv && pipenv install --system --deploy

# Copier le code source de l'interface Streamlit
COPY ui/ /app/ui/

# Exposer le port utilisé par Streamlit
EXPOSE 8501

# Lancer Streamlit
CMD ["streamlit", "run", "ui/streamlit_app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
