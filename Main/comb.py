import hgtk

data_0 = {
    './testdata/turtle/0.wav': {'ㅏ': 80.0, 'ㄱ': 20.0, 'ㄷ': 0.0, 'ㅠ': 0.0, 'ㅊ': 0.0},
    './testdata/turtle/1.wav': {'ㄷ': 80.0, 'ㅓ': 70.0, 'ㅁ': 0.0, 'ㅠ': 0.0, 'ㅊ': 0.0},
    './testdata/turtle/2.wav': {'ㅂ': 100.0, 'ㅏ': 0.0, 'ㅠ': 0.0, 'ㄴ': 0.0, 'ㄷ': 0.0},
    './testdata/turtle/3.wav': {'ㅜ': 100.0, 'ㅁ': 0.0, 'ㅈ': 0.0, 'ㅋ': 0.0, 'ㅇ': 0.0},
    './testdata/turtle/4.wav': {'ㄱ': 80.0, 'ㄴ': 20.0, 'ㅐ': 0.0, 'ㅈ': 0.0, 'ㄴ': 0.0},
    './testdata/turtle/5.wav': {'ㅇ': 100.0, 'ㅏ': 0.0, 'ㅣ': 0.0, 'ㄴ': 0.0, 'ㅋ': 0.0},
    './testdata/turtle/6.wav': {'ㅣ': 100.0, 'ㅌ': 0.0, 'ㅈ': 0.0, 'ㅜ': 0.0, 'ㅕ': 0.0}
}

data_1 = {
    './testdata/turtle/0.wav': {'ㅏ': 80.0, 'ㅁ': 20.0, 'ㄷ': 0.0, 'ㅠ': 0.0, 'ㅊ': 0.0},
    './testdata/turtle/1.wav': {'ㄷ': 80.0, 'ㅏ': 70.0, 'ㅁ': 0.0, 'ㅠ': 0.0, 'ㅊ': 0.0},
    './testdata/turtle/2.wav': {'ㅂ': 100.0, 'ㅏ': 0.0, 'ㅠ': 0.0, 'ㄴ': 0.0, 'ㄷ': 0.0},
    './testdata/turtle/3.wav': {'ㄱ': 100.0, 'ㅁ': 0.0, 'ㅈ': 0.0, 'ㅋ': 0.0, 'ㅇ': 0.0},
    './testdata/turtle/4.wav': {'ㅊ': 80.0, 'ㄴ': 20.0, 'ㅐ': 0.0, 'ㅈ': 0.0, 'ㄴ': 0.0},
    './testdata/turtle/5.wav': {'ㅇ': 100.0, 'ㅏ': 0.0, 'ㅣ': 0.0, 'ㄴ': 0.0, 'ㅋ': 0.0},
    './testdata/turtle/6.wav': {'ㅗ': 100.0, 'ㅌ': 0.0, 'ㅈ': 0.0, 'ㅜ': 0.0, 'ㅕ': 0.0},
    './testdata/turtle/7.wav': {'ㅣ': 100.0, 'ㅌ': 0.0, 'ㅈ': 0.0, 'ㅜ': 0.0, 'ㅕ': 0.0}
}

cons_list = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']
vows_list = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm']

# 자음 모음 판별기
def isCons(w):
    #tmp = ord(w)
    #return 12593 <= tmp <= 12622  # 자음 판별기
    if w in cons_list:
        return True
    else:
        return False

def isVow(w):
    #tmp = ord(w)
    #return 12623 <= tmp <= 12643  # 모음 판별기
    if w in vows_list:
        return True
    else:
        return False


# data를 바탕으로 Rule을 만족하는 list 만들기
def select_order(data):
    order = []
    cnt = 0  # list 추가 횟수
    c_cnt = 0  # 자음 등장 횟수
    v_cnt = 0  # 모음 등장 횟수

    for key, value in data.items():
        for item in value:
            if cnt == 0 and isCons(item):  # Rule 1: order에 추가될 첫 번째 요소는 자음이다
                order.append(item)
                cnt += 1
                # c_cnt += 1
                break
            elif cnt == 1 and isVow(item):  # Rule 2: order에 추가될 두 번째 요소는 모음이다
                order.append(item)
                cnt += 1
                v_cnt += 1
                break

            elif cnt > 1:
                if c_cnt >= 3: # Rule 3: order에는 자음이 연속으로 3번까지만 추가할 수 있다
                    if isVow(item):
                        order.append(item)
                        c_cnt = 0
                        v_cnt += 1
                        break
                elif v_cnt >=2: # Rule 4: order에는 모음이 연속으로 2번까지만 추가할 수 있다
                    if isCons(item):
                        order.append(item)
                        v_cnt = 0
                        c_cnt += 1
                        break
                else:
                    if isVow(item):
                        order.append(item)
                        c_cnt = 0
                        v_cnt += 1
                        break
                    elif isCons(item):
                        order.append(item)
                        v_cnt = 0
                        c_cnt += 1
                        break
    return order


# 생성한 list를 바탕으로 확률 평균값 도출
def calculate_average(data, order):
    result = []

    for item in order:
        for key, value in data.items():
            if item in value:
                result.append(value[item])
                break

    average = sum(result) / len(result)
    return average


# 출력 함수
def do_comb(data):
    order = select_order(data)
    print(order)
    average = calculate_average(data, order)
    print(average)
    return order
