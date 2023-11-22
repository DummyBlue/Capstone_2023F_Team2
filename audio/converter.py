from pydub import AudioSegment

def mp3_to_wav(mp3_file, wav_file):
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format="wav")

# 변환할 MP3 파일과 저장할 WAV 파일 지정
mp3_file = 'your_mp3_file.mp3' #have to change
wav_file = 'output_wav_file.wav'

# MP3를 WAV로 변환
mp3_to_wav(mp3_file, wav_file)
