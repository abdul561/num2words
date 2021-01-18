import inflect

def num2words():
    num = int(input("write the number :"))
    x = inflect.engine()
    return x.number_to_words(num)
