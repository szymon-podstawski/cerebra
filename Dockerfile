# Bazowy obraz Pythona
FROM python:3.9-slim

# Ustawienie zmiennych środowiskowych
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Utworzenie i ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie plików projektu
COPY requirements.txt .
COPY src/ ./src/
COPY config.py .
COPY run_production.py .

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Ekspozycja portu
EXPOSE 8080

# Uruchomienie aplikacji
CMD ["python", "run_production.py"] 