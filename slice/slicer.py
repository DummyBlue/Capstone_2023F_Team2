import librosa
import numpy as np
from pydub import AudioSegment
import os

# 입력한 녹음 파일의 경로
audio_path = "test.wav"

# 오디오 파일 로드
audio, sr = librosa.load(audio_path, sr=None, mono=True)

# Energy Threshold를 정의합니다. (적절한 값을 찾기 위해 실험 필요)
energy_threshold = 0.01 * np.max(np.abs(audio))

# Energy-based onset detection을 통해 각 키의 시작 시간을 탐지합니다.
onset_frames = librosa.onset.onset_detect(y=audio, sr=sr, backtrack=True, pre_max=20, post_max=20, pre_avg=100, post_avg=100, delta=0.2, wait=0)

# 각 키의 시작과 끝을 찾습니다.
key_starts = onset_frames[:-1] * len(audio) // sr
key_ends = onset_frames[1:] * len(audio) // sr
key_ends = np.append(key_ends, len(audio))

# 'key_slices' 폴더 생성 혹은 이미 존재할 경우 그냥 사용
folder_name = 'key_slices'
os.makedirs(folder_name, exist_ok=True)

# 기존에 저장된 key 코드 삭제
for file in os.listdir(folder_name):
    if file.startswith("key_"):
        os.remove(os.path.join(folder_name, file))

# 각 키를 잘라서 'key_slices' 폴더에 저장합니다.
for idx, (start, end) in enumerate(zip(key_starts, key_ends)):
    key_audio = AudioSegment.from_wav(audio_path)[start:end]
    key_audio.export(os.path.join(folder_name, f"key_{idx}.wav"), format="wav")
