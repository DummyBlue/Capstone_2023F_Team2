data = {
    './testdata/turtle/0.wav': {'ㄱ': 80.0, 'ㄴ': 20.0, 'ㄷ': 0.0, 'ㅠ': 0.0, 'ㅊ': 0.0},
    './testdata/turtle/1.wav': {'ㅓ': 80.0, 'ㄴ': 20.0, 'ㅁ': 0.0, 'ㅠ': 0.0, 'ㅊ': 0.0},
    './testdata/turtle/2.wav': {'ㅂ': 100.0, 'ㅏ': 0.0, 'ㅠ': 0.0, 'ㄴ': 0.0, 'ㄷ': 0.0},
    './testdata/turtle/3.wav': {'ㅜ': 100.0, 'ㅁ': 0.0, 'ㅈ': 0.0, 'ㅋ': 0.0, 'ㅇ': 0.0},
    './testdata/turtle/4.wav': {'ㄱ': 80.0, 'ㄴ': 20.0, 'ㅐ': 0.0, 'ㅈ': 0.0, 'ㄴ': 0.0},
    './testdata/turtle/5.wav': {'ㅇ': 100.0, 'ㅏ': 0.0, 'ㅣ': 0.0, 'ㄴ': 0.0, 'ㅋ': 0.0},
    './testdata/turtle/6.wav': {'ㅣ': 100.0, 'ㅌ': 0.0, 'ㅈ': 0.0, 'ㅜ': 0.0, 'ㅕ': 0.0}
}

# 각 딕셔너리의 첫 번째 원소 추출
first_elements = [list(value.keys())[0] for value in data.values()]

# 수치를 평균내기 위한 리스트 생성
probabilities = []

# 각 첫 번째 원소에 해당하는 수치 추출 및 평균 계산
for key in first_elements:
    # 해당 첫 번째 원소의 수치 추출하여 리스트에 추가
    probs = [dic[key] for dic in data.values() if key in dic]
    # 평균 계산하여 probabilities 리스트에 추가
    average_prob = sum(probs) / len(probs)
    probabilities.append(average_prob)

# 결과 출력
result = dict(zip(first_elements, probabilities))
print(result)
