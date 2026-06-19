# Music Genre Classifier

A neural-network experiment created for MISIS in 2023 to classify music genres
from Mel-frequency cepstral coefficients (MFCCs).

## What was implemented

- `preprocess.py` loads 30-second audio tracks, divides them into segments, and
  extracts 13 MFCC coefficients using Librosa.
- `genreClassifier.py` loads the generated feature data, creates a
  training/validation split, and trains a dense TensorFlow classifier for ten
  output classes.

## Technologies

- Python
- Librosa
- NumPy
- scikit-learn
- TensorFlow/Keras

## Running the project

```bash
pip install -r requirements.txt
```

Organize the audio dataset into one directory per genre:

```text
dataset/
├── classical/
├── jazz/
└── rock/
```

Then:

1. Set `DATASET_PATH` and `JSON_PATH` in `preprocess.py`.
2. Extract the MFCC data with `python preprocess.py`.
3. Set `DATA_PATH` in `genreClassifier.py` to the generated JSON file.
4. Train the classifier with `python genreClassifier.py`.

## Known limitations

- The audio dataset is not included.
- Paths are configured directly in the scripts rather than through command-line
  arguments.
- The original experiment showed overfitting and does not include a separate
  test set, cross-validation, model export, or reproducible random seed.
- The network assumes ten genre classes.

## Historical note

The implementation was written by hand before generative AI coding assistants
became widely available. It is preserved as an early machine-learning
experiment, including its original limitations.
