import os
from glob import glob

import librosa
import soundfile

SAMPLE_RATE = 16000
IS_MONO = True
DURATION = 1.7  # sec

duration_in_values = int(DURATION * SAMPLE_RATE)
path = ""
output_path = ""


def audio_slicer(data):
    while data.shape[0] > duration_in_values:
        audio_slice = data[:duration_in_values]
        yield audio_slice
        data = data[duration_in_values:]


os.makedirs(output_path)
for path_to_file in sorted(glob(f"{path}/*.wav")):
    audio, sr = librosa.load(path_to_file, sr=SAMPLE_RATE, mono=IS_MONO)
    for i, slc in enumerate(audio_slicer(audio)):
        soundfile.write(file=f"{output_path}/{path_to_file.split('/')[-1][:-4]}_{i}.wav",
                        data=slc, samplerate=SAMPLE_RATE)
        print(f"Saved {output_path}/{path_to_file.split('/')[-1][:-4]}_{i}.wav")
