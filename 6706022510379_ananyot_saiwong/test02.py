def find_duplicate_chars_count (s:str) -> dict:
    text= s
    set_word= set()
    char_eng = "abcdefghijklmnopqrstuvwsyz"
    for word in s:
        pure_str =""
    for char in word:
        if char in char_eng:
            pure_str = pure_str+char
        set_word.add(pure_str)
    dict_result = dict()
    for word in set_word:
        dict_result[word]= text.count(word)
    return dict_result
   






if __name__ == "__main__":
    print(find_duplicate_chars_count("programming"))
    print(find_duplicate_chars_count("mississippi"))
    print(find_duplicate_chars_count("abcdefg"))
    print(find_duplicate_chars_count("abacabad"))