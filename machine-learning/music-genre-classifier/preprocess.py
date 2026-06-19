import json
import os
import math
import librosa

DATASET_PATH = "path/to/dataset"
JSON_PATH = "path/to/output.json"
SAMPLE_RATE = 22050
TRACK_DURATION = 30  # seconds
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION


def save_mfcc(
    dataset_path: str,
    json_path: str,
    num_mfcc: int = 13,
    n_fft: int = 2048,
    hop_length: int = 512,
    num_segments: int = 5,
) -> None:
    """Extract MFCC features from a dataset and persist them with genre labels.

    Args:
        dataset_path: Root directory containing genre folders with audio files.
        json_path: Destination file where extracted data will be written as JSON.
        num_mfcc: Number of MFCC coefficients to compute per frame.
        n_fft: Window size (in samples) for the FFT.
        hop_length: Hop length (in samples) between successive frames.
        num_segments: Number of equal segments to slice each track into.
    """

    # Collected metadata and MFCC vectors will be stored in this structure.
    data = {"mapping": [], "labels": [], "mfcc": []}

    samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    num_mfcc_vectors_per_segment = math.ceil(samples_per_segment / hop_length)

    # Walk through every genre directory and its audio files.
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):

        if dirpath != dataset_path:

            semantic_label = dirpath.split("/")[-1]
            data["mapping"].append(semantic_label)
            print("\nProcessing: {}".format(semantic_label))

            for f in filenames:

                file_path = os.path.join(dirpath, f)
                signal, sample_rate = librosa.load(file_path, sr=SAMPLE_RATE)

                # Slice each track into equal segments to increase data diversity.
                for d in range(num_segments):

                    start = samples_per_segment * d
                    finish = start + samples_per_segment

                    # Compute MFCC features for the current segment window.
                    mfcc = librosa.feature.mfcc(
                        y=signal[start:finish],
                        sr=sample_rate,
                        n_fft=n_fft,
                        n_mfcc=num_mfcc,
                        hop_length=hop_length,
                    )
                    mfcc = mfcc.T

                    # Persist only segments with the expected frame count.
                    if len(mfcc) == num_mfcc_vectors_per_segment:
                        data["mfcc"].append(mfcc.tolist())
                        data["labels"].append(i - 1)
                        print("{}, segment:{}".format(file_path, d + 1))

    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=4)


if __name__ == "__main__":
    save_mfcc(DATASET_PATH, JSON_PATH, num_segments=10)
