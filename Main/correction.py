# This is Correction on Korean Typed words.
# Please Refer https://github.com/HeegyuKim/symspellpy-ko

from symspellpy_ko import KoSymSpell, Verbosity

sym_spell = KoSymSpell()
sym_spell.load_korean_dictionary(decompose_korean=True, load_bigrams=True)

def lookup_words(term):
    for suggestion in sym_spell.lookup_compound(term, max_edit_distance=2): # 편집거리 2 이하
        print(f"{suggestion.term}")
        print(f"{suggestion.distance}")
        print(f"{suggestion.count}")

        return suggestion.term

def do_correction(word):
    tmp = word.strip()
    return lookup_words(tmp)
