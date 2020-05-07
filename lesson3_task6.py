def convert_word(word: str):
    first_ch = word[0]
    code_firs_char = ord(first_ch)-32
    #print(f'first_ch: {first_ch}  type{type(first_ch)}  code:{code_firs_char}')
    convert_char = chr(code_firs_char)
    #print(f'convert_char: {convert_char}  type: {type(convert_char)}')
    return convert_char+word[1:]

def convert_word_v2(word: str):
    little_char_list = list(range('a', 'z'))
    tile_char_list = list(range('A', 'Z'))
    symbol_position = little_char_list.index(word[0])
    result = tile_char_list[symbol_position]+word[1:]
    return result

def conver_words(words: str):
    final_word_list = ''
    for word in words.split():
        final_word_list = final_word_list + convert_word(word) + ' '
    return final_word_list

words_list = input('Введите набор латинских слов разделенных пробелом:')
print (conver_words(words_list))
