from pathlib import Path
from nilearn import datasets
import mne.datasets
import shutil

def download_sample_data():
    # Tworzenie katalogu na dane
    data_dir = Path("dane")
    data_dir.mkdir(exist_ok=True)
    
    print("Pobieranie przykładowych danych...")
    
    # Pobieranie przykładowych danych fMRI
    print("\nPobieranie danych fMRI...")
    adhd = datasets.fetch_adhd(n_subjects=1)
    fmri_file = Path(adhd.func[0])
    
    # Kopiowanie pliku fMRI do naszego katalogu
    shutil.copy(fmri_file, data_dir / "przyklad_fmri.nii")
    
    # Pobieranie przykładowych danych EEG
    print("\nPobieranie danych EEG...")
    sample_data_folder = mne.datasets.sample.data_path()
    eeg_file = Path(sample_data_folder) / "MEG" / "sample" / "sample_audvis_raw.fif"
    
    # Kopiowanie pliku EEG do naszego katalogu
    shutil.copy(eeg_file, data_dir / "przyklad_eeg.fif")
    
    print("\nDane zostały pobrane i zapisane w katalogu 'dane'")
    print(f"fMRI: {data_dir/'przyklad_fmri.nii'}")
    print(f"EEG: {data_dir/'przyklad_eeg.fif'}")

if __name__ == "__main__":
    download_sample_data() 