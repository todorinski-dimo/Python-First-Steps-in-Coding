def transformed(word: str) -> str:
    list_num = []
    list_alpha = []
    word_list = list(word)
    for idx in range(len(word_list)):
        if word_list[idx].isnumeric():
            list_num.append(word_list[idx])
        else:
            list_alpha.append(word_list[idx])
    word_num = "".join(list_num)
    word_alpha = "".join(list_alpha)
    word_int = int(word_num)
    result_word = chr(word_int) + word_alpha
    result_list = list(result_word)
    result_list[1], result_list[-1] = result_list[-1], result_list[1]
    result_word = "".join(result_list)
    return result_word


input_words = input().split()
transformed_words = []

for item in input_words:
    transformed_words.append(transformed(item))
print(" ".join(transformed_words))
