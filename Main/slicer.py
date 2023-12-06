from pydub import AudioSegment
import os
import librosa
import matplotlib.pyplot as plt

def mp3_slice(file_name):
    # Convert MP3 to WAV
    sound = AudioSegment.from_mp3(f"{file_name}.mp3")
    sound.export(f"{file_name}.wav", format="wav")

    # Define slicing ranges and file names based on specified times for key C
    slicing_ranges = [
        (0.85, 1.25, 'key_g_0'),
        (1.9, 2.3, 'key_g_1'),
        (2.95, 3.35, 'key_g_2'),
        (3.98, 4.38, 'key_g_3'),
        (5.0, 5.45, 'key_g_4'),
        (6.05, 6.45, 'key_g_5'),
        (7.12, 7.52, 'key_g_6'),
        (8.1, 8.5, 'key_g_7'),
        (9.1, 9.5, 'key_g_8'),
        (10.11, 10.51, 'key_g_9'),
        (11.11, 11.51, 'key_g_10'),
        (12.15, 12.55, 'key_g_11'),
        (13.15, 13.55, 'key_g_12'),
        (14.2, 14.6, 'key_g_13'),
        (15.11, 15.51, 'key_g_14')
    ]

    # Load audio file for key ?
    audio = AudioSegment.from_wav(f'{file_name}.wav')

    # Create a folder if it doesn't exist
    folder_name = f'{file_name}_sliced'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Remove existing files with the same names if they exist
    for _, _, filename in slicing_ranges:
        file_path = os.path.join(folder_name, f'{filename}.wav')
        if os.path.exists(file_path):
            os.remove(file_path)

    # Slice audio for each range and save to the 'key_?_sliced' folder
    for start, end, filename in slicing_ranges:
        start_time_ms = int(start * 1000)
        end_time_ms = int(end * 1000)

        extracted_audio = audio[start_time_ms:end_time_ms]
        extracted_audio.export(os.path.join(folder_name, f'{filename}.wav'), format='wav')

        # Load and display the sliced audio using librosa
        file = os.path.join(folder_name, f'{filename}.wav')
        y, sr = librosa.load(file)
        plt.figure(figsize=(10, 3))
        plt.plot(y)
        plt.title(f'Sliced Audio: {filename}')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.show()
