from src.analyzer.brain_analyzer import BrainAnalyzer
import logging

def main():
    # Inicjalizacja analizatora
    analyzer = BrainAnalyzer(log_level=logging.INFO)
    
    # Test różnych częstotliwości EEG
    print("\nAnalizowanie EEG z częstotliwością alfa (10 Hz)...")
    eeg_alpha = analyzer.analyze(data_type="EEG", noise_level=0.1, frequency=10)
    print("\nWyniki analizy EEG (fala alfa):", eeg_alpha)
    
    print("\nAnalizowanie EEG z częstotliwością beta (20 Hz)...")
    eeg_beta = analyzer.analyze(data_type="EEG", noise_level=0.1, frequency=20)
    print("\nWyniki analizy EEG (fala beta):", eeg_beta)
    
    # Test fMRI z różnym poziomem szumu
    print("\nAnalizowanie fMRI z niskim szumem...")
    fmri_clear = analyzer.analyze(data_type="fMRI", noise_level=0.1)
    print("\nWyniki analizy fMRI (czysty sygnał):", fmri_clear)

if __name__ == "__main__":
    main() 