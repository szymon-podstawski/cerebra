from src.analyzer.brain_analyzer import BrainAnalyzer
from pathlib import Path


def main():
    analyzer = BrainAnalyzer()
    data_path = Path("data/sample.nii")  # przykładowa ścieżka
    results = analyzer.analyze(data_path, "fMRI")
    print(f"Analiza zakończona: {results['status']}")

if __name__ == "__main__":
    main()
