from word2number import w2n
from num2words import num2words


def two_number():

    first_user_input = input("First Word: ")
    second_user_input = input("Second Word: ")

    first_convert = w2n.word_to_num(first_user_input)
    second_convert = w2n.word_to_num(second_user_input)

    total = first_convert + second_convert

    first_convert_word = num2words(first_convert)
    second_convert_word = num2words(second_convert)
    result = num2words(total)
    print()

    print("First Word:", first_convert_word)
    print("second word:", second_convert_word)
    print("Result:", result)

two_number()
