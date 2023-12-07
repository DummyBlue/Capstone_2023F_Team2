from inspector import *
from correction import *
from comb import *
from findandreturn import *
from convert import *

def rm_space(list):
    tmp_list = []
    tmp_word = ""
    for k in list:
        if (k != " "):
            tmp_list.append(k)

    for z in tmp_list:
        tmp_word += z

    return tmp_word

if __name__ == '__main__':
    final_rst = doProcess() # 음성을 글자로 변환
    print(final_rst)

    mid_list = do_comb(final_rst) # 성학님 모듈을 이용해 합치기 수행

    mid2_list = do_conv(mid_list) # 영어를 한글로 변환
    print(mid2_list)

    mid3_list = do_inspect(mid2_list) # 글자들 합치기
    print(mid3_list)

    mid4_list = rm_space(mid3_list) # 합치는 과정에서의 공백 제거
    print(mid4_list)

    final_list = do_correction(mid4_list) # 교정 수행
    print(f"최종 결과: {final_list}")

#main(data_1)