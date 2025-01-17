import requests
import json
import matplotlib.pyplot as plt
import base64
import io
from PIL import Image

def test_api():
    # Adres API
    url = "http://localhost:8080/analyze"
    
    # Dane do wysłania
    data = {
        "data_type": "EEG",
        "noise_level": 0.1,
        "frequency": 10
    }
    
    try:
        print("Wysyłanie zapytania do API...")
        response = requests.post(url, json=data)
        
        # Sprawdzenie odpowiedzi
        response.raise_for_status()  # Rzuci wyjątek dla błędów HTTP
        
        results = response.json()
        
        print("\nOtrzymano odpowiedź!")
        print("\nWyniki analizy:")
        print(json.dumps(results["results"], indent=2))
        
        # Dekodowanie i wyświetlenie obrazu
        print("\nWyświetlanie wykresu...")
        image_bytes = base64.b64decode(results["plot_base64"])
        image = Image.open(io.BytesIO(image_bytes))
        plt.imshow(image)
        plt.axis('off')
        plt.show()
        
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas komunikacji z API: {e}")
        if hasattr(e.response, 'text'):
            print(f"Szczegóły błędu: {e.response.text}")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    test_api()