import sys
from pathlib import Path

def test_package_structure():
    print("Sprawdzanie struktury pakietu...")
    
    # Wyświetl ścieżki Pythona
    print("\nŚcieżki Pythona:")
    for path in sys.path:
        print(f"- {path}")
    
    # Sprawdź strukturę katalogów
    current_dir = Path.cwd()
    print(f"\nBieżący katalog: {current_dir}")
    
    expected_dirs = ['src', 'tests']
    expected_files = {
        'src': ['__init__.py'],
        'src/analyzer': ['__init__.py', 'brain_analyzer.py'],
        'src/visualization': ['__init__.py', 'plotting.py'],
        'tests': ['__init__.py', 'test_brain_analyzer.py']
    }
    
    print("\nSprawdzanie struktury katalogów i plików:")
    for dir_name in expected_dirs:
        dir_path = current_dir / dir_name
        if dir_path.exists():
            print(f"✓ Katalog {dir_name} istnieje")
            for file_name in expected_files[dir_name]:
                file_path = dir_path / file_name
                if file_path.exists():
                    print(f"  ✓ Plik {file_name} istnieje")
                else:
                    print(f"  ❌ Brak pliku {file_name}")
        else:
            print(f"❌ Brak katalogu {dir_name}")
    
    # Sprawdź podkatalogi src
    for subdir in ['analyzer', 'visualization']:
        dir_path = current_dir / 'src' / subdir
        if dir_path.exists():
            print(f"\nSprawdzanie {subdir}:")
            for file_name in expected_files[f'src/{subdir}']:
                file_path = dir_path / file_name
                if file_path.exists():
                    print(f"  ✓ Plik {file_name} istnieje")
                else:
                    print(f"  ❌ Brak pliku {file_name}")
        else:
            print(f"❌ Brak katalogu src/{subdir}")

if __name__ == "__main__":
    test_package_structure() 