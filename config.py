from pathlib import Path

# Konfiguracja podstawowa
class Config:
    # Podstawowe ustawienia
    API_TITLE = "Brain Analysis API"
    API_VERSION = "1.0.0"
    DEBUG = False
    
    # Ustawienia serwera
    HOST = "0.0.0.0"
    PORT = 8080
    
    # Ścieżki
    BASE_DIR = Path(__file__).parent
    
    # Limity API
    MAX_NOISE_LEVEL = 1.0
    MIN_NOISE_LEVEL = 0.0
    MAX_FREQUENCY = 100.0
    MIN_FREQUENCY = 0.1

# Konfiguracja dla developmentu
class DevelopmentConfig(Config):
    DEBUG = True

# Konfiguracja dla produkcji
class ProductionConfig(Config):
    DEBUG = False 