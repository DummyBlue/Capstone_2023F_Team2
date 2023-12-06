# 영어를 한글로 바꿔줍니다.

cons_list = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']
vows_list = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm']

cons_ko = ['ㅂ', 'ㅈ', 'ㄷ', 'ㄱ', 'ㅅ', 'ㅁ', 'ㄴ', 'ㅇ', 'ㄹ', 'ㅎ', 'ㅋ', 'ㅌ', 'ㅊ', 'ㅍ']
vows_ko = ['ㅛ', 'ㅕ', 'ㅑ', 'ㅐ', 'ㅔ', 'ㅗ', 'ㅓ', 'ㅏ', 'ㅣ', 'ㅠ', 'ㅜ', 'ㅡ']

def do_conv(list):
    tmp_list = []

    for k in list:
        if k in cons_list:
            tmp_list.append(cons_ko[cons_list.index(k)])
        else:
            tmp_list.append(vows_ko[vows_list.index(k)])

    return tmp_list