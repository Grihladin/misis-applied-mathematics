import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras

DATA_PATH = "path/to/mfcc_data.json"


def load_data(data_path: str):
    """Load the training dataset stored in a JSON file.

    Args:
        data_path: Location of the JSON file with MFCCs and genre labels.

    Returns:
        Tuple containing the feature matrix ``X`` and target labels ``y``.
    """

    with open(data_path, "r") as fp:
        data = json.load(fp)

    X = np.array(data["mfcc"])
    y = np.array(data["labels"])

    print("Dataset loaded successfully")

    return X, y


if __name__ == "__main__":

    # Load precomputed MFCC features and genre labels.
    X, y = load_data(DATA_PATH)

    # Hold out a validation split for monitoring generalization.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Build a dense neural network for multi-class genre classification.
    model = keras.Sequential(
        [
            keras.layers.Flatten(input_shape=(X.shape[1], X.shape[2])),
            keras.layers.Dense(512, activation="relu"),
            keras.layers.Dense(256, activation="relu"),
            keras.layers.Dense(64, activation="relu"),
            # Softmax layer maps activations to per-genre probabilities.
            keras.layers.Dense(10, activation="softmax"),
        ]
    )

    # Configure training with Adam optimizer and cross-entropy loss.
    optimiser = keras.optimizers.Adam(learning_rate=0.0001)
    model.compile(
        optimizer=optimiser,
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    model.summary()

    # Train the model and track validation performance each epoch.
    history = model.fit(
        X_train, y_train, validation_data=(X_test, y_test), batch_size=32, epochs=50
    )
