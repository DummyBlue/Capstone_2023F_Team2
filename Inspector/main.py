# Please Refer: https://github.com/kaniblu/hangul-utils
import hgtk
from hgtk import *

cand_list = []

word_cnt = 0

def isCons(w):
    tmp = ord(w)
    if ((tmp >= 12593) & (tmp <= 12622)): # ㄱ - ㅎ 범위 내인지 판별
        return True
    else:
        return False

def isVow(w):
    tmp = ord(w)
    if ((tmp >= 12623) & (tmp <= 12643)): # ㅏ - ㅣ 범위 내인지 판별
        return True
    else:
        return False

def eval_grammar(wlist):

    outer_list = []
    inner_list = []
    remain_len = len(wlist)
    bypass = 0

    for k in range(0, len(wlist), 1):
        if(bypass > 0):
            bypass -= 1
            continue

        remain_len -= 1
        print(f"\n#{k} Current Key: {wlist[k]}")
        print(inner_list, outer_list, remain_len)

        if(k <= 1):
            inner_list.append(wlist[k])

        else:
            if(isVow(wlist[k-1]) & isVow(wlist[k])): # 모음 + 모음
                inner_list.append(wlist[k])
                print("#1")
                continue

            if(remain_len >= 1):
                if(isVow(wlist[k-1]) & isCons(wlist[k]) & isVow(wlist[k+1])): # 모음 + 자음 + 모음
                    outer_list.append(inner_list.copy())
                    inner_list.clear()
                    inner_list.append(wlist[k])
                    print("#2")
                    continue

            if(remain_len >= 2):
                if(isVow(wlist[k-1]) & isCons(wlist[k]) & isCons(wlist[k+1]) & isVow(wlist[k+2])): # 모음 + 자음 + 자음 + 모음
                    inner_list.append(wlist[k])
                    outer_list.append(inner_list.copy())
                    inner_list.clear()
                    inner_list.append(wlist[k+1])
                    remain_len -= 1
                    bypass = 1
                    print("#3")
                    continue

            if(remain_len >= 3):
                if(isVow(wlist[k-1]) & isCons(wlist[k]) & isCons(wlist[k+1]) & isCons(wlist[k+2]) & isVow(wlist[k+3])): # 모음 + 자음 + 자음 + 자음 + 모음
                    inner_list.append(wlist[k])
                    inner_list.append(wlist[k+1])
                    outer_list.append(inner_list.copy())
                    inner_list.clear()
                    inner_list.append(wlist[k+2])
                    remain_len -= 2
                    bypass = 2
                    print("#4")
                    continue

            inner_list.append(wlist[k])
            print("#Else")

    outer_list.append(inner_list.copy())
    print(outer_list)
    make_one(outer_list)

def make_one(w):
    tmp = ""
    total_tmp = ""
    for k in w:
        print(k)
        for z in k:
            print(z)
            tmp += z

        total_tmp += tmp
        total_tmp += " "
        tmp = ""

    print(f"{hgtk.text.compose(total_tmp)}")

if __name__ == '__main__':
    word_cnt = 0
    #tmp_list = ['ㄱ', 'ㅐ', 'ㄴ', 'ㅏ', 'ㄹ', 'ㅣ']
    #tmp_list = ['ㄱ', 'ㅓ', 'ㅂ', 'ㅜ', 'ㄱ', 'ㅇ', 'ㅣ']
    tmp_list = ['ㅂ', 'ㅜ', 'ㄹ', 'ㄱ' ,'ㅇ', 'ㅡ', 'ㄴ', 'ㅅ', 'ㅐ', 'ㄱ']

    eval_grammar(tmp_list)


