from collections import defaultdict

data = {
    './testdata/turtle/0.wav': {'ㄱ': 80.0, 'ㄴ': 20.0, 'ㄷ': 0.0, 'ㅠ': 0.0, 'ㅊ': 0.0},
    './testdata/turtle/1.wav': {'ㅓ': 80.0, 'ㄴ': 20.0, 'ㅁ': 0.0, 'ㅠ': 0.0, 'ㅊ': 0.0},
    './testdata/turtle/2.wav': {'ㅂ': 100.0, 'ㅏ': 0.0, 'ㅠ': 0.0, 'ㄴ': 0.0, 'ㄷ': 0.0},
    './testdata/turtle/3.wav': {'ㅜ': 100.0, 'ㅁ': 0.0, 'ㅈ': 0.0, 'ㅋ': 0.0, 'ㅇ': 0.0},
    './testdata/turtle/4.wav': {'ㄱ': 80.0, 'ㄴ': 20.0, 'ㅐ': 0.0, 'ㅈ': 0.0, 'ㄴ': 0.0},
    './testdata/turtle/5.wav': {'ㅇ': 100.0, 'ㅏ': 0.0, 'ㅣ': 0.0, 'ㄴ': 0.0, 'ㅋ': 0.0},
    './testdata/turtle/6.wav': {'ㅣ': 100.0, 'ㅌ': 0.0, 'ㅈ': 0.0, 'ㅜ': 0.0, 'ㅕ': 0.0}
}

# 첫 번째 원소만 추출하여 새로운 리스트 생성
first_elements = [list(value.keys())[0] for value in data.values()]

# 첫 번째 원소들의 확률 평균 계산
total_probabilities = defaultdict(int)
count = defaultdict(int)

for key, value in data.items():
    first_key = list(value.keys())[0]
    total_probabilities[first_key] += value[first_key]
    count[first_key] += 1

averages = {key: total_probabilities[key] / count[key] for key in total_probabilities}

print("첫 번째 원소:", first_elements)
print("확률 평균:", averages)
