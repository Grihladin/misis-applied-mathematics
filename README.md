# Music Genre Classifier

A simple neural network that predicts music genres from Mel-frequency cepstral coefficients (MFCCs).

## Prerequisites

Install the required Python packages:

```
pip install -r requirements.txt
```

## Preparing the Dataset

1. Organize your audio files in subfolders named after each genre, e.g. `dataset/rock/*.wav`, `dataset/classical/*.wav`.
2. Update `DATASET_PATH` and `JSON_PATH` at the top of `preprocess.py` to match your folder structure.
3. Run the preprocessing script to extract MFCC features:

```
python preprocess.py
```

This generates a JSON file with MFCC arrays and labels for every segment.

## Training the Model

1. Set `DATA_PATH` in `genreClassifier.py` to point to the JSON generated above.
2. Start training the classifier:

```
python genreClassifier.py
```

The script will split the data into training and validation sets, build a dense neural network, and print accuracy metrics.

## Next Steps

- Experiment with different network architectures or hyperparameters.
- Add evaluation on a separate test set or cross-validation.
- Integrate the model into an application or API endpoint.
