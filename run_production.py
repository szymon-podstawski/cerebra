import uvicorn
from src.api.brain_api import app
from config import ProductionConfig

if __name__ == "__main__":
    uvicorn.run(
        "src.api.brain_api:app",
        host=ProductionConfig.HOST,
        port=ProductionConfig.PORT,
        workers=4,  # Liczba workerów
        log_level="info",
        reload=False  # Wyłączamy auto-reload w produkcji
    ) 