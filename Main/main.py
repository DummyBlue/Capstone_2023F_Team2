from inspector import *
from slicer import *
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
    final_rst = doProcess()
    print(final_rst)

    mid_list = do_comb(final_rst)

    mid2_list = do_conv(mid_list)
    print(mid2_list)

    mid3_list = do_inspect(mid2_list)
    print(mid3_list)

    mid4_list = rm_space(mid3_list)
    print(mid4_list)

    final_list = do_correction(mid4_list)
    print(f"최종 결과: {final_list}")

#main(data_1)