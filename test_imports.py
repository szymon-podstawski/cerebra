def test_imports():
    try:
        print("Sprawdzanie importów...")
        
        print("Importowanie numpy...")
        import numpy as np
        print("✓ numpy zaimportowane poprawnie")
        
        print("Importowanie nibabel...")
        import nibabel as nib
        print("✓ nibabel zaimportowane poprawnie")
        
        print("Importowanie mne...")
        import mne
        print("✓ mne zaimportowane poprawnie")
        
        print("Importowanie matplotlib...")
        import matplotlib.pyplot as plt
        print("✓ matplotlib zaimportowane poprawnie")
        
        print("Importowanie seaborn...")
        import seaborn as sns
        print("✓ seaborn zaimportowane poprawnie")
        
        print("\nWszystkie biblioteki zostały zaimportowane poprawnie!")
        return True
        
    except ImportError as e:
        print(f"\n❌ Błąd importowania: {str(e)}")
        print("\nSpróbuj zainstalować brakującą bibliotekę używając:")
        print(f"pip install {str(e).split()[-1]}")
        return False

if __name__ == "__main__":
    test_imports() 